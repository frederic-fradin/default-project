"""Trames et messages échangés entre le PC et l'objet (ADR 007).

Trame : marqueur "DT", type (1 octet), longueur de la charge (4 octets), charge, CRC32 du type,
de la longueur et de la charge. Entiers petit-boutistes. Le firmware C++ doit produire et lire
exactement les mêmes octets.
"""

import struct
import zlib

PROTOCOL_VERSION = 1
MARKER = b"DT"

HELLO_REQ = 0x01
HELLO = 0x02
DRAW = 0x10
LED = 0x11
KEY = 0x20
WHEEL = 0x21
DONE = 0x30
ERROR = 0x3F

MODE_FULL = 0
MODE_FAST = 1

ERROR_FRAME = 1  # CRC faux
ERROR_TYPE = 2  # type de message inconnu
ERROR_SIZE = 3  # charge de mauvaise taille ou valeur invalide
ERROR_ZONE = 4  # zone de DRAW hors de l'écran ou x / largeur impairs

# Une page entière fait 259 200 octets : au-delà, la longueur lue est forcément corrompue.
MAX_PAYLOAD = 300_000

# Format struct et noms des champs de chaque message. Les pixels de DRAW suivent les champs.
FORMATS = {
    HELLO_REQ: ("<", ()),
    HELLO: ("<BHHHBB", ("protocol", "firmware", "width", "height", "bpp", "keys")),
    DRAW: ("<HHHHB", ("x", "y", "width", "height", "mode")),
    LED: ("<BBBB", ("target", "red", "green", "blue")),
    KEY: ("<BB", ("key", "pressed")),
    WHEEL: ("<b", ("steps",)),
    DONE: ("<B", ("handled",)),
    ERROR: ("<B", ("code",)),
}

NAMES = {
    HELLO_REQ: "HELLO_REQ",
    HELLO: "HELLO",
    DRAW: "DRAW",
    LED: "LED",
    KEY: "KEY",
    WHEEL: "WHEEL",
    DONE: "DONE",
    ERROR: "ERROR",
}


def encode_frame(msg_type, payload=b""):
    body = struct.pack("<BI", msg_type, len(payload)) + payload
    return MARKER + body + struct.pack("<I", zlib.crc32(body))


def encode(msg_type, **fields):
    """Trame complète d'un message, ex. encode(KEY, key=0, pressed=1)."""
    fmt, names = FORMATS[msg_type]
    payload = struct.pack(fmt, *(fields[name] for name in names))
    return encode_frame(msg_type, payload + fields.get("pixels", b""))


def decode(msg_type, payload):
    """Charge d'une trame → dictionnaire des champs, avec "type" (et "pixels" pour DRAW)."""
    if msg_type not in FORMATS:
        raise ValueError(f"type de message inconnu : {msg_type:#04x}")
    fmt, names = FORMATS[msg_type]
    size = struct.calcsize(fmt)
    if len(payload) < size or (msg_type != DRAW and len(payload) != size):
        raise ValueError(f"{NAMES[msg_type]} : charge de {len(payload)} octets")
    message = dict(zip(names, struct.unpack(fmt, payload[:size])))
    message["type"] = msg_type
    if msg_type == DRAW:
        message["pixels"] = payload[size:]
    return message


def check_draw(message, screen_width, screen_height):
    """Code d'erreur d'un DRAW invalide, ou None s'il est correct."""
    x, y, width, height = message["x"], message["y"], message["width"], message["height"]
    if x % 2 or width % 2 or x + width > screen_width or y + height > screen_height:
        return ERROR_ZONE
    if message["mode"] not in (MODE_FULL, MODE_FAST) or len(message["pixels"]) != width * height // 2:
        return ERROR_SIZE
    return None


def read_frame(stream):
    """Lit la prochaine trame : (type, charge), ou None si la connexion est fermée.

    Ignore les octets qui précèdent le marqueur, pour se recaler après une trame abîmée.
    Lève ValueError si le CRC est faux ou la longueur impossible.
    """
    previous = b""
    while True:
        byte = stream.read(1)
        if not byte:
            return None
        if previous + byte == MARKER:
            break
        previous = byte
    body = _read_exact(stream, 5)
    if body is None:
        return None
    msg_type, length = struct.unpack("<BI", body)
    if length > MAX_PAYLOAD:
        raise ValueError(f"longueur impossible : {length} octets")
    payload = _read_exact(stream, length)
    crc = _read_exact(stream, 4)
    if payload is None or crc is None:
        return None
    if struct.unpack("<I", crc)[0] != zlib.crc32(body + payload):
        raise ValueError("CRC faux")
    return msg_type, payload


def _read_exact(stream, size):
    data = b""
    while len(data) < size:
        chunk = stream.read(size - len(data))
        if not chunk:
            return None
        data += chunk
    return data
