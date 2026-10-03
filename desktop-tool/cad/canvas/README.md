# Canevas Fusion

Une image par vue de pièce, à l'échelle 10 px = 1 mm, à importer comme canevas dans Fusion pour
dessiner les esquisses par-dessus. Cotes : `docs/design/coin-module-test.html`.

| Image | Plan | Origine |
|---|---|---|
| `coin-module_facade_XY.png` | XY | coin bas gauche de la façade |
| `coin-module_coupe_XZ.png` | XZ | coin bas gauche, au dos (z = 0) |
| `bouton_dessus_XY.png` | XY | centre du bouton |
| `bouton_coupe_XZ.png` | XZ | centre du dessous du bouton |

## Dans Fusion

1. **Insérer › Canevas**, choisir le plan indiqué, puis l'image. Opacité vers 50 %.
2. Dans le navigateur, dossier **Canevas** : clic droit sur l'image › **Étalonner**. Cliquer le
   centre des deux croix rouges de l'étalon, puis saisir la longueur écrite dessus (100 ou 20 mm).
3. Clic droit › **Modifier le canevas** : déplacer l'image pour poser la croix **ORIGINE** sur
   l'origine de Fusion. Sur le plan XZ, si l'image arrive retournée, utiliser les cases de
   retournement de la même boîte de dialogue.
4. Dessiner l'esquisse par-dessus, en gardant les cotes en paramètres : le canevas sert de guide,
   pas de référence de cote.

## Régénérer

`python cad/canvas/generer_canvas.py` (Chrome nécessaire pour le rendu PNG).
