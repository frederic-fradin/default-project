# Document de cadrage — desktop-tool

| | |
|---|---|
| **Version** | v1.8 — module en paysage (ADR 006), station à 12 colonnes percée |
| **Date** | 2026-09-26 |
| **Auteur** | Frédéric Fradin |
| **Statut** | ✅ Cadrage validé le 2026-09-26 — document de référence. Les éléments encore marqués `[À VALIDER]` seront tranchés en P1 |

---

## 1. Contexte et intention

Construire un **objet physique posé sur le bureau (à la maison)**, relié au PC, **discret**,
qui m'assiste dans mes tâches quotidiennes (raccourcis, agenda, emails, tâches, notes, puis
assistant IA), avec des **fonctionnalités évolutives**.

Le projet couvre trois thématiques, avec des **poids volontairement inégaux** :

| Thématique | Poids | Ce que je veux en retirer |
|---|---|---|
| 💻 Fonctionnalités / programmation | ⭐⭐⭐ Principal | Des fonctionnalités vraiment utiles, bien pensées, faciles à faire évoluer |
| 🎨 Design & impression 3D | ⭐⭐⭐ Principal | Un bel objet : conception 3D, finitions, multicouleur (AMS) avec la Bambu Lab A1 |
| 🔧 Assemblage électronique | ⭐ Minimal | Le strict nécessaire : **pas de soudure**, des modules qui se branchent |

**Arbitrage acté** : quand l'utilité et l'apprentissage s'opposent côté électronique, on prend
**la solution la plus simple à assembler**. Le temps gagné va aux fonctionnalités et au design.

---

## 2. Objectifs

### 2.1 Objectif global

Disposer d'ici **mi-avril 2027** d'une **v1.0** : un **module** imprimé sobre, à écran noir et
blanc, **clipsable dans un pupitre**, branché au PC par un seul câble USB-C, avec **3 raccourcis,
une molette, l'agenda du jour, une to-do list, les alertes email, un bloc-notes et un lanceur
de commandes pour mes CLI Python**, et qui accueille de nouvelles fonctionnalités par simple
ajout de module logiciel. Le module est **dimensionné dès la v1 pour recevoir une batterie** et
passer en sans-fil en v2 sans refaire le boîtier.

### 2.2 Critères de succès de la v1.0

| # | Critère | Mesure |
|---|---|---|
| O1 | L'objet est utilisé | Utilisé ≥ 4 jours ouvrés sur 5 pendant 1 mois |
| O2 | Le design me plaît | Objet fini, fidèle à la direction B (§6), discret, aucun câble visible sauf l'USB-C |
| O3 | Zéro soudure | Tout l'assemblage se fait avec connecteurs, vis, clips et aimants |
| O4 | Évolutivité logicielle | Nouvelle fonctionnalité = nouveau module côté PC, sans reprogrammer l'objet |
| O5 | Mise à jour facile | Mise à jour du firmware sans ouvrir le boîtier |
| O6 | Reproductibilité | Sources 3D, liste des composants et code versionnés dans le dépôt |

---

## 3. Périmètre

### 3.1 Dans le périmètre (v1.0)

- Conception et impression du boîtier, multicouleur (AMS), plusieurs itérations.
- Assemblage **sans soudure** de modules du commerce.
- Firmware de l'objet (affichage, touches, molette, communication avec le PC).
- **Application compagnon sur le PC** en Python (voir §7) : Outlook, to-do, notes,
  raccourcis, et une petite interface de saisie.
- Fonctionnalités v1 : voir §5.

### 3.2 Hors périmètre (v1.0)

| Élément | Raison | Horizon |
|---|---|---|
| Batterie / fonctionnement autonome | Sécurité, complexité | ✅ v2 (acté) — **volume réservé et charge intégrée à la carte dès la v1** (§6.3) |
| Connexion sans fil (Wi-Fi ou Bluetooth) | Le câble suffit en v1 | v2 — **intégrée à la carte**, protocole conçu dès la v1 pour ne pas dépendre du câble (§7.1) |
| Transcription vocale (bloc-notes) et assistant IA | Complexité | v2 — micro du PC ou micro USB, transcription locale |
| Envoi du contenu des emails à une IA | Confidentialité : lecture simple et alertes uniquement | ✅ Écarté en v1 (acté) |
| Compte Google | Un seul compte Outlook en v1 | v1.x ou v2 |
| Fonctionnement sans PC allumé | L'objet est un « terminal » du PC | ✅ Accepté (acté) |
| Écran couleur, écran tactile, animations | Écran noir et blanc voulu (discrétion) | ✅ Écarté (acté) |
| Circuit imprimé sur mesure, soudure | Contraire à l'arbitrage §1 | Non prévu |

---

## 4. Contraintes et ressources

### 4.1 Imprimante — Bambu Lab A1 + AMS lite

