## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre shell OS
exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/spleenYou/OC-P13.git`

#### Créer l'environnement virtuel

- `cd /path/to/OC-P13`
- `python3 -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement : `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel :
  `which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Variable d'environnement

Pour fonctionner, des variables d'environnement sont nécessaires.

- `cd /path/to/OC-P13`
- `export SERVER_TYPE=TEST`
- `export HOSTS=127.0.0.1,localhost`
- `export SECRET_KEY=SECRET_KEY_EXAMPLE`
- `export SENTRY_DSN=https://517a76dae9a195009...3e6f03e@o450...7232.ingest.de.sentry.io/4509...2160`
- Description des variables :
    - SERVER_TYPE -> TEST ou PROD selon le type de serveur.
    - HOSTS -> adresses de votre serveur, séparés par une virgule.
    - SECRET_KEY -> clé secrète utilisée par Django pour la cryptographie.
    - SENTRY_DSN -> le DSN fourni par Sentry pour le suivi des logs.

#### Exécuter le site

- `cd /path/to/OC-P13`
- `source venv/bin/activate`
- `pip install -r requirements.txt`
- `python manage.py runserver`
- Aller à l'adresse `http://localhost:8000` dans un navigateur web.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/OC-P13`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/OC-P13`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/OC-P13`
- Ouvrir une session shell : `sqlite3`
- Se connecter à la base de données : `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données : `.tables`
- Afficher les colonnes de la table des profils : `pragma table_info(Profiles_profile);`
- Lancer une requête sur la table des profils : `select user_id, favorite_city from
  Profiles_profile where favorite_city like 'B%';`
- Pour quitter : `.quit`

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin` et le mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1`
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Image Docker

Une image Docker est disponible pour des tests.

Mettre les variables d'environnement dans un fichier.

Puis exécuter `docker run --env-file <filename> -d -p 8000:8000 spleen85/oc-p13:latest`

Et aller sur `http://localhost:8000`

### Déploiement

#### Description

Le déploiement de ce projet est automatisé via GitHub Actions. À chaque modification poussée sur la branche master, un
pipeline CI/CD se déclenche automatiquement pour :

1. Exécuter les tests.
2. Construire une nouvelle image Docker de l'application Django pour l'historique (oc-p13:<GIT_COMMIT>).
3. Construire une nouvelle image Docker de l'application Django pour le déploiement (oc-p13:latest).
4. Pousser ces images sur un registre Docker.
5. Déployer automatiquement l'image "latest" sur [Render](https://render.com) (hébergeur cloud).

Cela permet de garantir que la dernière version stable du code est toujours en production, sans intervention manuelle.

#### Configuration requise

Pour que le déploiement fonctionne correctement, il faut :

- Un compte GitHub avec accès au dépôt.
- Un compte Docker avec accès au hub.
- Un fichier de workflow GitHub Actions configuré dans .github/workflows/main.yml (fourni dans le dépôt).
- Un compte Render configuré avec un service Web app Docker déployant depuis l’image Docker construite (oc-p13:latest).
- Les variables d'environnement suivantes définies dans l'environnement Render:\
  (Mettre n'importe quelle valeur, elles seront mises à jour par github)
    - HOSTS
    - SECRET_KEY
    - SENTRY_DSN
    - SERVER_TYPE
- Les variables d’environnement suivantes définies dans les Secrets GitHub :
    - RENDER_API_KEY : clé d’API pour déployer sur Render.
    - RENDER_SERVICE_ID : ID du service Render (dans l'url render du projet : dashboard.render.com/web/srv-<
      RENDER_SERVICE_ID>)
    - URL_DEPLOY_HOOK : l'URL fournie par Render (settings > Deploy > Deploy Hook)
    - DOCKER_USERNAME : nom d'utilisateur Docker
    - DOCKER_PASSWORD : Mot de passe ou PAT (Personal Access Token) Docker
    - Les 4 variables d'environnement nécéssaires au projet, qui seront poussées sur Render pendant le workflow :
        - HOSTS
        - SECRET_KEY
        - SENTRY_DSN
        - SERVER_TYPE
