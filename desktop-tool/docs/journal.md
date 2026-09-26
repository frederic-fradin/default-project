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
