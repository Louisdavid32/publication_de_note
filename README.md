# Application de gestion des notes des étudiants

Ce projet est une application web développée avec Django qui permet de gérer les notes des étudiants dans un environnement universitaire. L'application prend en compte les niveaux, les filières, les unités d'enseignement (UE), les matières (EC), les contrôles continus (CC) et les sessions d'examens.

## Fonctionnalités

*   Gestion des étudiants (ajout, modification, suppression)
*   Gestion des niveaux, des filières, des UE et des EC
*   Saisie des notes des étudiants pour chaque EC
*   Calcul automatique de la moyenne des étudiants
*   Import/export de données Excel

## Installation

1.  Cloner le dépôt : `git clone https://github.com/Louisdavid32/publication_de_note/.git`
2.  Créer un environnement virtuel : `python3 -m venv .env`
3.  Activer l'environnement virtuel : `source .env/bin/activate`
4.  Migrer la base de données : `python manage.py migrate`
5.  Créer un superutilisateur : `python manage.py createsuperuser`
6.  Lancer le serveur de développement : `python manage.py runserver`

## Utilisation

1.  Se connecter à l'application avec le superutilisateur créé.
2.  Ajouter les niveaux, les filières, les UE et les EC via l'interface d'administration.
3.  Importer les données des étudiants depuis un fichier Excel.
4.  Saisir les notes des étudiants.
5.  Consulter les notes et les moyennes des étudiants.

## Contribution

Toute contribution est la bienvenue. Veuillez consulter le fichier CONTRIBUTING.md pour plus d'informations.

## Licence

Ce projet est sous licence MIT.# publication_de_note
Application web Django pour la gestion des notes des étudiants dans un environnement universitaire.
