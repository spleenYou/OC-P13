## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/spleenYou/OC-P13.git`

#### Créer l'environnement virtuel

- `cd /path/to/OC-P13`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Variable d'environnement

Pour fonctionner, un fichier contenant des variables d'environnement est nécéssaire.

- `cd /path/to/OC-P13`
- `nano .env`
- Ecrire les variables suivantes :
  - SERVER_TYPE -> TEST ou PROD selon le type de serveur.
  - HOSTS -> Si vous êtes sur un serveur en production, indiquer les adresses de votre serveur entre guillements et séparés par une virgule.
  - SECRET_KEY -> Clé secrète pour la cryptographie de Django.
  - SENTRY_DSN -> le DSN donné par Sentry pour le suivi des logs.

Exemple de fichier .env : \
SERVER_TYPE=TEST \
HOSTS='127.0.0.1,localhost' \
SECRET_KEY=New_secret_key_de_folie#@=&4%=hp46(s \
SENTRY_DSN=https://517a76dae9a195---------------03e@o4509--------7232.ingest.de.sentry.io/4509---------160

#### Exécuter le site

- `cd /path/to/OC-P13`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
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
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Profiles_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Profiles_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`