| Caractéristique | Conséquence |
|---|---|
| Volume 256 × 256 × 256 mm | Largement suffisant, boîtier en une seule pièce possible |
| Cadre ouvert | **PLA / PETG** ; pas d'ABS / ASA |
| AMS lite (4 couleurs) ✅ | Corps + touches + accent de couleur + marquages, sans peinture |
| Buse 0,4 mm | Texte en relief ou en creux : trait ≥ ~0,8 mm |

**Finitions** : les objets de référence ont des surfaces lisses (moulage par injection). En
impression FDM, les couches restent visibles → la direction B, avec ses **faces planes**, est
favorable : façade imprimée **à plat sur le plateau**, arrondis sur les arêtes.

### 4.2 Assemblage sans outillage spécifique

Pas de fer à souder, donc pas d'inserts laiton posés à chaud. Fixations retenues :
**clips imprimés**, **vis auto-taraudeuses pour plastique**, **aimants néodyme** (façade
amovible, pied détachable), éventuellement un point de colle pour caler les switches.

### 4.3 Compétences

| Domaine | Niveau | Conséquence |
|---|---|---|
| Python | ✅ Bon | L'essentiel de la logique sera en Python côté PC |
| 3D | 🟡 Débutant sur Blender → **Fusion** | Prise en main en P1 avec des pièces test |
| Électronique | ❌ Non maîtrisé, pas équipé | Modules « plug-and-play » uniquement |

**Décision** : **Fusion** (licence « Personal Use » gratuite, usage non commercial) pour le
boîtier. Blender reste possible pour des rendus, sans obligation.

### 4.4 Disponibilité

**4 h / semaine** (acté), pause pendant les fêtes.

### 4.5 Budget — plafond 150 €

| Poste | Estimation | Réel (TTC) |
|---|---|---|
| Carte ESP32-S3 avec écran e-paper 4,7" (livraison comprise) | 40 – 55 € | 59,00 € |
| Module 4 touches mécaniques sans soudure + switches | 15 – 25 € | 17,36 € |
| Molette (encodeur) sans soudure | 9 – 12 € | 8,17 € |
| Câbles à connecteurs + câble USB-C data + petit matériel (vis, aimants, patins) | 15 – 20 € | 35,11 € |
| Frais de port DigiKey | — (non prévu) | 30,00 € |
| Filament PLA (3–4 couleurs, itérations) | 20 – 35 € | 0 € (en stock) |
| **Total** | **~100 – 145 €** | **149,64 €** |

**Reste disponible : 0,36 €** (au 2026-09-27, tout le matériel v1 est commandé). La TVA DigiKey est
répartie sur chaque poste ; le centime d'arrondi est porté sur le petit matériel. Le dépassement
vient du port DigiKey et de la carte, plus chère que prévu ; il est compensé par le filament déjà
en stock. Tout achat supplémentaire (filament, rechange) fera dépasser le plafond.

Détail, alternatives et liens : [`hardware/bom.md`](../hardware/bom.md). Pas de coût d'API IA
en v1. On achète **après** validation de la liste (fin P0). La batterie (≈ 10–15 €) est achetée
en v2, hors budget v1. Les aimants du pupitre sont déjà prévus dans la liste d'achats.

---

## 5. Fonctionnalités

### 5.1 Principes

- L'objet **affiche et capte** (écran, touches, molette) ; le PC **calcule et se connecte**.
- On **consulte et agit rapidement** sur l'objet (cocher une tâche, lancer un raccourci), on
  **saisit** sur le PC.
- **Écran e-paper = interface « papier »** : des pages fixes et lisibles, pas d'animation ;
  la molette fait défiler **par pas** (élément par élément), pas en continu.

### 5.2 Fonctionnalités retenues et découpage en versions

