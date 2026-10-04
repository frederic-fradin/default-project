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

**Mise en attente (même jour)**
- Pas encore certain de garder le principe du socle à éléments clipsés pour le pupitre du
  module : **pièce test des chevilles en attente**, rien n'est modélisé ni imprimé. La planche
  `tenons-test.html` et la révision de l'ADR 005 restent valables si le principe est conservé.

## 2026-10-03 — Mesures pour la pièce test « coin de module » (P1)

**NeoKey 1x4** (carte vue de dessus, switches vers soi)
- Carte : 76,5 × 21,5 × 1,6 mm ; composants dessous jusqu'à 3 mm (connecteurs STEMMA QT aux deux
  bouts, fiche vers l'extérieur, dans l'axe de la longueur).
- Centre du switch 1 : 10 mm du bord gauche, 10 mm du bord bas ; pas de 19,05 mm.
- 4 trous Ø 2, entre les switches 1-2 et 3-4 : **centres à 19 mm des bouts et 3 mm des grands
  côtés** (remesuré au centre). À confirmer avec un gabarit imprimé avant la pièce complète.

**Molette Adafruit 5880**
- Carte : 25,5 × 25,5 × 1,6 mm (1 pouce chez Adafruit, 25,4).
- 4 trous Ø 2 dans les coins, centres à 2,5 mm des deux bords (0,1 pouce, 2,54).
- Axe au centre de la carte.
- Corps de l'encodeur : 12 × 12 × 7 mm au-dessus de la carte.
- Bague filetée Ø 7 (M7 probable), 7 mm au-dessus du corps (haut à 14 mm de la carte), écrou de
  2 mm d'épaisseur fourni.
- Axe Ø 6 en D, bout à 22 mm au-dessus de la carte (8 mm au-dessus de la bague) ; « 4 mm sur la
  partie plate » : longueur du méplat ou épaisseur sur le méplat, à préciser.
- Clic : l'axe s'enfonce de 0,5 mm.
- Dessous : composants jusqu'à 3 mm, 2 connecteurs QT sur deux bords opposés, fiche vers
  l'extérieur.
- Axe : épaisseur sur le méplat **4,5 mm**, méplat **7 mm** de long depuis le bout : l'alésage du
  bouton est en D sur toute sa profondeur.
- NeoKey : centre du switch 1 à 10,75 mm du bord haut, les switches sont centrés dans la largeur
  de la carte.

**Choix de conception (même jour)**
- Dessus de la façade à **11 mm au-dessus de la carte NeoKey**, une fenêtre 13 × 13 par switch :
  les touches dépassent de 7,5 mm au repos.
- Encodeur vissé sur 4 plots, carte à **14 mm sous le dessus de la façade** : la bague filetée
  affleure, l'écrou n'est pas utilisé, l'axe dépasse de 8 mm, bouton de molette ≈ 9 mm.
- Planche cotée : `docs/design/coin-module-test.html`.

**Bouton de molette (même jour)**
- Modélisé dans Fusion (alésage en D sur toute la profondeur, 3 variantes de jeu repérées par
  1, 2 ou 3 points gravés sous le bouton) ; **impression en cours**.

**Coin de module (même jour)**
- Modélisation commencée puis arrêtée aux plots NeoKey ; **reprise de zéro le 2026-10-04**, en
  suivant `docs/design/coin-module-test.html` et les canevas de `cad/canvas/`.
- Points expliqués en séance : origine du design (au coin bas gauche, dans le vide à cause du
  congé), cotes depuis l'origine ou les bords, vue de dessous en miroir pour les plots.
- Bouton de molette, variante **jeu 0,2** (alésage Ø 6,2, méplat 4,7) : **tient bien sur l'axe**.
  Cohérent avec la croix des touches : la règle des +0,2 sur la cote mesurée se confirme.
- Vérifications : aucun jeu en rotation, retrait facile à la main, clic de l'encodeur bien
  transmis.

**Décision**
- Jeu d'alésage du bouton retenu : **`jeu_axe = 0,2 mm`**. Les variantes 0,1 et 0,3 sont
  abandonnées. Bouton de molette **validé**.
- Règle confirmée sur 3 pièces (logements d'aimant, croix des touches, axe de l'encodeur) :
  **+0,2 mm sur la cote mesurée** pour un emmanchement serré.
- Coin de module remodélisé de zéro : **impression en cours** (façade contre le plateau).

## 2026-10-04 — Montage des cartes dans le coin de module (P1)

**Test** (coin de module imprimé, NeoKey + 4 touches et encodeur + bouton jeu 0,2 vissés)
- Alignement : switches centrés dans leurs fenêtres, axe de l'encodeur centré dans son trou.
- Fenêtres : aucun frottement des switches ni des capuchons.
- Hauteur des touches (7,5 mm au-dessus de la façade) : **parfaite**. Emplacement des touches
  et de la molette sous le pouce gauche : **parfait**.
- Bague filetée : ne touche pas la façade.
- **Plots** : les vis M2 font éclater le plastique autour de l'avant-trou (plot Ø 3,6, avant-trou
  Ø 1,6, soit 1 mm de paroi).
- **Trous NeoKey côté écran** : 2 vis sur 4 seulement ; les 2 plots côté écran sont trop bas,
  il faut les rapprocher de l'écran de 1 mm. Les 2 plots côté bord arrondi sont justes.
- **Bouton de molette** : frotte la façade quand on l'enfonce, le clic ne se fait pas. Il faut
  plus d'espace sous le bouton.
- Câbles QT : juste, mais ça passe. Les connecteurs des deux cartes se font face : piste,
  tourner la carte de l'encodeur de 90° pour brancher côté écran.

