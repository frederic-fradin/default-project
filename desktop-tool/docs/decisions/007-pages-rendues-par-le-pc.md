# 007 — Pages dessinées par le PC et protocole de messages PC ↔ objet

| | |
|---|---|
| **Date** | 2026-10-05 |
| **Statut** | ✅ Acceptée le 2026-10-05 — précise l'[ADR 001](001-architecture-objet-compagnon.md) (le firmware n'a plus de gabarits) |

## Contexte

L'ADR 001 fait de l'objet un terminal générique, mais le cadrage hésite sur ce que le PC lui
envoie : des **gabarits** (liste, carte, horloge) remplis avec du texte, ou des **pages déjà
dessinées**. Il faut trancher avant d'écrire le code, car ce choix fixe le protocole, la part
de C++ et la façon de tester sans la carte (simulateur sur le PC).

Données de la carte LilyGO T5 4,7" S3 : écran **960 × 540** en **16 niveaux de gris**,
8 Mo de PSRAM, USB-C natif de l'ESP32-S3 (port série virtuel).

## Options étudiées

1. **Gabarits sur l'objet** : le PC envoie du texte et des valeurs, le firmware met en page.
   Messages légers, mais polices à convertir pour l'ESP32 (accents compris), mise en page en
   C++, et carte à reprogrammer à chaque nouveau gabarit.
2. **Pages dessinées par le PC** : le PC dessine l'image avec Python (Pillow) et l'envoie ;
   l'objet l'affiche sans la comprendre.

## Décision

**Option 2.** Le firmware sait seulement : afficher une image (page entière ou zone), régler les
LED, renvoyer les événements des touches et de la molette. Il ne contient **aucun texte ni
aucune police**.

### Images

- Page entière : 960 × 540, **4 bits par pixel** (16 gris), 2 pixels par octet, soit
  **259 200 octets**. `0x0` = noir, `0xF` = blanc.
- Ordre des pixels : ligne par ligne, de gauche à droite ; dans un octet, pixel pair dans les
  4 bits de poids faible (convention de la bibliothèque epdiy, **à vérifier sur la carte**).
- Le PC peut n'envoyer qu'une **zone** (x, y, largeur, hauteur ; x et largeur pairs), par
  exemple la ligne surlignée d'une liste quand on tourne la molette.
- Deux modes de rafraîchissement choisis par le PC : **complet** (efface les traces, l'écran
  clignote, ≈ 1 s) et **rapide** (sans clignotement, laisse des traces : pour les petits
  changements).

### Trame (commune à tous les messages)

| Champ | Taille | Contenu |
|---|---|---|
| Marqueur | 2 octets | `DT` (0x44 0x54) |
| Type | 1 octet | voir le tableau des messages |
| Longueur | 4 octets | taille de la charge (entier non signé, petit-boutiste) |
| Charge | *n* octets | selon le type |
| Contrôle | 4 octets | CRC32 du type, de la longueur et de la charge |

La trame ne dépend pas du transport : elle passe telle quelle sur le câble USB (v1), sur une
connexion TCP locale (**simulateur**) et plus tard en Wi-Fi ou Bluetooth (v2).

### Messages

| Code | Nom | Sens | Charge |
|---|---|---|---|
| `0x01` | `HELLO_REQ` | PC → objet | vide : « qui es-tu ? » |
| `0x02` | `HELLO` | objet → PC | version du protocole, version du firmware, largeur, hauteur, bits par pixel, nombre de touches |
| `0x10` | `DRAW` | PC → objet | x, y, largeur, hauteur (2 octets chacun), mode (0 complet, 1 rapide), pixels |
| `0x11` | `LED` | PC → objet | cible (0-3 = touches, 4 = molette), rouge, vert, bleu (0,0,0 = éteinte) |
| `0x20` | `KEY` | objet → PC | touche (0-3 = touches, 4 = clic de la molette), état (1 appuyée, 0 relâchée) |
| `0x21` | `WHEEL` | objet → PC | crans tournés depuis le dernier envoi (entier signé, + = sens horaire) |
| `0x30` | `DONE` | objet → PC | code du message traité : l'image est affichée, le PC peut envoyer la suivante |
| `0x3F` | `ERROR` | objet → PC | code d'erreur (trame invalide, zone hors écran, taille incorrecte…) |

### Déroulement type

1. Le compagnon démarre et envoie `HELLO_REQ` ; l'objet répond `HELLO` (le PC vérifie la
   version et la taille de l'écran).
2. Le PC envoie la page d'accueil (`DRAW` complet), attend `DONE`.
3. On tourne la molette : l'objet envoie `WHEEL +1` ; le PC redessine la ligne concernée
   (`DRAW` rapide, petite zone), attend `DONE`.
4. Appui sur la touche 1 : `KEY 0 appuyée` puis `KEY 0 relâchée` ; le PC lance le raccourci. Il
   reconnaît lui-même un **appui long** grâce au temps écoulé entre les deux.

Le PC n'envoie jamais un `DRAW` avant le `DONE` du précédent : l'objet n'a besoin que d'une
image en mémoire.

## Conséquences

- ✅ Firmware court, écrit une fois : une nouvelle page ou fonctionnalité = du Python seulement.
- ✅ Polices, accents, icônes, mise en page : tout se fait avec Pillow, sur le PC.
- ✅ **Simulateur fidèle** : une fenêtre Python reçoit les mêmes trames par TCP et affiche
  exactement l'image que verra l'écran ; le compagnon se développe **avant la carte**.
- ✅ Toute la logique de navigation (surlignage, défilement) reste en Python.
- ❌ Une page entière pèse ≈ 260 Ko : ≈ 0,3 à 0,5 s par USB, du même ordre que le
  rafraîchissement de l'e-paper (accepté). En Bluetooth (v2), compter plusieurs secondes :
  prévoir alors une compression, ajoutable sans casser le protocole (nouveau mode de `DRAW`).
- ❌ Chaque mouvement de molette fait un aller-retour PC ↔ objet (quelques millisecondes en USB,
  négligeable devant le rafraîchissement).
- ❌ Si le PC s'éteint, l'écran garde la dernière page (propre à l'e-paper) sans indiquer qu'il
  n'est plus à jour : accepté en v1 (le PC éteint est acceptable, cadrage §4).