| Fonctionnalité | Sur l'objet | Côté PC | Complexité | Version |
|---|---|---|---|---|
| **3 raccourcis** | 3 touches physiques à symbole neutre ; **la fonction est affichée à l'écran** en face de chaque touche (ADR 004) | Exécute l'action : raccourci clavier, application, script, URL | 🟢 | **v0.1 (MVP)** |
| **Navigation** | 4e touche (icône maison) « Accueil / page suivante » + molette (tourner = défiler, appuyer = valider) | Gestion des pages | 🟢 | **v0.1 (MVP)** |
| **Agenda du jour** (Outlook) | Prochain rendez-vous, compte à rebours, liste du jour | Lecture du calendrier (méthode déjà utilisée dans mes scripts) | 🟢 | **v0.1 (MVP)** |
| **To-do list** (propre à l'outil) | Liste, défiler avec la molette, cocher d'un appui | Stockage local + interface de saisie | 🟢 | v0.2 |
| **Alertes email** | Expéditeur + objet du dernier email ; **LED de couleur** sur une touche si l'expéditeur fait partie d'une liste « importants » | Lecture de la boîte Outlook, filtrage par expéditeur. **Aucune IA** | 🟡 | v0.2 |
| **Affichage depuis PowerShell** | Affiche un texte ou le résultat d'une commande envoyé par `desk show` | `Get-Date \| desk show`, `desk show "Build OK"` | 🟢 | v0.2 |
| **Bloc-notes** | Affichage de notes épinglées (post-it permanent) | Saisie / édition sur le PC | 🟢 | v1.0 |
| **Lanceur de commandes** (mes CLI Python) | Menu « Commandes » : choisir avec la molette, lancer d'un appui, voir l'état (en cours / OK / erreur) et les dernières lignes du résultat ; LED quand une tâche longue se termine | Exécute des commandes **déclarées à l'avance** dans le fichier de configuration, avec des paramètres choisis dans des listes | 🟡 | v1.0 |
| **Transcription vocale** des notes | Appui long sur une touche → dictée | Micro du PC, transcription **locale** (modèle type Whisper) | 🟡 | v2 |
| **Assistant IA** | Question / réponse | API IA ou modèle local | 🔴 | v2 |

**Interface de saisie sur le PC** ✅ : une **commande dans le terminal PowerShell**, légère
et utilisée au quotidien. Exemples :

```powershell
desk todo add "Relire le cadrage"     # ajouter une tâche
desk todo                              # lister les tâches
desk note "Rappeler le fournisseur"    # épingler une note
desk vip add boss@entreprise.com       # expéditeur « important »
```

La configuration des raccourcis et des réglages reste dans un **fichier texte** (TOML) éditable.
La commande et l'application compagnon partagent la même base SQLite locale.

**L'objet comme « terminal déporté » de PowerShell et de mes CLI** — ce qui est possible et ce
qui ne l'est pas :

| Usage | Faisable ? | Comment |
|---|---|---|
| **Envoyer un affichage depuis PowerShell** | ✅ Oui | `desk show` : n'importe quel script ou pipeline peut afficher un texte ou un résultat sur l'objet |
| **Lancer mes CLI Python depuis l'objet** | ✅ Oui | Menu de commandes prédéfinies (fichier TOML), paramètres choisis avec la molette, résultat résumé à l'écran |
| **Suivre une tâche longue** | ✅ Oui | L'objet indique « en cours », puis la LED s'allume à la fin (succès ou erreur) |
| **Taper des commandes libres sur l'objet** | ❌ Non | Pas de clavier ; l'e-paper est inadapté au défilement d'un terminal |
| **Voir en direct la sortie complète d'un script** | ❌ Non | Seules les dernières lignes et l'état final sont affichés |

Exemple de déclaration d'une commande :

```toml
[[commands]]
name  = "Rapport F1"
run   = "python -m f1.cli report --season {saison}"
cwd   = "C:/Users/fradi/Python/f1"
params.saison = ["2026", "2025"]
```

**Sécurité** : l'objet ne peut lancer **que** les commandes déclarées dans ce fichier, jamais une
commande arbitraire reçue par le câble ou, plus tard, par le réseau.

### 5.3 Backlog (après v1.0)

Compte Google, assistant IA, batterie, statut « en réunion », suivi de l'imprimante A1,
météo, qualité de l'air, tableaux de bord perso (ex. F1)…

---

## 6. Intention design

### 6.1 Analyse des images de référence (`images/`)

| Image | Ce qu'on retient |
|---|---|
| desktop-1 — robot jaune | Formes douces, écran incliné sur socle, personnalité |
| desktop-2 — calculatrice jaune | Corps en pupitre, touches rondes contrastées |
| desktop-3 — boîtier noir | Minimaliste, **une couleur d'accent (orange)**, **molette**, typographie pixel |
| desktop-4 — panneau blanc | Grille écran + grandes touches plates à libellés + molette |
| **desktop-5 — panneau carré** ⭐ | **Référence principale** : écran + touches empilées sur le côté, grosse typographie noir et blanc |
| desktop-6 — thermostat | Écran en haut, touches à pictogrammes, blanc et noir |
| **desktop-9 — panneau gris** ⭐ | **Référence couleurs et symboles** (2026-09-27) : corps gris chaud mat, touches gris clair aux symboles fins et discrets, **un seul bouton d'accent orange** |

### 6.2 Direction retenue : B « Panneau », inspirée de l'image 5 ✅

| Élément | Choix |
|---|---|
| Esprit | Épuré, précis, **discret** (n'attire pas l'œil), avec **une petite touche de couleur** |
| Format | Encombrement max **≈ 5" × 5" (127 × 127 mm)** en façade |
| Écran | **Noir et blanc (e-paper)**, **en paysage** depuis l'ADR 006 (portrait auparavant), typographie forte comme l'image 5 |
| Commandes | **En bas** (ADR 006) : molette en bas à gauche, sous le pouce gauche (utilisateur gaucher) ; 4 touches en ligne en bas à droite |
| Couleurs | **Trois styles en balance** (PLA mat Panchroma) : **A** module **Charcoal Black** + molette **Army Red** ; **B** module **Muted White** + molette **Sunrise Orange** ; **C** module **Ash Grey** + touches **Muted White** + molette **Sunrise Orange** (image desktop-9, préférée). **Station de la couleur du corps du module.** `[À VALIDER]` en P1 |
| Touches | **Symboles neutres** : **1, 2 et 3 barres** sur les touches 1 à 3, **maison** sur la touche 4 ; **fonction de chaque touche affichée à l'écran**, en face d'elle (ADR 004). Symboles **gravés en creux**, touche imprimée **face visible contre le plateau** |
| Lumière | Aucune lumière émise par l'écran ; seules les LED des touches s'allument, **à faible intensité**, pour les alertes |
| Posture sur le bureau | **Station modulaire** (ADR 005) : socle avec rainure à stylo et grille d'accroches, pupitre du module et pupitre MagSafe clipsés dessus, inclinés à 65° |

Esquisse de disposition (vue de face, échelle approximative), **en paysage depuis l'ADR 006** :

```
 ◄────────────────── ≈ 125 mm ──────────────────►
┌───────────────────────────────────────────────┐   ▲
│                                               │   │
│              ÉCRAN e-paper 4,7"               │   │
│          (paysage)  noir et blanc             │   │
│                                               │ ≈ 115 mm
│     MUET ▾   CAPTURE ▾  OUTLOOK ▾  ACCUEIL ▾   │   │
├───────────┬───────────────────────────────────┤   │
│  ╭─────╮  │  ┌────┐ ┌────┐ ┌────┐ ┌────┐       │   │
│  │  ◉  │  │  │ |  │ │ || │ │||| │ │ ⌂  │       │   │
│  ╰─────╯  │  └────┘ └────┘ └────┘ └────┘       │   │
└───────────┴───────────────────────────────────┘   ▼
  molette        4 touches (pas de 19 mm)
```

> **Challenge — L'écart entre les touches est imposé.** Le module de touches sans soudure
> retenu (§7.2) place **4 switches tous les 19 mm** dans une colonne. On ne peut donc pas
> faire 3 grandes touches carrées comme sur l'image 5 (≈ 30 mm de haut chacune). Proposition :
> **4 touches larges et basses** (≈ 36 × 17 mm) = 3 raccourcis + 1 touche « Accueil ». C'est
> un vrai plus pour la navigation. Les grandes touches carrées demanderaient des boutons
> séparés et davantage de câblage. `[À VALIDER]`

> **Challenge — L'e-paper n'est pas réactif comme un écran de téléphone.** Il ne rafraîchit
> qu'une partie de l'écran en quelques centaines de millisecondes. Un rafraîchissement complet
> prend 1 à 2 secondes, avec un « clignotement » noir et blanc, à faire de temps en temps pour
> effacer les traces. Pour un agenda, une to-do ou des notes, c'est parfait (et très
> lisible, sans lumière). Pour faire défiler une longue liste avec la molette, ce sera
> un peu saccadé. Les raccourcis, eux, ne sont pas concernés : ce sont des touches physiques.
> ✅ Accepté en connaissance de cause.

