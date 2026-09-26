# 001 — Architecture : objet « terminal » + application compagnon sur le PC

| | |
|---|---|
| **Date** | 2026-09-26 |
| **Statut** | ✅ Acceptée |

## Contexte

Les fonctionnalités visées (agenda et emails Outlook, to-do, notes, raccourcis, IA à terme)
demandent de s'authentifier auprès de services externes, de stocker des données et
d'exécuter des actions sur le PC. Je maîtrise Python mais pas l'électronique ni l'embarqué.
L'objet est posé sur un bureau à la maison, à côté du PC.

## Options étudiées

1. **Objet autonome en Wi-Fi** : l'objet se connecte lui-même à Outlook, stocke les données.
2. **Objet terminal + compagnon PC** : l'objet affiche et capte ; une application Python sur le
   PC fait tout le reste, via un câble USB-C.
3. **Écran secondaire USB + clavier de macros du commerce** : aucune électronique, mais l'objet
   se réduit à un support imprimé.

## Décision

**Option 2.** L'objet embarque un firmware **générique** (gabarits d'écran remplis par le PC,
événements des touches renvoyés au PC). Toute la logique métier est en Python sur le PC.

## Conséquences

- ✅ L'essentiel du développement se fait en Python, avec toutes les bibliothèques du PC.
- ✅ Aucun secret (tokens Outlook) stocké sur l'objet.
- ✅ Les raccourcis peuvent lancer n'importe quelle action PC, modifiables sans reprogrammer.
- ✅ Un seul câble, pas de Wi-Fi en v1.
- ✅ Nouvelle fonctionnalité = nouveau module Python, sans toucher au firmware.
- ❌ L'objet n'affiche rien d'utile quand le PC est éteint (accepté).
- ❌ Il faut concevoir un protocole de messages PC ↔ objet.
