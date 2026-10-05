import io
import zlib

import pytest

from src import protocol


def read(data):
    return protocol.read_frame(io.BytesIO(data))


def test_key_frame_bytes():
    frame = protocol.encode(protocol.KEY, key=1, pressed=1)
    body = b"\x20\x02\x00\x00\x00\x01\x01"
    assert frame == b"DT" + body + zlib.crc32(body).to_bytes(4, "little")


@pytest.mark.parametrize(
    "msg_type, fields",
    [
        (protocol.HELLO_REQ, {}),
        (protocol.HELLO, {"protocol": 1, "firmware": 3, "width": 960, "height": 540, "bpp": 4, "keys": 4}),
        (protocol.LED, {"target": 4, "red": 255, "green": 60, "blue": 0}),
        (protocol.KEY, {"key": 3, "pressed": 0}),
        (protocol.WHEEL, {"steps": -2}),
        (protocol.DONE, {"handled": protocol.DRAW}),
        (protocol.ERROR, {"code": protocol.ERROR_ZONE}),
        (protocol.DRAW, {"x": 10, "y": 20, "width": 4, "height": 2, "mode": 1, "pixels": b"\x0f\xf0\x12\x34"}),
    ],
)
def test_round_trip(msg_type, fields):
    msg_type_read, payload = read(protocol.encode(msg_type, **fields))
    assert msg_type_read == msg_type
    assert protocol.decode(msg_type, payload) == {**fields, "type": msg_type}


def test_resync_after_garbage():
    frame = protocol.encode(protocol.WHEEL, steps=1)
    assert read(b"\x00DXD" + frame) == (protocol.WHEEL, b"\x01")


def test_bad_crc():
    frame = bytearray(protocol.encode(protocol.WHEEL, steps=1))
    frame[-1] ^= 0xFF
    with pytest.raises(ValueError, match="CRC"):
        read(bytes(frame))


def test_impossible_length():
    with pytest.raises(ValueError, match="longueur"):
        read(b"DT\x10\xff\xff\xff\x00")


def test_closed_connection():
    assert read(b"") is None
    assert read(protocol.encode(protocol.KEY, key=0, pressed=1)[:-2]) is None


def test_decode_errors():
    with pytest.raises(ValueError, match="inconnu"):
        protocol.decode(0x7F, b"")
    with pytest.raises(ValueError, match="KEY"):
        protocol.decode(protocol.KEY, b"\x01")


def draw(**fields):
    message = {"x": 0, "y": 0, "width": 960, "height": 540, "mode": 0, "pixels": bytes(259_200)}
    return {**message, **fields}


def test_check_draw():
    assert protocol.check_draw(draw(), 960, 540) is None
    assert protocol.check_draw(draw(x=2), 960, 540) == protocol.ERROR_ZONE
    assert protocol.check_draw(draw(x=1, width=2, pixels=bytes(540)), 960, 540) == protocol.ERROR_ZONE
    assert protocol.check_draw(draw(mode=2), 960, 540) == protocol.ERROR_SIZE
    assert protocol.check_draw(draw(pixels=b""), 960, 540) == protocol.ERROR_SIZE