**Maquettes** : 3 variantes en planches cotées (perspective, face, profil, dessus) et 2 postures dans
[`design/maquettes.html`](design/maquettes.html) (également publiées en page web).

### 6.3 Variante retenue : 1 « Colonne », en module + pupitre ✅

Voir la fiche [`decisions/003-module-pupitre-batterie.md`](decisions/003-module-pupitre-batterie.md).

| Élément | Choix |
|---|---|
| **Module** | Variante 1 **tournée en paysage** (ADR 006) : écran en haut, molette en bas à gauche, 4 touches en ligne en bas à droite (3 raccourcis + Accueil), USB-C au dos. **125 × 115 × 26 mm** |
| **Station** ✅ (ADR 005, remplace le pupitre ci-dessous) | **Socle** 250 × 90 × 10 mm **percé de 48 trous ronds** (12 colonnes × 4 rangées, pas de 20 mm) ; **éléments clipsés** par 4 tenons ronds : pupitre du module (6 colonnes, lame à 65°, connecteur USB-C magnétique noyé dans la lame) et pupitre MagSafe (4 colonnes, iPhone 13 Pro en portrait, palet déjà possédé, sans rebord devant) ; **2 colonnes libres** pour un futur élément ; station de la couleur du module |
| ~~Pupitre~~ *(abandonné, trop massif)* | Objet séparé qui **reprend la forme du module** (mêmes arrondis, mêmes plaques), **décalé vers la droite** pour laisser le bord gauche libre à la prise en main. Le module s'y dépose et tient par **4 aimants** (Ø6 mm au dos). Forme retenue ✅ : **volume plein, en triangle symétrique de profil** (face et dos à ≈ 55°), avec une **empreinte de 26 mm** où le module s'incruste sur **toute son épaisseur** (façade au même niveau que le pupitre, seules touches et molette dépassent) ; **aucun rebord devant la façade** ; empreinte **ouverte à gauche et en haut** : le module dépasse de 12 mm à gauche ; pupitre avec **bordures droite et basse de 25 mm** et **arrêté 36 mm sous le haut du module** ; arêtes arrondies ; aimants hauts du module à redescendre vers ≈ 75 mm pour rester sur le pupitre |
| **Module seul** | Dos plat avec patins : se pose à plat ou se prend en main |
| **Batterie (v2)** | Emplacement réservé derrière la carte pour une LiPo plate ≈ 5 × 40 × 60 mm (≈ 2 000 mAh). La carte intègre déjà le circuit de charge |
| **Câble** | USB-C **au dos du module** (rallonge à montage sur panneau), branché par le **connecteur magnétique de la lame** ; câble en gorge au dos de la lame puis sous la semelle. En v2, la station peut devenir la **station de charge** |
| **Antenne** | Aucun aimant ni métal devant l'antenne de la carte |

