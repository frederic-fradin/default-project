"""Génère les images de canevas Fusion (une par vue de pièce), à l'échelle 10 px = 1 mm.

Chaque image porte une croix d'origine (à poser sur l'origine de Fusion) et un étalon
(deux croix à cliquer pour « Étalonner »). Le rendu PNG passe par Chrome sans interface.

Usage : python cad/canvas/generer_canvas.py
"""

import math
import subprocess
from pathlib import Path

DOSSIER = Path(__file__).parent
CHROME = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PX_MM = 10  # résolution : 10 px par mm

# Couleurs : fond clair, traits sombres, origine et étalon en rouge (lisibles dans Fusion).
FOND, TRAIT, CACHE, COTE, REPERE = "#ffffff", "#1b2a3a", "#6b7c8c", "#3d6f99", "#d0312d"
POLICE = "Consolas, 'IBM Plex Mono', monospace"

# Cotes partagées avec docs/design/coin-module-test.html (mm).
KX = [50.5 + i * 19.05 for i in range(4)]  # axes des switches
YC, XM = 21, 21  # axe des commandes, axe de la molette
NK = dict(x=40.825, y=10.25, l=76.5, w=21.5)  # carte NeoKey
NK_TROUS = [(NK["x"] + 19, NK["y"] + 3), (NK["x"] + 57.5, NK["y"] + 3),
            (NK["x"] + 19, NK["y"] + 18.5), (NK["x"] + 57.5, NK["y"] + 18.5)]
EN_TROUS = [(10.75, 10.75), (31.25, 10.75), (10.75, 31.25), (31.25, 31.25)]


class Vue:
    """Une image : repère en mm, axe vertical vers le haut, origine placée à (ox, oy) dans l'image."""

    def __init__(self, largeur, hauteur, ox, oy):
        self.w, self.h, self.ox, self.oy = largeur, hauteur, ox, oy
        self.el = []

    def X(self, x):
        return round(self.ox + x, 3)

    def Y(self, y):
        return round(self.oy - y, 3)

    def add(self, s):
        self.el.append(s)

    def trait(self, x1, y1, x2, y2, couleur=TRAIT, ep=0.25, tirets=None):
        d = f' stroke-dasharray="{tirets}"' if tirets else ""
        self.add(f'<line x1="{self.X(x1)}" y1="{self.Y(y1)}" x2="{self.X(x2)}" y2="{self.Y(y2)}" '
                 f'stroke="{couleur}" stroke-width="{ep}"{d}/>')

    def rect(self, x, y, l, h, couleur=TRAIT, ep=0.3, tirets=None, fond="none", r=0):
        d = f' stroke-dasharray="{tirets}"' if tirets else ""
        self.add(f'<rect x="{self.X(x)}" y="{self.Y(y + h)}" width="{l}" height="{h}" rx="{r}" '
                 f'fill="{fond}" stroke="{couleur}" stroke-width="{ep}"{d}/>')

    def cercle(self, x, y, d, couleur=TRAIT, ep=0.3, tirets=None, fond="none"):
        t = f' stroke-dasharray="{tirets}"' if tirets else ""
        self.add(f'<circle cx="{self.X(x)}" cy="{self.Y(y)}" r="{d / 2}" fill="{fond}" '
                 f'stroke="{couleur}" stroke-width="{ep}"{t}/>')

    def poly(self, pts, couleur=TRAIT, ep=0.35, fond="none"):
        p = " ".join(f"{self.X(x)},{self.Y(y)}" for x, y in pts)
        self.add(f'<polygon points="{p}" fill="{fond}" stroke="{couleur}" stroke-width="{ep}" stroke-linejoin="miter"/>')

    def texte(self, x, y, t, taille=2.6, couleur=COTE, ancre="middle", rot=0):
        tr = f' transform="rotate({rot} {self.X(x)} {self.Y(y)})"' if rot else ""
        self.add(f'<text x="{self.X(x)}" y="{self.Y(y)}" font-family="{POLICE}" font-size="{taille}" '
                 f'fill="{couleur}" text-anchor="{ancre}"{tr}>{t}</text>')

    def axe(self, x1, y1, x2, y2):
        self.trait(x1, y1, x2, y2, CACHE, 0.18, "3 0.8 0.6 0.8")

    def cote_h(self, x1, x2, y, t):
        self.trait(x1, y, x2, y, COTE, 0.18)
        for x in (x1, x2):
            self.trait(x, y - 1.2, x, y + 1.2, COTE, 0.18)
        self.texte((x1 + x2) / 2, y + 0.8, t)

    def cote_v(self, x, y1, y2, t):
        self.trait(x, y1, x, y2, COTE, 0.18)
        for y in (y1, y2):
            self.trait(x - 1.2, y, x + 1.2, y, COTE, 0.18)
        self.texte(x - 0.8, (y1 + y2) / 2, t, rot=-90)

    def croix(self, x, y, taille=4):
        self.trait(x - taille, y, x + taille, y, REPERE, 0.25)
        self.trait(x, y - taille, x, y + taille, REPERE, 0.25)
        self.cercle(x, y, taille, REPERE, 0.2)

    def origine(self, etiquette="ORIGINE 0,0", taille=4, dx=2.6, dy=-4.6):
        self.croix(0, 0, taille)
        self.texte(dx, dy, etiquette, 2.6, REPERE, "start")

    def etalon(self, x, y, longueur, texte="cliquer le centre des deux croix"):
        self.trait(x, y, x + longueur, y, REPERE, 0.3)
        self.croix(x, y, 2.5)
        self.croix(x + longueur, y, 2.5)
        self.texte(x + longueur / 2, y + 1.6, f"ÉTALON {longueur} mm" + (f" : {texte}" if texte else ""), 2.4, REPERE)

    def svg(self):
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{self.w * PX_MM}" height="{self.h * PX_MM}" '
                f'viewBox="0 0 {self.w} {self.h}"><rect width="{self.w}" height="{self.h}" fill="{FOND}"/>'
                + "".join(self.el) + "</svg>")


