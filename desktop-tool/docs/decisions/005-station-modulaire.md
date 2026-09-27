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

- **Socle** : dalle 220 × 98 × 10 mm aux arrondis du module ; **rainure à stylo** de
  180 × 12 × 6 mm, centrée, devant ; **grille de 22 accroches** (2 rangées de 11 logements
  10 × 10 × 6 mm, au pas de 20 mm).
- **Éléments clipsés** sur la grille, chacun avec une semelle de 3 mm et des tenons
  (9,6 × 9,6 × 6 mm, fente et ergot) :
  - **pupitre module** : lame d'appui à 65°, renfort, cale ; **USB-C du module au dos**
    (rallonge à montage sur panneau), branché par un **connecteur USB-C magnétique noyé dans la
    lame** : poser le module suffit à le brancher ;
  - **pupitre MagSafe** : iPhone Pro **en portrait**, lame 80 × 112 mm avec empreinte
    Ø 56,5 × 5,5 mm pour le palet, cale et griffe de sécurité.
- Les câbles passent en gorge au dos des lames puis sous les semelles.

## Conséquences

- ✅ Objet **évolutif** : de nouveaux éléments (vide-poche, porte-stylos, support d'écouteurs,
  logement de batterie en v2) se clipsent sans refaire le socle ; les éléments se déplacent par
  pas de 20 mm.
- ✅ Pièces séparées, plus simples à imprimer ; toutes tiennent sur le plateau de l'A1.
- ✅ Le module reste amovible ; le connecteur magnétique se détache seul.
- ✅ Palet MagSafe déjà possédé : aucun achat pour la charge du téléphone.
- ❌ Connecteur USB-C magnétique (données + charge) et rallonge sur panneau : ≈ 10 à 15 €,
  **hors budget** (plafond de 150 € déjà atteint).
- ❌ Position du port USB-C au dos à valider avec la carte T5 réelle (livraison mi-octobre).
- ❌ Tenons clipsables à régler par une pièce test (jeu ≈ 0,2 mm par côté, ergot ≈ 0,4 mm) ;
  en secours, 2 aimants Ø 6 × 3 mm par élément.
- ❌ Emprise plus large que le pupitre seul (220 × 98 mm) ; le haut du téléphone culmine à
  ≈ 156 mm.
