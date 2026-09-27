## LOCAL

1. Création du dossier/projet en local dans le dossier G:/PYTHON

2. Création du .gitgnore dans VSCODE

3. Création de l'environnement virtuel
python -m venv env
.\env\Scripts\activate

## LOCAL REPOSITORY (GIT)

4. Création dépot local GIT
git init ( git init --initial-branch=main )
git add * (ou préciser un nom de fichier)
git status
git commit -m "Commentaires"
git log

## REMOTE REPOSITORY (GITLAB)

5. Création du projet sur GitLab (en ligne)

6. Copie du lien vers projet présent dans README

7. Création liaison local > remote
git remote add origin <>https://gitlab.com/lecureur/cer_engrais.git<>

8. Création de la nouvelle branche (si besoin)

9. Push des commits dans remote
git push origin <>dev<>


# CREATION FROM REMOTE

 git clone <>https://gitlab.com/lecureur/lec_valorisation.git<>


# BRANCH MANAGEMENT

Pour créer une nouvelle branche : git checkout -b main

Pour changer de branche, (p.e. se mettre sur dev) : git checkout dev

Les étapes effectués :
From branch main > git push origin main > git checkout dev > git push origin dev 