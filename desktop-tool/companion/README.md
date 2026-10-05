# Compagnon desktop-tool

Application Python sur le PC : dessine les pages de l'objet et réagit à ses touches et à sa
molette. Protocole : [ADR 007](../docs/decisions/007-pages-rendues-par-le-pc.md).

## Installation

```powershell
cd desktop-tool/companion
python -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
```

## Lancer avec le simulateur (sans la carte)

Dans deux terminaux :

```powershell
.venv\Scripts\python simulator.py   # 1. la fenêtre qui imite l'objet
.venv\Scripts\python main.py        # 2. le compagnon
```

Dans la fenêtre : touches **1 à 4** du clavier (rangée du haut ou pavé numérique) ou clic
sur les touches dessinées ; **roulette de la souris** = molette ; **Entrée** ou clic sur la
molette = clic de la molette. Le simulateur imite les délais de l'e-paper (≈ 1 s avec flash
en rafraîchissement complet, ≈ 0,3 s en rapide). Fermer la fenêtre arrête aussi le compagnon.

## Lancer avec la carte

Dans `config.toml`, remplacer `target = "sim"` par le port série de la carte (ex. `"COM5"`).

## Tests

```powershell
.venv\Scripts\python -m pytest
```

## Organisation

| Fichier | Rôle |
|---|---|
| `main.py` | Lance le compagnon |
| `simulator.py` | Fenêtre qui imite l'objet |
| `config.toml` | Connexion (simulateur ou port série) |
| `src/protocol.py` | Trames et messages (ADR 007) |
| `src/image.py` | Image Pillow ↔ pixels 4 bits de l'écran |
| `src/link.py` | Ouverture de la connexion |
| `src/pages.py` | Dessin des pages |
| `src/app.py` | Boucle principale : événements → état → page |
