# 004 — Touches neutres, fonctions affichées à l'écran

| | |
|---|---|
| **Date** | 2026-09-27 |
| **Statut** | ✅ Acceptée |

## Contexte

Les fonctionnalités finales ne sont pas arrêtées : une touche peut changer de rôle d'une version à
l'autre, voire d'une page à l'autre. Les premiers tests d'impression ont montré qu'un marquage en
relief n'est pas agréable ; la gravure en creux, touche imprimée face visible contre le plateau,
donne un meilleur rendu.

## Options étudiées

1. **Libellés texte sur les touches** : lisibles, mais figent chaque touche à une fonction.
2. **Icônes de fonction** (+, −, entrée, retour) : doublonnent la molette (tourner = défiler,
   appuyer = valider) et font perdre les 3 raccourcis du MVP.
3. **Symboles neutres + fonction affichée à l'écran**, en face de chaque touche.

## Décision

**Option 3.** Touches 1 à 3 : symboles neutres, **1, 2 et 3 barres** (choisi le 2026-09-27). Touche 4 : maison (Accueil),
seule fonction fixe. L'écran e-paper affiche, à côté de chaque touche, la fonction qu'elle a sur
la page courante.

## Conséquences

- ✅ Aucune fonction figée dans le plastique : tout se reconfigure côté PC.
- ✅ Une touche peut changer de rôle selon la page (ex. « Répondre » sur une page Outlook).
- ❌ Contrainte de conception : les touches doivent être **alignées sur des zones de l'écran**
  (hauteur et pas des touches ↔ bandeau d'étiquettes à gauche de l'écran), à valider sur la
  maquette d'encombrement.
- ❌ Une colonne de l'écran portrait (≈ 540 px de large) est réservée aux étiquettes.
- ❌ Chaque changement de page rafraîchit aussi les étiquettes (e-paper : pages fixes, R4).
