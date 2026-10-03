# 005 — Station de bureau modulaire au lieu du pupitre triangle

| | |
|---|---|
| **Date** | 2026-09-27 |
| **Statut** | ✅ Acceptée — remplace la forme du pupitre de l'[ADR 003](003-module-pupitre-batterie.md) |

## Contexte

Le pupitre plein en triangle (ADR 003, révision du 2026-09-26) est jugé **trop massif** sur la
maquette. Le bureau accueille aussi un iPhone (iPhone Pro, avec un palet MagSafe déjà possédé)
et un stylo. Les usages de l'objet évolueront : le support ne doit pas figer l'agencement.

## Options étudiées

1. **Pupitre triangle plein** (ADR 003) : module incrusté à 100 %, massif.
2. **D · Béquille** : module posé sur le bureau, béquille fine aimantée au dos.
3. **E · Ailettes** : deux voiles fins cachés derrière le module, deux griffes devant.
4. **F · Plateau** : dalle basse, module appuyé sur une lame ; version d'un seul bloc puis
   **version modulaire** (socle + éléments clipsés).

## Décision

**Option 4, en version modulaire** (voir `docs/design/maquettes.html`, planche « F · Station
modulaire ») :

- **Socle** : dalle **250 × 90 × 10 mm** aux arrondis du module, **percée sur toute sa
  surface de 48 trous ronds** Ø 10 × 6 mm (12 colonnes × 4 rangées, au pas de 20 mm, 15 mm de
  marge). 12 colonnes : le maximum imprimable posé droit sur l'A1 (256 mm). La profondeur est
  celle des semelles : aucun trou ne reste vide devant ou derrière un élément.
- **Éléments clipsés** sur la grille, chacun avec une semelle de 3 mm percée aux coins et
  **4 chevilles** séparées (tige Ø 9,6 fendue avec ergot, tête Ø 13 noyée dans un lamage de la
  semelle, imprimées couchées), qui se clipsent dans une gorge au fond des trous du socle :
  - **pupitre module** (6 colonnes) : lame d'appui à 65°, renfort, assise sous l'arête basse
    (face avant en pente douce) ; **USB-C du module au dos**
    (rallonge à montage sur panneau), branché par un **connecteur USB-C magnétique noyé dans la
    lame** : poser le module suffit à le brancher ;
  - **pupitre MagSafe** (4 colonnes) : iPhone 13 Pro avec coque (74 × 149 × 12 mm) **en
    portrait**, lame 62 × 112 mm avec empreinte Ø 56,5 × 5,5 mm pour le palet ; assise sous le
    téléphone en pente douce, **sans rebord devant** (le palet tient le téléphone) ;
  - **2 colonnes libres** à droite, pour un futur élément (boîte à crayons…) ; le support
    AirPods a été écarté.
- Plus d'éléments : une **rallonge de socle** clipsable, reliée par des pions dans les trous de
  bord.
- *Révision du 2026-09-27* : rainure à stylo et grille de 22 accroches carrées remplacées par la
  surface percée de trous ronds ; socle élargi pour le module en paysage (ADR 006).
- *Révision du 2026-10-03* : les 4 tenons intégrés sous la semelle deviennent **4 chevilles
  séparées**. Intégrés, ils pendaient sous la semelle (aucune face pour imprimer l'élément sans
  support) et pliaient entre deux couches. Couchées, les chevilles plient dans le plan des
  couches ; socle et éléments s'impriment à plat. Pièce test : `docs/design/tenons-test.html`.
- Les câbles passent en gorge au dos des lames puis sous les semelles.
- **Couleur** : la station (socle et éléments) prend **la couleur du corps du module**, pour que
  l'ensemble se lise comme un seul objet.

## Conséquences

- ✅ Objet **évolutif** : de nouveaux éléments (boîte à crayons, repose-stylo, vide-poche,
  logement de batterie en v2) se clipsent sans refaire le socle ; les éléments se déplacent par
  pas de 20 mm ; une cheville ronde se clipse sans orientation imposée.
- ✅ Pièces séparées, plus simples à imprimer ; toutes tiennent sur le plateau de l'A1.
- ✅ Le module reste amovible ; le connecteur magnétique se détache seul.
- ✅ Palet MagSafe déjà possédé : aucun achat pour la charge du téléphone.
- ❌ Connecteur USB-C magnétique (données + charge) et rallonge sur panneau : ≈ 10 à 15 €,
  **hors budget** (plafond de 150 € déjà atteint).
- ❌ Position du port USB-C au dos à valider avec la carte T5 réelle (livraison mi-octobre).
- ❌ Chevilles à régler par une pièce test (jeu 0,2 mm au rayon, ergot 0,2 / 0,3 / 0,4 mm) ;
  ≈ 0,7 mm de jeu dans l'axe des méplats, à observer ; en secours, 2 aimants Ø 6 × 2 mm par
  élément.
- ❌ 4 petites pièces de plus par élément ; la tête des chevilles se voit sur la semelle quand
  elle n'est pas sous la lame.
- ❌ Emprise plus large que le pupitre seul (250 × 90 mm) ; le haut du téléphone culmine à
  ≈ 152 mm.
- ❌ Socle de 250 mm : 3 mm de jeu par côté sur le plateau de l'A1.
