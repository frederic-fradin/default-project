"""Lance le compagnon : `python main.py` (lancer d'abord `python simulator.py` si target = "sim")."""

import tomllib
from pathlib import Path

from src import app, link

config = tomllib.loads((Path(__file__).parent / "config.toml").read_text(encoding="utf-8"))
app.run(link.open_link(config["link"]["target"]))
