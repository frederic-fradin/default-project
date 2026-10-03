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

**Budget (même jour)**
- Dépenses réelles relevées sur les factures : Amazon **92,16 €**, DigiKey **57,48 €** (port 30 € TTC
  compris), filament en stock → **149,64 €** pour un plafond de 150 €, reste **0,36 €**.
- Écarts : port DigiKey non prévu et carte plus chère que l'estimation (59 €) ; compensés par le
  filament déjà en stock.
- Un seul câble STEMMA QT ↔ broches mâles (4209) commandé, pas de rechange.
- Détail dans `hardware/bom.md` (section « Dépenses réelles ») et cadrage §4.5 (v1.5).
- ⚠️ Tout nouvel achat (filament, pièce de rechange) fera dépasser le plafond.

**Maquette : touches et station de bureau (même jour)**
- Maquette mise à jour avec l'ADR 004 : symboles **gravés en creux, sans couleur**, plus petits
  (barres 0,8 × 5 mm, écart 1,5 mm ; maison 5 mm) ; colonne d'étiquettes à gauche de l'écran,
  alignée sur les touches.
- Pupitre triangle jugé **trop massif**. Trois pistes allégées dessinées : béquille, ailettes,
  plateau.
- **Décision (ADR 005)** : **station modulaire** — socle 220 × 98 × 10 (rainure à stylo de
  180 mm, grille de 22 accroches au pas de 20 mm) + éléments clipsés : pupitre du module et
  pupitre MagSafe (iPhone Pro en portrait, palet déjà possédé). Cadrage passé en v1.6.
- USB-C du module déplacé **au dos**, branché par un connecteur magnétique noyé dans la lame.
- ⚠️ Connecteur USB-C magnétique + rallonge sur panneau : ≈ 10 à 15 € hors budget.

**Suite**
- Pièce test des tenons clipsables (morceau de grille + 2 tenons) pour régler le jeu.
- À réception de la carte T5 : position réelle du port USB-C, cheminement de la rallonge.

**Référence visuelle (même jour)**
- Ajout de `images/desktop-9.jpg` : **image préférée pour les couleurs et les symboles des
  touches** — corps gris chaud mat, touches gris clair aux symboles fins et discrets, un seul
  bouton d'accent orange.

**Couleurs (même jour)**
- Style **C « gris chaud + orange »** ajouté d'après l'image desktop-9 : module Ash Grey, touches
  Muted White, molette Sunrise Orange. Trois styles en balance (A, B, C).
- **Station de la couleur du corps du module** (remplace le « pupitre Fossil Grey »).
- Maquette : planches de couleur redessinées sur la station modulaire ; pupitre triangle et
  pupitres allégés archivés dans « Études précédentes ». Cadrage passé en v1.7.

**Module en paysage et station affinée (même jour)**
- Impression test à l'échelle du module : en main, la molette tombait trop haut pour le pouce.
- **Décision (ADR 006)** : module tourné de 90° vers la gauche → **125 × 115 × 26**, écran en
  paysage en haut, molette en bas à gauche (sous le pouce gauche), 4 touches en ligne en bas à
  droite, étiquettes des touches en bas de l'écran. Risque R16 (portrait) levé.
- Station (ADR 005 révisée) : rainure à stylo retirée ; socle **250 × 90 × 10** percé de
  **48 trous ronds** (12 colonnes × 4 rangées, maximum posé droit sur l'A1) ; 4 tenons ronds par
  élément ; assises en pente douce ; support du téléphone **sans rebord devant** ; iPhone 13 Pro
  avec coque (74 × 149 × 12) ; lame MagSafe réduite à 62 mm.
- Support AirPods Pro 3 essayé puis écarté : **2 colonnes libres** à droite, usage à définir
  (boîte à crayons…).
- Cadrage passé en v1.8.

**Suite**
- Pièce test : molette et barre de touches dans un coin de module en paysage (accès au pouce).
- Pièce test des tenons ronds fendus (jeu ≈ 0,2 mm, ergot ≈ 0,4 mm).

## 2026-10-02 — Réception des composants (P1)

- Reçus : NeoKey 1x4 QT, 10 switches Kailh Tactile Brown, molette Adafruit 5880, câbles
  STEMMA QT (JST SH 4 broches) ↔ QT et ↔ broches mâles, câble USB-C data, vis, aimants, patins.
- Reste à recevoir : carte LilyGO T5 4,7" (prévue mi-octobre).

**Suite**
- Mesurer un vrai switch (croix de la tige, hauteur) puis dessiner le capuchon de touche test.
- Mesurer la NeoKey (empreinte, hauteur avec switches) et la molette (axe, hauteur, bouton)
  pour la pièce test « coin de module en paysage ».
- ✅ Vérifier que les aimants 6 × 2 mm entrent dans un logement imprimé (jeu à régler) → fait le 2026-10-03.

## 2026-10-03 — Logements d'aimant (P1)

**Test** (plaquette test, trous Ø 6,1 / 6,2 / 6,3 × 2,2 mm sous le carreau gris)
- Ø 6,1 mm : l'aimant ne rentre pas.
- **Ø 6,2 mm** : l'aimant tient parfaitement.
- Ø 6,3 mm : il entre un peu plus facilement.

**Décision**
- Logement d'aimant retenu : **Ø 6,2 × 2,2 mm** pour les aimants 6 × 2 mm N52 (jeu de 0,1 mm
  au rayon). À créer comme paramètre utilisateur Fusion (`d_aimant = 6,2 mm`, `p_aimant = 2,2 mm`)
  dans les pièces du module et de la station.
