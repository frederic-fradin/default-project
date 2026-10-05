"""Dessin des pages de l'écran (960 × 540, paysage). Chaque fonction renvoie une image Pillow."""

from functools import lru_cache

from PIL import Image, ImageDraw, ImageFont

WIDTH, HEIGHT = 960, 540
WHITE, BLACK, GREY = 255, 0, 136

# Centre de chaque touche, en pixels de l'écran, pour placer les étiquettes juste au-dessus
# (ADR 004). Provisoire : estimé sur le module de 125 mm, à recaler sur la maquette.
KEY_X = (358, 535, 711, 887)
LABELS_Y = 470

KEY_NAMES = ("Touche 1", "Touche 2", "Touche 3", "Accueil", "Clic molette")

FONT_DIR = "C:/Windows/Fonts"


@lru_cache
def font(size, bold=False):
    return ImageFont.truetype(f"{FONT_DIR}/{'segoeuib' if bold else 'segoeui'}.ttf", size)


def key_labels(draw, labels):
    """Bande des étiquettes en bas de l'écran, chacune au-dessus de sa touche."""
    draw.line((24, LABELS_Y, WIDTH - 24, LABELS_Y), fill=GREY, width=2)
    for x, label in zip(KEY_X, labels):
        draw.text((x, (LABELS_Y + HEIGHT) // 2), label, font=font(26), fill=BLACK, anchor="mm")


def hello(state):
    """Page de test de la P1 : dernière touche appuyée, compteur de molette, LED de la touche 1."""
    page = Image.new("L", (WIDTH, HEIGHT), WHITE)
    draw = ImageDraw.Draw(page)
    draw.text((48, 40), "desktop-tool", font=font(64, bold=True), fill=BLACK)
    last_key = "aucune" if state["last_key"] is None else KEY_NAMES[state["last_key"]]
    lines = (
        f"Dernière touche : {last_key}",
        f"Molette : {state['wheel']:+d}",
        f"LED de la touche 1 : {'allumée' if state['led'] else 'éteinte'}",
    )
    for row, line in enumerate(lines):
        draw.text((48, 170 + row * 70), line, font=font(40), fill=BLACK)
    key_labels(draw, ("LED", "", "", "Accueil"))
    return page
