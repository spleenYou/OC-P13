Installation
============

L'installation peut se faire de deux manières distinctes, en copiant le répertoire Github ou en utilisant l'image Docker. 

Via Gihub
---------

#. Mettez vous dans le répertoire qui accueillera le projet.
#. Ouvrir un terminal
#. Cloner le répertoire Github ``git clone https://github.com/spleenYou/OC-P13.git``
#. Aller dans le répertoire créer ``cd OC-P13``
#. Créer un environnement virtuel ``python3 -m venv venv``
#. Activer l'environnement virtuel ``source venv/bin/activate`` (Linux) ou ``.\venv\Scripts\Activate.ps1`` (Windows)
#. Installation des packages ``pip install -r requirements.txt``


Via Docker
----------

#. Aller sur `Docker <URL_Docker_>`__
#. Créer un compte si besoin
#. Installer `Docker Desktop <URL_Docker_Desktop_>`__ selon votre système d'exploitation
#. Vérifier que Docker Desktop est lancé
#. Ouvrir un terminal
#. Récupérer l'image ``docker pull spleen85/oc-p13:latest``

.. _URL_Docker: https://www.docker.com/
.. _URL_Docker_Desktop: https://docs.docker.com/get-started/get-docker/