- Ø 6,3 mm en secours, avec un point de colle, si une autre bobine ou un autre réglage
  d'impression resserre les trous.
- Enseignement : les trous imprimés sortent **≈ 0,1 à 0,2 mm plus petits** que la cote. Pour un
  ajustement serré, prévoir au moins **+0,2 mm au diamètre** ; à confirmer sur les tenons ronds et
  la croix des touches.

**Mesures d'un switch Kailh BOX Brown** (enfiché sur la NeoKey, au repos)
- Croix de la tige : branches 4,0 × ≈ 1,2 mm, profondeur 3,6 mm sous le haut du carré.
- Carré (box) autour de la croix : intérieur 6,0 mm (angles légèrement arrondis), extérieur 6,5 mm ;
  dépasse de 4,0 mm du boîtier au repos, affleure le boîtier touche enfoncée.
- Boîtier : face plate du dessus 10,1 × 10,0 mm, base 14,0 × 15,5 mm.
- Hauteurs au-dessus de la carte NeoKey : dessus du boîtier 11,5 mm, haut du carré 15,5 mm.
- Entraxe des switches : 19,0 mm.

**Impression du capuchon de touche test (même jour)**
- Profil retenu : **0.20mm Standard @BBL A1**. La face visible est contre le plateau et la
  croix est un ajustement en XY, donc une couche plus fine n'apporte rien ici. La première
  couche fait 0,20 mm : la gravure de 0,6 mm fait 3 couches et le plateau de 3 mm 15 couches.
- Orientation : face gravée sur le plateau (« Poser sur une face » dans Bambu Studio), pied et
  croix vers le haut, sans support.
- Les 3 variantes de croix (jeu 0,2 / 0,3 / 0,4 mm) sont imprimées ensemble avec les mêmes
  réglages, sans compensation de trous en XY.
- À surveiller : les barres de 0,8 mm sont dans la première couche et peuvent se refermer en
  partie (patte d'éléphant). Si c'est le cas, élargir les barres à 1,0 mm.
- Plaque : plaque par défaut de l'A1 (PEI texturée).

**Résultat du premier capuchon (même jour)**
- Variante **jeu 0,2 mm** (croix 4,2 × 1,4 mm) : le capuchon s'enclenche bien sur le switch.
- Vérifications : il tient retourné et résiste légèrement à la traction ; il ne bouge pas et ne
  bascule pas quand on appuie sur un coin ; aucun frottement sur toute la course.

**Décision**
- Jeu de croix retenu : **`jeu_croix = 0,2 mm`** (croix 4,2 × 1,4 mm). Les variantes 0,3 et
  0,4 mm ne sont pas imprimées.
- Enseignement : pour un emmanchement serré de petites pièces imprimées, prévoir **+0,2 mm** sur
  la cote mesurée. C'est cohérent avec les logements d'aimant ; à vérifier sur les tenons ronds.
- Face gravée : les barres de 0,8 mm sortent **nettes**, la première couche ne les referme pas.
  Largeur 0,8 mm conservée.
- Finition : le grain mat de la plaque PEI texturée plaît sur le dessus de la touche. **Plaque
  texturée retenue** pour les faces visibles imprimées côté plateau.
- Capuchon de touche test **validé** (profil 0.20mm Standard, jeu de croix 0,2 mm, gravure
  0,8 × 0,6 mm, plaque texturée).

**Jeu de 4 touches (même jour)**
- Modélisation : un seul fichier, capuchon de base copié en **réseau rectangulaire de corps**
  (4 corps, espacement `pas_touche` = 19 mm, placé dans la timeline avant les gravures), puis une
  gravure par corps : 1, 2, 3 barres et maison.
- Impression : 4 touches avec les réglages validés (0.20mm Standard, plaque texturée, face
  gravée sur le plateau). **Résultat : tout est OK**, les 4 touches sont prêtes pour la NeoKey.

## 2026-10-03 — Fixation des éléments de la station (P1)

**Problème**
- Les 4 tenons intégrés sous la semelle (ADR 005) pendaient sous l'élément : aucune face ne
  permettait d'imprimer un pupitre sans support. Imprimés debout, les bras fendus pliaient
  entre deux couches et risquaient de casser à la base.

**Décision** (option B parmi A : tenons avec supports, B : chevilles séparées, C : picots sur le socle)
- **Chevilles séparées**, imprimées couchées : tige Ø 9,6 fendue (fente 2 × 7) avec ergot au
  bout, tête Ø 13 × 1 dans un lamage Ø 13,4 × 1,2 de la semelle ; trou du socle Ø 10 × 6 avec
  gorge Ø 10,8 × 2 au fond pour le clic. ADR 005 révisée, cadrage v1.9.
- Planche cotée de la pièce test : `docs/design/tenons-test.html` (bout de socle à 3 trous,
  bout de semelle à 2 trous, 3 variantes d'ergot 0,2 / 0,3 / 0,4 mm, 2 chevilles par variante).

**Suite**
- Modéliser et imprimer la pièce test, puis noter clic, tenue, retrait, jeu dans l'axe des
  méplats et tenue après 10 cycles.