def cartouche(v, lignes):
    """Texte en bas à gauche de l'image."""
    for i, t in enumerate(lignes):
        y_img = v.h - 4 - 3.6 * (len(lignes) - 1 - i)
        v.add(f'<text x="4" y="{y_img}" font-family="{POLICE}" font-size="{3 if i == 0 else 2.4}" '
              f'fill="{TRAIT if i == 0 else COTE}">{t}</text>')


def coin_facade():
    """Coin de module, vue de dessus de la façade (plan XY), origine au coin bas gauche."""
    v = Vue(160, 100, 18, 62)
    R, e = 7, 2.5
    # Contour extérieur : bords gauche, bas, droit ; le haut est le bord de coupe.
    v.add(f'<path d="M{v.X(0)} {v.Y(40)} V{v.Y(R)} A{R} {R} 0 0 0 {v.X(R)} {v.Y(0)} H{v.X(125 - R)} '
          f'A{R} {R} 0 0 0 {v.X(125)} {v.Y(R)} V{v.Y(40)}" fill="none" stroke="{TRAIT}" stroke-width="0.35"/>')
    v.trait(0, 40, 125, 40, CACHE, 0.25, "2 1")
    # Parois intérieures (cachées sous la façade).
    ri = R - e
    v.add(f'<path d="M{v.X(e)} {v.Y(40)} V{v.Y(e + ri)} A{ri} {ri} 0 0 0 {v.X(e + ri)} {v.Y(e)} H{v.X(125 - e - ri)} '
          f'A{ri} {ri} 0 0 0 {v.X(125 - e)} {v.Y(e + ri)} V{v.Y(40)}" fill="none" stroke="{CACHE}" '
          f'stroke-width="0.2" stroke-dasharray="1 0.6"/>')
    # Cartes cachées.
    v.rect(NK["x"], NK["y"], NK["l"], NK["w"], CACHE, 0.2, "1 0.6")
    v.rect(8.25, 8.25, 25.5, 25.5, CACHE, 0.2, "1 0.6")
    # Plots et avant-trous (cachés).
    for x, y in NK_TROUS + EN_TROUS:
        v.cercle(x, y, 3.6, CACHE, 0.2, "1 0.6")
        v.cercle(x, y, 1.6, CACHE, 0.2, "0.6 0.4")
    # Fenêtres et trou de bague (traversants).
    for cx in KX:
        v.rect(cx - 6.5, YC - 6.5, 13, 13, TRAIT, 0.35)
        v.axe(cx, YC - 9, cx, YC + 9)
    v.cercle(XM, YC, 7.4, TRAIT, 0.35)
    v.axe(-4, YC, 129, YC)
    v.axe(XM, YC - 9, XM, YC + 9)
    # Cotes.
    for a, b, t in [(0, 21, "21"), (21, 50.5, "29,5"), (50.5, 69.55, "19,05"), (69.55, 88.6, "19,05"),
                    (88.6, 107.65, "19,05"), (107.65, 125, "17,35")]:
        v.cote_h(a, b, 45, t)
    v.cote_v(-8, 0, YC, "21")
    v.cote_v(133, 0, 40, "40")
    v.cote_h(KX[0] - 6.5, KX[0] + 6.5, YC + 8.5, "13")
    v.texte(XM, YC - 7, "Ø 7,4", 2.4)
    v.texte(NK["x"], NK["y"] - 2.6, "carte NeoKey (cachée) · plots Ø 3,6 · avant-trous Ø 1,6", 2, CACHE, "start")
    v.texte(10, 26.5, "carte encodeur", 2, CACHE, "start")
    v.origine()
    v.etalon(0, -12, 100)
    cartouche(v, ["COIN-MODULE · FAÇADE · plan XY, vue de dessus",
                  "traits pleins : façade · tirets : caché derrière la façade · 10 px = 1 mm"])
    return v


