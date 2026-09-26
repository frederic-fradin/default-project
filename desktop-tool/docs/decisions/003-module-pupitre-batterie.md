# 003 — Variante 1 en module + pupitre, batterie et sans-fil anticipés

| | |
|---|---|
| **Date** | 2026-09-26 |
| **Statut** | ✅ Acceptée |

## Contexte

Trois variantes de façade ont été dessinées (`docs/design/maquettes.html`). L'objet doit
pouvoir, à terme, fonctionner sur batterie et sans fil, sans refaire le boîtier.

## Options étudiées

1. **Variante 1 « Colonne »** : molette en façade, 4 touches larges, écran portrait.
2. **Variante 2 « Molette sur la tranche »** : façade plus épurée, encodeur monté couché.
3. **Variante 3 « Grandes touches »** : 3 grandes touches, matériel de touches différent.

Pour la posture : objet unique (vertical sur pied ou pupitre) ou **deux objets** (module +
pupitre).

## Décision

- **Variante 1**, réalisée en **deux objets** : un **module** autonome et un **pupitre** dans
  lequel il se clipse par **4 aimants**.
- *Révision du 2026-09-26* : pupitre plein en **triangle symétrique de profil** (face et dos à
  55°), avec une **empreinte de 26 mm** où le module s'incruste sur toute son épaisseur, **sans
  rebord** devant la façade ; empreinte ouverte à gauche et en haut, bordures droite et basse de
  25 mm, haut du pupitre 36 mm sous le haut du module (voir `docs/design/maquettes.html`).
- **Épaisseur du module portée à 26 mm** pour réserver l'emplacement d'une LiPo plate
  (≈ 5 × 40 × 60 mm) derrière la carte.
- **Protocole PC ↔ objet indépendant du transport** : USB en v1, Wi-Fi ou Bluetooth en v2.

## Conséquences

- ✅ Le matériel de la liste d'achats reste valable (NeoKey 1x4 + molette Adafruit 5880).
- ✅ Passage sur batterie en v2 sans refaire le boîtier ; la carte intègre la charge.
- ✅ Le pupitre peut devenir la station de charge en v2.
- ✅ Deux pièces plus simples à imprimer qu'un objet unique avec pied.
- ❌ Module un peu plus épais (26 mm au lieu de 24).
- ❌ Batterie à choisir avec protection intégrée (la carte n'en a pas).
- ❌ Autonomie limitée à une ou deux journées si la connexion sans fil reste active.