> **Challenge — L'autonomie sur batterie sera limitée.** L'e-paper ne consomme presque rien,
> mais une connexion Wi-Fi ou Bluetooth **permanente** pour rester réactif aux touches
> consomme beaucoup plus. Ordre de grandeur : **une à deux journées** avec 2 000 mAh, pas
> des semaines. D'où l'intérêt du pupitre qui recharge. `[À VALIDER en v2]`

La conception détaillée (forme exacte, couleurs, écran de repos) se fait en P3.

---

## 7. Architecture cible

### 7.1 Principe : un « terminal » de bureau et un « cerveau » sur le PC

Voir la fiche de décision [`decisions/001-architecture-objet-compagnon.md`](decisions/001-architecture-objet-compagnon.md).

```
┌──────────────────────── PC Windows ─────────────────────────┐
│  Application compagnon (Python, lancée au démarrage)          │
│   ├─ Connecteurs : Outlook (agenda, emails) · to-do · notes   │
│   ├─ Moteur de raccourcis (clavier, applis, scripts)          │
│   ├─ Interface de saisie locale (to-do, notes, réglages)      │
│   └─ Envoie à l'objet des « pages » toutes prêtes à afficher  │
└──────────────────────────┬──────────────────────────────────┘
                           │ 1 câble USB-C (alimentation + données série)
┌──────────────────────────┴──────────────────────────────────┐
│  Objet desktop-tool (ESP32-S3 + e-paper 4,7" portrait)        │
│   ├─ Affiche des gabarits génériques (liste, carte, horloge…) │
│   ├─ 4 touches à LED + molette (I²C, sans soudure)            │
│   └─ Renvoie les événements (« touche 2 », « molette +1 »)    │
└─────────────────────────────────────────────────────────────┘
```

**Protocole indépendant du transport** : les messages PC ↔ objet (pages à afficher,
événements) sont définis une fois pour toutes ; en v1 ils passent par le câble USB, en v2 par
Wi-Fi ou Bluetooth **sans changer le reste du code**.

**Principe clé : un firmware générique.** L'objet ne connaît pas Outlook ni la to-do ; il sait
afficher quelques **gabarits de page** que le PC remplit. Nouvelle fonctionnalité = nouveau
module Python sur le PC, **sans reprogrammer l'objet**.

### 7.2 Choix techniques

| Sujet | Options | Recommandation provisoire |
|---|---|---|
| Type d'écran | E-paper · écran couleur IPS avec interface en noir et blanc | **E-paper** : aucune lumière, aspect papier, très discret, très sobre en énergie (bon pour la batterie en v2). Contrepartie : moins réactif (§6.2) |
| Carte | LilyGO T5 4,7" S3 · Elecrow CrowPanel 4,2" e-paper · Elecrow CrowPanel Advance 4,3" (couleur) | **LilyGO T5 4,7" S3** : 960 × 540 en 16 niveaux de gris (texte très net), 119 × 64 mm (tient dans 127 mm en portrait), USB-C. ⚠️ Stock et connecteur I²C à vérifier avant achat. Détails et alternatives : `hardware/bom.md` |
| Touches | Module 4 touches I²C (Adafruit NeoKey 1x4) · touches séparées | **NeoKey 1x4** : switches enfichables, LED RGB par touche (alertes), branchement sans soudure |
| Molette | M5Stack Unit Encoder · Adafruit 5880 | **Adafruit 5880** (molette déjà soudée, connecteur STEMMA QT comme le NeoKey, clic intégré, LED) |
| Langage de l'objet | MicroPython · C++ (Arduino / ESP-IDF) | **C++**, écrit une fois avec mon aide : les pilotes e-paper de ces cartes existent surtout en C++. Toute la logique évolutive reste en Python sur le PC |
| Lecture Outlook | Méthode déjà utilisée dans mes scripts Python | **Réutiliser l'existant** |
| Stockage to-do / notes | Fichier JSON · base SQLite locale | SQLite locale sur le PC |
| Interface de saisie | Page locale (Streamlit) · commande dans le terminal | ✅ **Commande `desk` dans PowerShell** (Python) + fichier TOML pour les réglages |
| Logiciel 3D | Blender · Fusion · Onshape | ✅ **Fusion** |

