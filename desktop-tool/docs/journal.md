# Journal de bord — desktop-tool

Une entrée par session : ce qui a été fait, ce qui a coincé, la suite. Ajouter des photos dans
`docs/journal/` au fil de l'eau.

---

## 2026-09-26 — Cadrage (P0)

**Fait**
- Cadrage complet, validé en v1.0 (`docs/cadrage.md`).
- Décisions : architecture objet + application compagnon (001), Fusion (002), variante 1 en
  module + pupitre, avec batterie et sans-fil anticipés (003).
- Maquettes blueprint du module et du pupitre (`docs/design/maquettes.html`).
- Carte LilyGO T5 4,7" V2.3 ESP32-S3 « Welded » commandée, livraison mi-octobre.

- Modules commandés chez DigiKey (NeoKey 1x4, molette Adafruit 5880, switches Kailh Brown,
  câbles STEMMA QT), livraison ≈ 3 jours. Opencircuit, Botland et BerryBase étaient en rupture
  sur le NeoKey.

**Points ouverts**
- ✅ Commande Amazon passée : câble USB-C data, aimants 6 × 2 mm N52, vis, patins. PLA en stock.
  **Tout le matériel v1 est commandé.**
- À réception de la carte : vérifier le connecteur batterie et l'accès I²C (SDA 18 / SCL 17).
- Conception : les connecteurs STEMMA QT du NeoKey sont sous la carte, aux deux bouts.
- À tester en P1 : stabilité du pupitre (incrustation 100 %), affichage portrait, jeu de l'empreinte.

**Couleurs (provisoires)** : module et touches Muted White, molette et libellés Sunrise Orange,
pupitre Fossil Grey. À confirmer avec une plaquette test.

**Suite (P1)**
- Installer Fusion (licence Personal Use) et suivre un premier tutoriel.
- Premières pièces test à imprimer : plaquette couleurs (Muted White / Fossil Grey / Sunrise Orange),
  logements d'aimant 6 × 2 mm (jeux 6,1 / 6,2 / 6,3 mm), jeu d'une empreinte.

---

## 2026-09-27 — Fusion, première pièce (P1)

**Fait**
- Fusion installé (licence Personal Use).
- Plaquette test modélisée pas à pas (`cad/plaquette-test`) : 105 × 30 × 4 mm, paramètres utilisateur
  (`cote`, `largeur`, `epaisseur`), 3 carreaux en corps séparés (Blanc / Gris / Orange), « DESK » en
  relief 0,6 mm (Arial Black, 6 mm) en 4e corps, 3 trous d'aimant sous le carreau gris
  (Ø 6,1 / 6,2 / 6,3 × 2,2 mm).
- Appris : esquisse contrainte (tout en noir), cotes par paramètres, extrusion en « Nouveau corps »,
  texte d'esquisse, extrusion en mode « Couper ».

**Décision**
- Touches : **icônes plutôt que texte** (ex. maison = Accueil). Un libellé fige la touche à une
  fonctionnalité, alors que l'usage final n'est pas arrêté. Cadrage passé en v1.2.

**Suite**
- Exporter en `.f3d` + `.3mf` dans `cad/`, imprimer, noter couleurs / netteté du relief / trou d'aimant retenu.
- Prochaine pièce test : touche sur switch Kailh, avec une icône en relief.

**Tests d'impression (même jour)**
- Couleurs : hésitation entre deux styles — **A** module Charcoal Black + molette Army Red,
  **B** module Muted White + molette Sunrise Orange.
- Relief positif sur les touches : pas convaincant → essai d'icônes **gravées en creux**
  (même principe que les logements d'aimant).
- Constat : une touche imprimée **face visible contre le plateau** a un bien meilleur rendu.
- Idée de symboles : +, −, entrée, retour (à arbitrer, recoupe les fonctions de la molette).
- **Décision (ADR 004)** : touches à symboles neutres + maison ; la fonction de chaque touche est
  affichée à l'écran, en face d'elle. Cadrage passé en v1.4.
- Symboles des touches 1 à 3 : **1, 2 et 3 barres** gravées en creux.