def coin_coupe():
    """Coin de module, coupe A-A dans l'axe des commandes (plan XZ), origine au coin bas gauche du dos."""
    v = Vue(160, 80, 18, 50)
    hach = '<pattern id="h" width="1.2" height="1.2" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">' \
           f'<line x1="0" y1="0" x2="0" y2="1.2" stroke="{CACHE}" stroke-width="0.15"/></pattern>'
    v.add(f"<defs>{hach}</defs>")
    piece = [
        [(0, 0), (0, 26), (17.3, 26), (17.3, 23.5), (2.5, 23.5), (2.5, 0)],
        [(114.15, 26), (125, 26), (125, 0), (122.5, 0), (122.5, 23.5), (114.15, 23.5)],
    ] + [[(a, 23.5), (a, 26), (b, 26), (b, 23.5)] for a, b in [(24.7, 44), (57, 63.05), (76.05, 82.1), (95.1, 101.15)]]
    for p in piece:
        v.poly(p, TRAIT, 0.35, "url(#h)")
    # Plots (hors du plan de coupe).
    for x in (NK["x"] + 19, NK["x"] + 57.5):
        v.rect(x - 1.8, 15, 3.6, 8.5, CACHE, 0.2, "1 0.6")
    for x in (10.75, 31.25):
        v.rect(x - 1.8, 12, 3.6, 11.5, CACHE, 0.2, "1 0.6")
    # Composants de référence, en gris.
    v.rect(NK["x"], 13.4, NK["l"], 1.6, CACHE, 0.2)
    for cx in KX:
        v.poly([(cx - 7, 15), (cx + 7, 15), (cx + 5.05, 26.5), (cx - 5.05, 26.5)], CACHE, 0.2)
        v.rect(cx - 3.25, 26.5, 6.5, 4, CACHE, 0.2)
        v.rect(cx - 9, 30.5, 18, 3, CACHE, 0.2, "1 0.6")
    v.rect(8.25, 10.4, 25.5, 1.6, CACHE, 0.2)
    v.rect(15, 12, 12, 7, CACHE, 0.2)
    v.rect(17.5, 19, 7, 7, CACHE, 0.2)
    v.rect(18, 26, 6, 8, CACHE, 0.2)
    v.rect(8.5, 27, 25, 9, CACHE, 0.2, "1 0.6")
    v.axe(XM, 8, XM, 38)
    # Cotes.
    v.cote_v(133, 0, 26, "26")
    v.cote_v(-8, 23.5, 26, "2,5")
    v.cote_v(5.4, 12, 26, "14")
    v.cote_v(37.2, 15, 26, "11")
    v.cote_v(140, 26, 33.5, "7,5")
    v.texte(62.5, 37, "pièce hachurée · composants en gris · capuchons et bouton en tirets", 2.2, CACHE)
    v.origine("ORIGINE 0,0 (dos)", dx=-17, dy=-7)
    v.etalon(0, -10, 100)
    cartouche(v, ["COIN-MODULE · COUPE A-A · plan XZ (y = 21), vue de face",
                  "z vers le haut, dos à z = 0, façade à z = 26 · 10 px = 1 mm"])
    return v


