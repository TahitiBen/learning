# Gestionnaire d'inventaire réseau

Outil en ligne de commande pour gérer un inventaire de machines dans une base de données SQLite.

## Fonctionnalités
- Lister les machines
- Ajouter une machine
- Rechercher une machine par nom
- Modifier l'adresse IP d'une machine
- Supprimer une machine

## Technologies
- Python 3
- SQLite (module `sqlite3`)

## Sécurité & robustesse
- Requêtes paramétrées (protection contre les injections SQL)
- Gestion des erreurs de base de données (`try` / `except`)
- Messages clairs si aucune machine n'est trouvée / modifiée / supprimée

## Utilisation
1. Avoir la base `machines.db` (tables `machines` et `reseaux`).
2. Lancer : `python inventaire_manager.py`
3. Choisir une option du menu (1 à 6).

## Ce que ce projet m'a appris
Ce projet m'a permis d'approfondir Python et SQL, et surtout de comprendre comment les **relier** : comment, depuis Python, on se connecte à une base et on l'exploite concrètement (lecture, écriture, recherche). J'y ai aussi appris à **sécuriser mes requêtes** contre les injections SQL (requêtes paramétrées) et à **gérer proprement les erreurs** avec `try`/`except`.