**Décisions (même jour)**
- Trous NeoKey : `trou_nk_y` remplacé par `trou_nk_y_bas` = 3 (côté arrondis, inchangé) et
  `trou_nk_y_haut` = 2 (côté écran) : les trous de la carte ne sont pas symétriques.
- Plots : avant-trou **1,6 → 1,8**, plot **3,6 → 4,2** à confirmer, 4 boucles de paroi dans
  Bambu Studio. Avant de réimprimer le coin : **plaquette de 3 plots** (Ø 3,6 / 4,2 / 5,
  avant-trou 1,8), vissés à travers la carte de l'encodeur ; on garde le plus petit diamètre
  qui ne casse pas.
- Bouton de molette version 2 : `p_alesage` **7 → 6** et `h_bouton` **9 → 8** : 2 mm sous le
  bouton au lieu de 1, dessus toujours à 10 mm de la façade. Coin de module inchangé côté
  encodeur.
- Carte de l'encodeur tournée de 90° (connecteur côté écran) : trous symétriques, rien ne
  change dans la CAO.
- Planche `coin-module-test.html` et canevas mis à jour.
- Suite : imprimer la plaquette de plots et le bouton v2, puis réimprimer le coin de module.
- CAO mise à jour : coin de module (trous NeoKey, plots, avant-trous), bouton v2, plaquette de
  plots modélisée. **Plaquette de plots en impression.**

**Plaquette de plots (même jour)** (avant-trou 1,8, 4 boucles de paroi, vis M2 × 6 à travers la
  carte de l'encodeur)
- Ø 3,6 (1 point) : vissé, dévissé, revissé, **tient**.
- Ø 4,2 (2 points) : vissé, puis **cassé à mi-hauteur** (rupture entre deux couches, pas
  d'éclatement autour de l'avant-trou) : excès de couple probable, pas un problème de diamètre.
- Ø 5 (3 points) : vissé, dévissé, revissé, rien n'a bougé.
- **Décision** : `d_plot` reste à **3,6** (le plus petit qui tient ; 5 ne passe pas entre les
  switches) avec `d_pilote` = **1,8**. La casse venait de l'avant-trou de 1,6. Au montage,
  serrer jusqu'au contact de la carte, sans forcer.
- Coin de module version 2 (trous NeoKey côté écran à 2 mm, plots Ø 3,6, avant-trous 1,8,
  4 boucles de paroi) : **impression en cours**.

## 2026-10-04 — Planche de la maquette d'encombrement (P1)

- Cotes de la carte T5 relevées sur le plan officiel LilyGO (`shell/EPD47-S3.dxf` du dépôt
  LilyGo-EPD47, branche esp32s3), sur la fiche de l'écran ED047TC1 et sur le schéma V2.3.
  Provisoires jusqu'à la réception de la carte.
- Constats : carte de 118,07 × 63,07 pour 120 mm entre les parois (moins de 1 mm de jeu par
  côté) ; zone active décalée côté nappe (bords de fenêtre ≈ 13 et 7,5) ; **USB-C sur le petit
  côté, pas au dos** ; aucun trou de fixation (pattes à prévoir) ; tous les composants au dos.
- Point dur : le câble 4209 sur le connecteur femelle 2×20 dépasserait de ≈ 6 mm sous le dos.
  Piste : prise P5 (PH 2,0 : 3,3 V, IO15, IO16, GND) avec un câble PH 2,0 ↔ STEMMA QT.
- Planche : `docs/design/maquette-encombrement.html`. À trancher : sens de la carte, branchement
  I²C, hauteur de l'écran.
- **Choix** : carte T5 USB-C à droite (connecteur 2×20 en bas) ; écran haut, `y_t5` = 44.
  Branchement I²C : **en attente des mesures** (boîtier des broches du câble 4209 maintenant,
  hauteur du connecteur 2×20 à réception).

## 2026-10-04 — Coin de module v2 monté : VALIDÉ (P1)

- 8 vis M2 serrées sans fissure (plots Ø 3,6, avant-trous 1,8, 4 parois), les 4 vis de la
  NeoKey passent.
- Aucun contact des plots avec les switches ni avec le corps de l'encodeur.
- Bouton v2 : clic franc, sans frottement, tient bien sur l'axe.
- Encodeur tourné de 90° : la fiche QT sort côté écran.
- **Coin de module validé** : il sert de base au bas de la maquette d'encombrement.

**Câble 4209 (même jour)**
- Boîtier noir d'une broche mâle : **14 mm** (valeur supposée confirmée).
- Derrière la carte T5, il reste ≈ 19 mm jusqu'à l'intérieur du dos. Connecteur 2×20 (≈ 8,5)
  + boîtier (14) + courbure du fil (≈ 3) ≈ 25,5 mm : **le 4209 ne tient pas** dans l'épaisseur,
  même avec un connecteur plus bas (5 + 14 + 3 = 22 > 19).
- **Décision** : branchement par la **prise P5** (IO15/IO16) avec le câble Adafruit 4424 (JST PH
  4 broches ↔ STEMMA QT, 200 mm, ≈ 3 € + port, hors budget accepté). Ordre des fils à refaire
  avant de brancher : P5 = 3,3 V, IO15, IO16, GND ; câble = GND, V+, SDA, SCL. BOM mise à jour.

## 2026-10-04 — Maquette d'encombrement modélisée (P1)

- `cad/module-maquette` créé depuis le coin de module validé : module complet 125 × 115 × 26,
  4 coins arrondis, dos ouvert, fenêtre de l'écran, 4 plots pour les pattes de la carte
  (avant-trous de 4 mm, 1 mm de façade sous la vis), trou de l'USB-C dans la paroi droite.
- Cotes de la carte T5 **provisoires** : le .3mf exporté n'est **pas à imprimer** avant la
  réception de la carte, les mesures et la mise à jour des paramètres.