def bouton_dessus():
    """Bouton de molette, vue de dessus (plan XY), origine au centre ; jeu 0,2."""
    v = Vue(70, 64, 35, 30)
    v.cercle(0, 0, 25, TRAIT, 0.35)
    v.cercle(0, 0, 23, CACHE, 0.15)
    v.rect(-0.4, 5, 0.8, 5, TRAIT, 0.25)
    # Alésage en D (sous le bouton) : Ø 6,2 coupé par le méplat à x = 1,6.
    r, f = 3.1, 1.6
    hc = math.sqrt(r * r - f * f)
    v.add(f'<path d="M{v.X(f)} {v.Y(hc)} A{r} {r} 0 1 0 {v.X(f)} {v.Y(-hc)} Z" fill="none" stroke="{CACHE}" '
          f'stroke-width="0.25" stroke-dasharray="0.8 0.5"/>')
    # Points de variante (sous le bouton) : positions pour 3 points ; 1 point = centre, 2 points = ± 1,25.
    for y in (-2.5, 0, 2.5):
        v.cercle(-9, y, 1, CACHE, 0.15, "0.4 0.3")
    v.axe(-15, 0, 15, 0)
    v.axe(0, -15, 0, 15)
    v.cote_h(-12.5, 12.5, -15.5, "Ø 25")
    v.texte(0, 13.8, "repère 0,8 × 5", 2, COTE)
    v.texte(5.5, -5.5, "D : Ø 6,2 · méplat 4,7", 2, CACHE, "start")
    v.texte(-9, -5, "points", 2, CACHE)
    v.origine("0,0", 1.5, 1.4, 1.2)
    v.etalon(-10, -21, 20, "")
    cartouche(v, ["BOUTON · DESSUS · plan XY", "tirets : sous le bouton · jeu 0,2 · 10 px = 1 mm"])
    return v


def bouton_coupe():
    """Bouton de molette, coupe dans l'axe (plan XZ), origine au centre du dessous ; jeu 0,2."""
    v = Vue(70, 48, 35, 24)
    hach = '<pattern id="h" width="1" height="1" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">' \
           f'<line x1="0" y1="0" x2="0" y2="1" stroke="{CACHE}" stroke-width="0.12"/></pattern>'
    v.add(f"<defs>{hach}</defs>")
    pts = [(-12.5, 0), (-12.5, 8)]
    pts += [(-12.5 + 1 - math.cos(a) * 1, 8 + math.sin(a) * 1) for a in [i * math.pi / 12 for i in range(1, 6)]]
    pts += [(-11.5, 9), (5, 9), (5, 8.4), (10, 8.4), (10, 9), (11.5, 9)]
    pts += [(12.5 - 1 + math.sin(a) * 1, 8 + math.cos(a) * 1) for a in [i * math.pi / 12 for i in range(1, 6)]]
    pts += [(12.5, 8), (12.5, 0), (1.6, 0), (1.6, 7), (-3.1, 7), (-3.1, 0)]
    v.poly(pts, TRAIT, 0.3, "url(#h)")
    v.axe(0, -2, 0, 11)
    v.cote_v(16, 0, 9, "9")
    v.cote_v(-16, 0, 7, "7")
    v.cote_h(-3.1, 1.6, 11, "4,7")
    v.texte(0, 15, "alésage en D Ø 6,2 sur 7 · repère creux 0,6", 2, COTE)
    v.origine("0,0", 1.5, 2, -3.2)
    v.etalon(-10, -9, 20, "")
    cartouche(v, ["BOUTON · COUPE · plan XZ", "dessous à z = 0 · jeu 0,2 · 10 px = 1 mm"])
    return v


def rendre(nom, vue):
    svg = DOSSIER / f"{nom}.svg"
    svg.write_text(vue.svg(), encoding="utf-8")
    png = DOSSIER / f"{nom}.png"
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars", "--force-device-scale-factor=1",
                    f"--window-size={vue.w * PX_MM},{vue.h * PX_MM}", f"--screenshot={png}", svg.as_uri()],
                   check=True, capture_output=True)
    print(png.name, f"{vue.w * PX_MM} × {vue.h * PX_MM} px")


if __name__ == "__main__":
    rendre("coin-module_facade_XY", coin_facade())
    rendre("coin-module_coupe_XZ", coin_coupe())
    rendre("bouton_dessus_XY", bouton_dessus())
    rendre("bouton_coupe_XZ", bouton_coupe())