Chaque choix fera l'objet d'une fiche dans `docs/decisions/`.

---

## 8. Démarche, étapes et calendrier prévisionnel (base 4 h / semaine)

Principe : **prototype utile sur la table d'abord**, design ensuite.

### 8.1 Phases et jalons

| Phase | Période | Contenu | Livrables | Critère de sortie |
|---|---|---|---|---|
| **P0 — Cadrage** ✅ | 26 sept 2026 (terminé en avance) | Questions §11.2, validation de la liste d'achats, commande | Cadrage v1.0, fiches décision, commande | Commande passée |
| **P1 — Prise en main** | 28 sept → 15 nov (7 sem.) — Fusion et pièces test d'abord, électronique à réception de la carte (mi-oct.) | **Code** : afficher un gabarit sur l'e-paper, lire les touches et la molette, échanger des messages PC ↔ objet. **3D** : prise en main de Fusion, pièces test (clips, touches sur switch, aimants, multicouleur, texte), **maquette d'encombrement** avec les vraies pièces | « Hello world » PC ↔ objet, pièces test, maquette | Le PC affiche un texte sur l'objet et réagit à une touche |
| **P2 — MVP sur table** | 16 nov → 20 déc (5 sem.) | Firmware générique + compagnon : **raccourcis**, **navigation**, **agenda du jour** | v0.1 | 🎯 **J1** : utilisé tous les jours depuis 1 semaine, même sans boîtier |
| *Pause fêtes* | 21 déc → 3 janv 2027 | Usage libre, notes d'amélioration | | |
| **P3 — Design & boîtier** | 4 janv → 28 févr (8 sem.) | Croquis, modélisation Fusion, 2–3 itérations d'impression multicouleur, intégration. En parallèle : **to-do**, **alertes email**, interface de saisie | Fichiers 3D + 3MF, boîtier, v0.2 | 🎯 **J2** : l'objet est dans son boîtier, sur le bureau |
| **P4 — Finition v1.0** | 1er mars → 11 avril (6 sem.) | **Bloc-notes**, finitions (écran de repos, typographie, icônes), démarrage automatique, documentation | v1.0 taguée | 🎯 **J3** : critères O1–O6 vérifiés |
| **P5 — v2** | À partir de mai 2027 | Transcription vocale, assistant IA, batterie, compte Google, backlog | v2.x | Revue de backlog mensuelle |

### 8.2 Vue calendrier

```
             2026                         2027
             Oct     Nov     Déc     Jan     Fév     Mar     Avr
P0 Cadrage   ██
P1 Prise m.    ██████████
P2 MVP                 ██████████
Fêtes                            ░░
P3 Design                          ████████████████
P4 Finition                                        ████████████
Jalons                           J1              J2          J3
```

### 8.3 Marges

- Environ **100 h de travail** au total jusqu'à la v1.0.
- Principaux risques de retard : **disponibilité de la carte**, **pilote e-paper** et
  **prise en main de Fusion**.
- Hypothèse réaliste avec +30 % : v1.0 **fin mai / juin 2027**.
- Le jalon **J1** reste le plus important.

---

## 9. Risques

