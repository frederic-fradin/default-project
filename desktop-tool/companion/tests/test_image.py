import pytest
from PIL import Image

from src import image


def test_pixel_order():
    picture = Image.new("L", (2, 1))
    picture.putpixel((1, 0), 255)
    assert image.to_4bpp(picture) == b"\xf0"


def test_round_trip():
    picture = Image.frombytes("L", (4, 2), bytes(level * 17 for level in (0, 1, 2, 3, 12, 13, 14, 15)))
    assert image.from_4bpp(image.to_4bpp(picture), 4, 2).tobytes() == picture.tobytes()


def test_full_page_size():
    assert len(image.to_4bpp(Image.new("L", (960, 540), 255))) == 259_200


def test_odd_width():
    with pytest.raises(ValueError, match="impaire"):
        image.to_4bpp(Image.new("L", (3, 1)))
