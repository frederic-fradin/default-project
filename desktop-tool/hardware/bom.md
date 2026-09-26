# Liste des composants (BOM) — v1.0 (tout est commandé)

Contraintes : **zéro soudure**, budget ≤ 150 €, objet ≤ ~127 × 127 mm, écran noir et blanc,
commandes à gauche. Prix indicatifs relevés le 2026-09-26, **hors frais de port** sauf mention.

## 1. Liste proposée

| # | Composant | Rôle | Qté | Prix indicatif | Où chercher |
|---|---|---|---|---|---|
| 1 | **LilyGO T5 4,7" E-Paper V2.3 ESP32-S3**, version **« Female pin Welded »** (connecteurs femelles déjà soudés), sans tactile | Cerveau de l'objet + écran 960 × 540, 16 niveaux de gris, 119 × 62 × 8 mm, USB-C | 1 | ≈ 40–50 € | ✅ [Amazon.fr, ASIN B0BWDV5W6N](https://www.amazon.fr/dp/B0BWDV5W6N) (vérifié le 2026-09-26) |
| 2 | **Adafruit NeoKey 1x4 QT I2C** (réf. 4980) | 4 touches mécaniques enfichables, LED RGB, 2 connecteurs STEMMA QT (sous la carte, aux deux bouts), 76,5 × 21,5 × 4,6 mm | 1 | 10,22 € | [DigiKey](https://www.digikey.fr/fr/products/detail/adafruit-industries-llc/4980/14319123) |
| 3 | **Adafruit Kailh Mechanical Key Switches – Tactile Brown** (réf. 4954, lot de 10, compatibles MX) | Touches : relief tactile sans clic ; si besoin, joints toriques sous les capuchons pour réduire le bruit | 1 lot (4 utilisés + 6 de rechange) | 7,14 € | [DigiKey](https://www.digikey.fr/fr/products/detail/adafruit-industries-llc/4954/14113455) |
| 4 | **Adafruit I2C Stemma QT Rotary Encoder Breakout with Encoder** (réf. **5880**, molette déjà soudée — ne pas confondre avec la 4991 vendue sans molette) | Molette crantée + clic + 1 LED RGB, I²C adresse 0x36, carte 25 × 25 mm | 1 | 8,17 € | [DigiKey](https://www.digikey.fr/fr/products/detail/adafruit-industries-llc/5880/22596384) |
| 5 | Câble **STEMMA QT ↔ broches mâles** (Adafruit 4209, ≈ 150 mm) | Carte (connecteur femelle, broches I²C SDA 18 / SCL 17 / 3,3 V / GND) → NeoKey | 1 (+ 1 de rechange) | 0,97 € pièce | [DigiKey](https://www.digikey.fr/fr/products/detail/adafruit-industries-llc/4209/10230003) |
| 6 | Câble STEMMA QT ↔ STEMMA QT ≈ 100 mm (réf. 4210) | NeoKey → molette | 1 | ≈ 1 € | [DigiKey](https://www.digikey.fr/fr/products/detail/adafruit-industries-llc/4210/10230021) |
| 7 | Câble USB-C ↔ USB (A ou C selon le PC), **données**, 1–1,5 m, coudé si possible | Alimentation + communication avec le PC | 1 | ≈ 6–10 € | Amazon |
| 8 | Vis auto-taraudeuses pour plastique M2/M2,5 (assortiment) | Fixations | 1 lot | ≈ 5–8 € | Amazon |
| 9 | Aimants néodyme 6 × 2 mm | Fixation du module dans le pupitre (4 + 4) | 1 lot de 20+ | ≈ 4–6 € | Amazon |
| 10 | Patins antidérapants | Stabilité sur le bureau | 1 lot | ≈ 2–4 € | Amazon, magasin de bricolage |
| 11 | Filament PLA : couleur du corps + noir + couleur d'accent (+ blanc ?) | Boîtier | selon stock | ≈ 20–35 € | Bambu Lab, Amazon |

**Total estimé : ≈ 100 – 145 €** (selon le filament déjà en stock et les frais de port).

## Suivi des commandes

| # | Composant | Statut | Date | Livraison prévue |
|---|---|---|---|---|
| 1 | LilyGO T5 4,7" V2.3 ESP32-S3 « Female pin Welded » | ✅ Commandé (Amazon.fr) | 2026-09-26 | mi-octobre 2026 |
| 2 | Adafruit NeoKey 1x4 QT I2C (4980) | ✅ Commandé (DigiKey) | 2026-09-26 | ≈ 3 jours |
| 3 | Kailh Tactile Brown × 10 (4954) | ✅ Commandé (DigiKey) | 2026-09-26 | ≈ 3 jours |
| 4 | Molette Adafruit 5880 | ✅ Commandé (DigiKey) | 2026-09-26 | ≈ 3 jours |
| 5 | Câble STEMMA QT ↔ broches mâles (4209) × 2 | ✅ Commandé (DigiKey) | 2026-09-26 | ≈ 3 jours |
| 6 | Câble STEMMA QT ↔ QT (4210) | ✅ Commandé (DigiKey) | 2026-09-26 | ≈ 3 jours |
| 7 | Câble USB-C data | ✅ Commandé (Amazon) | 2026-09-26 | |
| 8–10 | Vis, aimants 6 × 2 mm N52, patins | ✅ Commandé (Amazon) | 2026-09-26 | |
| 11 | Filament PLA | ✅ En stock | | |

Revendeur retenu pour 2 à 6 : **DigiKey**, un seul panier (≈ 29 € + 25 € de port, gratuit dès 75 €).
Botland, BerryBase et Opencircuit n'avaient plus le NeoKey en stock (2026-09-26).

## 2. Branchement (sans soudure)

```
PC ──USB-C── [LilyGO T5 4,7"] ──I²C── [NeoKey 1x4] ──I²C── [Molette Adafruit 5880]
                         (câble broches mâles → QT)     (câble QT ↔ QT)
```

Les deux modules partagent le bus I²C de la carte (SDA = GPIO 18, SCL = GPIO 17), déjà utilisé
par l'horloge interne : adresses toutes différentes (0x30 NeoKey, 0x36 molette, 0x51 horloge).

## 3. Points à vérifier AVANT d'acheter ⚠️

1. ✅ **Carte T5** : version **« Female pin Welded »** retenue (ASIN B0BWDV5W6N). Elle n'a pas
   de connecteur STEMMA QT, mais ses connecteurs femelles soudés exposent le bus I²C : on s'y
   branche avec un câble « STEMMA QT vers broches mâles », sans soudure. Une prise PH2.0 4 broches
   existe aussi sur la carte (solution de secours, brochage à vérifier à réception).
   ⚠️ Sur la page Amazon, vérifier que la variante sélectionnée est bien **Welded / soudée**
   (et non « Non-Welded »), puis vérifier à réception, sur le schéma de brochage du
   fabricant, que SDA 18 et SCL 17 sont bien accessibles sur le connecteur femelle.
2. **Disponibilité et délai** : la carte est souvent en rupture sur le site officiel ; les
   délais depuis l'Asie sont de 2 à 4 semaines, ce qui cale bien avec la P1 (prise en main de
   Fusion en attendant).
3. ✅ **Tension** : NeoKey et molette Adafruit 5880 fonctionnent en 3,3 V.

## 4. Pour la v2 (à ne pas acheter maintenant)

| Composant | Rôle | Prix indicatif | Points d'attention |
|---|---|---|---|
| Batterie LiPo plate ≈ 5 × 40 × 60 mm (type 504060), ≈ 2 000 mAh, **avec protection intégrée** | Fonctionnement sans câble | ≈ 10–15 € | La carte charge la batterie mais **n'a pas de protection** ; vérifier le type de connecteur (JST-PH 2,0 mm ou 1,25 mm selon la version de la carte) **et le sens des fils** avant de brancher |
| Adaptateur USB-C magnétique compatible données (optionnel) | Poser le module sur le pupitre pour le recharger sans brancher de câble | ≈ 8–12 € | Fiabilité variable, à tester |

## 5. Alternatives étudiées

| Option | Pour | Contre | Verdict |
|---|---|---|---|
| **Elecrow CrowPanel 4,2" E-Paper** (≈ 27 $) | Moins cher, molette + 2 boutons déjà sur la carte | 400 × 300 seulement (texte moins fin), commandes soudées sur la carte à des positions imposées (difficile de les mettre à gauche), pas de connecteur Grove, Arduino uniquement | **Plan B** si la T5 est introuvable |
| M5Stack M5PaperS3 (≈ 59 $) | Écran 4,7" tactile, batterie, boîtier inclus | Produit en fin de vie, plus cher | Écarté |
| Elecrow CrowPanel Advance 4,3" couleur (≈ 31 $) | Très réactive, tactile, connecteurs Grove, micro intégré | Écran couleur rétroéclairé (moins discret), 122 mm de long (très juste) | Écarté après le choix du noir et blanc |
| Écran 5" couleur | Plus grand | 136 mm de long : ne tient pas dans 127 mm | Écarté |