| # | Risque | Prob. | Impact | Parade |
|---|---|---|---|---|
| R1 | Dérive du périmètre | 🔴 | Haut | Découpage en versions (§5.2), rien de nouveau avant la v1.0 |
| R2 | Accès Outlook (compte pro) | 🟢 | Haut | Déjà accessible depuis mes scripts Python : réutiliser la méthode |
| R3 | Carte e-paper en rupture de stock ou connecteur I²C absent | 🟡 | Haut | Vérifier avant achat ; alternative CrowPanel 4,2" e-paper (`hardware/bom.md`) |
| R4 | Pilote e-paper délicat (rafraîchissement partiel, traces) | 🟡 | Moyen | Exemples du fabricant en P1 ; interface conçue pour l'e-paper (pages fixes) |
| R5 | Rendu FDM loin des références | 🟢 | Moyen | Direction B à faces planes ; pièces test de finition en P1 |
| R6 | Courbe d'apprentissage de Fusion | 🟡 | Moyen | Pièces d'exercice en P1 |
| R7 | Budget serré (150 €) | 🟡 | Moyen | Liste validée avant achat ; revendeurs avec retour facile |
| R8 | Fuite de secrets (tokens Outlook) dans git | 🟡 | Haut | Secrets uniquement sur le PC, exclus via `.gitignore` dès le premier commit |
| R9 | Perte de motivation (4 h/sem., 6 mois) | 🟡 | Haut | MVP utile dès décembre, journal de bord avec photos |
| R10 | Encombrement : tout faire tenir dans ≈ 127 × 127 mm | 🟡 | Moyen | Maquette imprimée avec les vraies pièces en P1 |
| R11 | Touches imprimées qui accrochent (tolérance sur le switch) | 🟡 | Faible | Pièces test en P1, plusieurs jeux de tolérance |
| R12 | Batterie LiPo : la carte n'a **pas de circuit de protection**, et le sens du connecteur varie selon les fabricants | 🟡 | Haut | Batterie **avec protection intégrée**, connecteur vérifié avant branchement (v2) |
| R13 | Autonomie sans fil décevante | 🟡 | Moyen | Pupitre qui recharge, mise en veille de l'objet, mesures en v2 |
| R16 | ~~Affichage en portrait : la bibliothèque officielle LilyGO ne gère pas la rotation~~ **Levé (ADR 006)** : le module passe en paysage, orientation native de la carte | ⚪ | — | Bibliothèque epdiy à jour (`epd_set_rotation(EPD_ROT_PORTRAIT)`), ou pages dessinées déjà tournées par le PC (Python/Pillow). Test dès P1 |
| R15 | Pupitre : module incrusté à 100 % difficile à retirer, ou ensemble instable à l'appui | 🟡 | Moyen | Pièce test en P1 ; encoche pour le doigt, patins antidérapants, lest si besoin |
| R14 | Lanceur de commandes détourné (exécution non voulue) | 🟢 | Haut | Liste blanche de commandes dans le fichier de configuration uniquement |

---

## 10. Organisation du projet

- **Dépôt** : `desktop-tool/` — `firmware/` (objet), `companion/` (application PC, à créer en
  P1), `cad/`, `hardware/`, `images/` (références design), `docs/`.
- **Journal de bord** (`docs/journal.md`) : une entrée par session, avec photos.
- **Décisions** (`docs/decisions/NNN-titre.md`) : contexte, options, choix, raison.
- **Revue de phase** : mise à jour de ce document à chaque fin de phase.

---

## 11. Questions ouvertes

### 11.1 Tranchées

| # | Question | Réponse |
|---|---|---|
| Q1 | Priorité ? | Fonctionnalités et design ; assemblage minimal |
| Q2 | Fonctionnalités ? | Raccourcis, agenda, email, to-do, bloc-notes, IA à terme |
| Q3 | Niveau électronique ? | Non maîtrisé, pas équipé → zéro soudure |
| Q4 | Lieu, lien au PC ? | Maison, connexion au PC nécessaire |
| Q5 | AMS, budget ? | AMS oui, budget max 150 € |
| — | Batterie ? | v2 |
| — | Bloc-notes ? | Saisie PC en v1, transcription vocale en v2 |
| — | Confidentialité email ? | Pas d'IA : lecture simple + alerte visuelle selon l'expéditeur |
| — | PC éteint ? | Acceptable |
| Q6 | Compte ? | Outlook, un seul compte ; Google éventuellement plus tard |
| Q7 | To-do ? | Liste propre à l'outil |
| Q9 | Entrées ? | Touches physiques, 3 raccourcis pour commencer + molette |
| Q12 | Disponibilité ? | 4 h / semaine |
| Q14 | Accès Outlook ? | Compte pro, déjà utilisé dans des scripts Python → pas de problème d'accès |
| Q16 | Direction design ? | **B « Panneau »**, référence image 5, avec une touche de couleur |
| Q17 | Disposition ? | ~~Écran portrait, commandes à gauche~~ → **écran paysage en haut, molette en bas à gauche, touches en bas à droite** (ADR 006) |
| Q19 | Taille ? | Objet ≈ 5" × 5" max |
| Q20 | Logiciel 3D ? | Fusion |
| — | Type d'écran ? | Noir et blanc, pour rester discret |
| Q21 | Interface de saisie ? | Commande dans le terminal PowerShell |
| Q23 | Réactivité de l'e-paper ? | Acceptée |
| Q22 | Variante ? | **Variante 1**, en module + pupitre clipsable (aimants) |
| Q24 | Commande ? | ✅ Carte LilyGO T5 4,7" V2.3 ESP32-S3 « Welded » commandée le 2026-09-26, livraison mi-octobre ; autres composants à commander (voir `hardware/bom.md`) |
| Q25 | Lanceur de commandes ? | **Gardé en v1.0** (et `desk show` en v0.2) |
| — | Batterie, sans-fil ? | Pris en compte dès maintenant dans les dimensions (26 mm) et l'architecture ; activés en v2 |

