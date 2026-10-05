"""Conversion entre images Pillow et pixels 4 bits de l'écran (ADR 007).

16 niveaux de gris, 0 = noir, 15 = blanc ; 2 pixels par octet, le pixel pair dans les 4 bits
de poids faible (convention epdiy, à vérifier sur la carte).
"""

from PIL import Image


def to_4bpp(picture):
    gray = picture.convert("L")
    if gray.width % 2:
        raise ValueError(f"largeur impaire : {gray.width}")
    levels = gray.point(lambda value: value >> 4).tobytes()
    return bytes(even | (odd << 4) for even, odd in zip(levels[0::2], levels[1::2]))


def from_4bpp(pixels, width, height):
    levels = bytearray(width * height)
    levels[0::2] = bytes((byte & 0x0F) * 17 for byte in pixels)
    levels[1::2] = bytes((byte >> 4) * 17 for byte in pixels)
    return Image.frombytes("L", (width, height), bytes(levels))
