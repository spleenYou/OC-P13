Démarrage rapide
================

Avant le démarrage, il faut vérifier le pré-requis et configurer les variables d'environnement, sinon le projet ne fonctionnera pas.

Pré-requis
----------

Sentry
~~~~~~

Le projet utilise `Sentry <URL_Sentry_>`_ pour le suivi des exceptions et des erreurs.

.. _URL_Sentry: https://sentry.io/

Si vous n'avez pas créer de projet sur Sentry :

#. Aller sur `Sentry <URL_Sentry_>`_
#. Créer un compte si besoin
#. Cliquer sur 'Créer un projet'
#. Choisir les éléments suivants :

    #. Plateforme : Django
    #. Règler la fréquence des alertes selon vos préférences
    #. Donner un nom à votre projet
#. Dans `Configure SDK`, copier le dsn indiqué (exemple: https://176...63e@o450...732.ingest.de.sentry.io/450...160)

le DSN est également dans les paramêtres du projet/SDK Setup/Clés clients(DSN).

Clé secrète
~~~~~~~~~~~

Django utilise une clé secrète pour la signature cryptographique des données.

Si vous n'avez pas définit de clé secrète, il est existe un `générateur <URL_DJECRETY_>`_ pour cela

.. _URL_DJECRETY: https://djecrety.ir

Variables d'environnement
-------------------------

Voici les variables d'environnement dont le projet à besoin :

=========== ============================================= ==========================================================
Variable    Description                                   Exemple
=========== ============================================= ==========================================================
SERVER_TYPE Définit le type de serveur                    ``TEST`` ou ``PROD``
HOSTS       Adresses du serveur (PROD)                    localhost,127.0.0.1
SECRET_KEY  Clé utilisée par Django pour la cryptographie SuperCleSecrete123456789ABCDEF
SENTRY_DSN  DSN fourni par Sentry pour le suivi des logs  https://176...63e@o450...732.ingest.de.sentry.io/450...160
=========== ============================================= ==========================================================

Lancement du projet
-------------------

- Si vous utilisez le répertoire Github, ouvrez le terminal (s'assurer d'être dans l'environnement virtuel) et rentrez les variables d'environnement :

    - ``export SERVER_TYPE=TEST``
    - ``export HOSTS=localhost,127.0.0.1``
    - ``export SECRET_KEY=SuperCleSecrete12345``
    - ``export SENTRY_DSN=https://176...63e@o450...732.ingest.de.sentry.io/450...160``

    Puis lancer le projet : ``python manage.py runserver``


- Si vous utilisez l'image Docker :

    - soit vous mettez les variables dans un fichier (ex: .env) et vous entrer ``docker run --env-file .env -d -p 8000:8000 spleen85/oc-p13:latest``
    - soit vous entrer directement : ``docker run -e SERVER_TYPE=TEST -e HOSTS=localhost,127.0.0.1 -e SECRET_KEY=SuperCleSecrete12345 -e SENTRY_DSN=https://176...63e@o450...732.ingest.de.sentry.io/450...160 -d -p 8000:8000 spleen85/oc-p13:latest``

Le projet est accessible à l'adresse http://localhost:8000/