### 11.2 À trancher pendant la P1

| # | Question | Impact | Statut |
|---|---|---|---|
| Q27 | Couleurs : choix entre les styles A, B et C (station de la couleur du module), validation définitive après une plaquette test imprimée | Design | ⏳ |
| Q26 | Pupitre, à confirmer à l'essai en P1 : **stabilité** avec l'incrustation à 100 % (appuis sur les touches et la molette), **facilité pour retirer le module** (prévoir une encoche pour le doigt si besoin), angle de 55° | Conception P3 (n'empêche pas la commande) | ⏳ |

---

## Historique des versions

| Version | Date | Modifications |
|---|---|---|
| v0.1 | 2026-09-26 | Création — brouillon de cadrage |
| v0.2 | 2026-09-26 | Arbitrages Q1–Q5 : priorité fonctionnalités/design, zéro soudure, architecture objet + compagnon PC, budget 150 €, batterie en v2 |
| v0.3 | 2026-09-26 | Outlook seul, emails sans IA, to-do propre, 3 touches, 4 h/sem. → v1.0 mi-avril 2027, intention design (2 directions), firmware générique |
| v0.4 | 2026-09-26 | Direction B (image 5), commandes à gauche, Fusion, **écran noir et blanc e-paper**, sélection du matériel et liste d'achats, questions Q21–Q24 |
| v0.5 | 2026-09-26 | Réactivité e-paper acceptée, saisie via commande `desk` dans PowerShell, maquettes blueprint des 3 variantes et des postures |
| v0.6 | 2026-09-26 | Variante 1 retenue en module + pupitre, épaisseur 26 mm avec emplacement batterie, protocole indépendant du transport, affichage depuis PowerShell (`desk show`) et lanceur de commandes pour les CLI Python |
| v0.7 | 2026-09-26 | Lanceur de commandes confirmé en v1 ; pupitre repensé dans le style du module, décalé à droite : trois concepts (berceau en L, socle à fente, dos décalé) |
| v0.8 | 2026-09-26 | Pupitre repensé : volume plein triangulaire de profil, face avant au contour du module agrandi, sans bordure avant, arêtes adoucies ; versions centrée et décalée à droite |
| v0.9 | 2026-09-26 | Pupitre : module incrusté sur la moitié de son épaisseur (empreinte 13 mm), sans rebord, ouvert à gauche, décalé à droite |
| v0.10 | 2026-09-26 | Pupitre : bordure droite 36 mm, haut du pupitre 36 mm sous le haut du module, empreinte ouverte à gauche et en haut |
| v0.11 | 2026-09-26 | Pupitre : dos incliné comme la face (triangle symétrique), bordure droite réduite à 25 mm |
| v0.12 | 2026-09-26 | Pupitre : bordure basse portée à 25 mm, comme la bordure droite |
| v0.13 | 2026-09-26 | Pupitre : incrustation du module portée à 100 % (26 mm), visuel validé, stabilité à confirmer en P1 |
| v0.14 | 2026-09-26 | Carte validée (ASIN B0BWDV5W6N, version soudée) ; câble I²C adapté ; affichage portrait : solutions identifiées (risque R16) |
| **v1.0** | 2026-09-26 | **Cadrage validé** : carte commandée, P0 clôturée, démarrage de P1 avec Fusion en attendant la livraison |
| v1.1 | 2026-09-26 | Couleurs provisoires : Muted White (module, touches), Sunrise Orange (molette, libellés), Fossil Grey (pupitre) |
| v1.2 | 2026-09-27 | Touches : **icônes au lieu de libellés texte** (ex. maison = Accueil), pour ne pas figer une touche à une fonctionnalité |
| v1.3 | 2026-09-27 | Après tests d'impression : icônes **en creux**, touches imprimées face visible côté plateau ; couleurs rouvertes entre deux styles (noir + rouge / blanc + orange) |
| v1.4 | 2026-09-27 | ADR 004 : touches à symboles neutres, fonctions affichées à l'écran en face de chaque touche |
| v1.5 | 2026-09-27 | Budget : dépenses réelles relevées, **149,64 €** pour un plafond de 150 € |
| v1.6 | 2026-09-27 | ADR 005 : pupitre triangle abandonné (trop massif) au profit d'une **station modulaire** (socle + pupitre module + pupitre MagSafe clipsés) ; USB-C au dos du module via connecteur magnétique |
| v1.7 | 2026-09-27 | Style C « gris chaud + orange » (image desktop-9) ajouté ; station de la couleur du corps du module |
| v1.8 | 2026-09-27 | ADR 006 : module en paysage (écran en haut, commandes en bas) ; R16 levé ; station à 12 colonnes (250 × 90 mm) percée de 48 trous ronds, sans rainure à stylo, iPhone 13 Pro, 2 colonnes libres |
