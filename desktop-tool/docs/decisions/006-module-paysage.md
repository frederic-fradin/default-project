# 006 — Module en paysage : écran en haut, commandes en bas

| | |
|---|---|
| **Date** | 2026-09-27 |
| **Statut** | ✅ Acceptée — modifie la disposition de la variante 1 ([ADR 003](003-module-pupitre-batterie.md)) |

## Contexte

La variante 1 « Colonne » (ADR 003) place l'écran en portrait à droite et les commandes en
colonne à gauche : molette en haut, 4 touches empilées dessous. Une **impression test à
l'échelle du module** montre qu'en main, la molette tombe trop haut pour le pouce gauche.

## Options étudiées

1. **Garder la colonne à gauche** (ADR 003) : écran portrait, molette en haut à gauche.
2. **Tourner le module de 90° vers la gauche** : écran en paysage en haut, molette en bas à
   gauche, touches en ligne en bas à droite.

## Décision

**Option 2.** Module de **125 × 115 × 26 mm** (même volume, tourné) :

- **Écran e-paper 4,7" en paysage**, en haut.
- **Molette en bas à gauche**, sous le pouce gauche quand on tient le module (utilisateur
  gaucher).
- **4 touches en ligne en bas à droite**, au pas de 19,05 mm du NeoKey 1x4 : 1, 2, 3 barres puis
  maison (ADR 004).
- Les **étiquettes des touches** (ADR 004) passent d'une colonne à gauche de l'écran à une
  **bande en bas de l'écran**, chacune juste au-dessus de sa touche.
- Port **USB-C au dos**, branché par la lame d'appui de la station (ADR 005).

## Conséquences

- ✅ Molette sous le pouce en prise en main, et facile d'accès posée sur la station.
- ✅ La carte T5 affiche **nativement en paysage** : le risque R16 (rotation en portrait)
  disparaît.
- ✅ Le NeoKey 1x4 est une barrette : il se monte naturellement à l'horizontale.
- ✅ Écran large : deux colonnes d'informations (heure et rendez-vous à gauche, agenda à droite).
- ❌ Module plus large (125 mm au lieu de 115) : la station passe à 12 colonnes (250 mm).
- ❌ Barre de touches (76 mm) logée juste entre la molette et le bord droit (≈ 9 mm de marge) ;
  la molette est à 8,5 mm du bord bas : à valider sur une pièce test.
- ❌ Pages de l'écran à redessiner en paysage (pas encore commencées : sans impact).
