# Compagnon desktop-tool — conventions de code

Application Python sur le PC qui pilote l'objet (ADR 001 et 007 dans `../docs/decisions/`).
Le PC dessine les pages et les envoie ; l'objet affiche et renvoie les touches et la molette.

## Conventions

- **Pas de classes** : le porteur du projet est analyste Python, pas développeur. Modules de
  fonctions, état dans de simples dictionnaires.
- **Fonctions pures dans `src/`** quand c'est possible : `protocol.py`, `image.py`, `pages.py`
  n'ouvrent ni connexion ni fenêtre.
- **Pas de sur-ingénierie** : pas d'abstraction ni de gestion d'erreurs pour des cas qui ne se
  produisent pas.
- **Commentaires** uniquement pour le « pourquoi » non évident.
- Textes de l'interface et messages en **français**.

## Points à respecter

- `protocol.py` et `image.py` fixent les octets échangés : le firmware C++ doit faire
  exactement pareil. Toute modification passe par l'ADR 007 et les tests (`pytest`).
- Une seule image à la fois chez l'objet : ne jamais envoyer un `DRAW` avant le `DONE` du
  précédent.
- `simulator.py` imite la carte (mêmes trames, en TCP local) : le garder à jour quand le
  protocole évolue.
