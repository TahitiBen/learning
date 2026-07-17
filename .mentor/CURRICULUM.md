# CURRICULUM — Parcours de Ruben

> Plan de formation adapté à un profil **SISR** qui veut coder pour l'**automatisation système & réseau**, apprend **en pratiquant**, ~1 h/semaine.
> Priorité : **Python** (automatisation/infra) → **SQL** → **JS/TS** (plus léger). Fil rouge système & réseau.
> Coche les cases au fur et à mesure. Ce plan s'adapte au rythme réel — il n'est pas gravé dans le marbre.

---

## Phase 0 — Environnement & git *(en cours)*

- [x] Vérifier les outils (`git --version`)
- [x] Cloner le repo dans `learning`
- [x] Créer la structure de dossiers (langages + `.mentor` + `.claude`)
- [x] Comprendre `.gitkeep` et les dossiers vides
- [x] Installer le skill `prof-dev` (`SKILL.md`)
- [ ] Premier `git add` / `commit` / `push`
- [ ] Convention de message de commit
- [ ] `README.md` à la racine

**Transversal (toutes les séances) :** terminal, git, bonnes habitudes de ligne de commande.

---

## Phase 1 — Python : les fondamentaux

- [ ] `print`, exécuter un script (`python fichier.py`)
- [ ] Variables et types de base (`int`, `float`, `str`, `bool`)
- [ ] Entrées utilisateur (`input`) et conversions de type
- [ ] Opérateurs (arithmétiques, comparaison, logiques)
- [ ] Conditions (`if` / `elif` / `else`)
- [ ] Boucles (`while`, `for`, `range`)
- [ ] Listes (`list`) : créer, parcourir, modifier
- [ ] Dictionnaires (`dict`) : clés/valeurs
- [ ] Fonctions (`def`, paramètres, `return`)
- [ ] Gestion d'erreurs de base (`try` / `except`)
- [ ] **Mini-projet :** un petit outil en ligne de commande (ex. calculateur de sous-réseau simple, ou convertisseur d'unités)

---

## Phase 2 — Python : intermédiaire

- [ ] Chaînes de caractères avancées (méthodes, formatage `f-string`)
- [ ] Compréhensions de listes / dicts
- [ ] Lire et écrire des fichiers (`open`, `pathlib`)
- [ ] Modules et imports (`import`, organiser son code)
- [ ] `pip`, environnements virtuels (`venv`)
- [ ] Introduction à la POO (classes, objets, méthodes) — léger
- [ ] **Mini-projet :** parser un fichier de logs et en extraire des stats

---

## Phase 3 — Python pour l'automatisation système & réseau *(le cœur de ton orientation)*

- [ ] `os`, `sys`, `pathlib` : manipuler fichiers et dossiers
- [ ] `subprocess` : lancer des commandes système depuis Python
- [ ] `argparse` : faire de vrais outils en ligne de commande
- [ ] Dates et logs (`datetime`, logging)
- [ ] Requêtes réseau / API avec `requests` (récupérer de la donnée)
- [ ] Traiter du JSON
- [ ] **Mini-projet :** script d'inventaire (machines/services) ou de supervision simple
- [ ] Comparaison Python ↔ PowerShell/Bash sur une même tâche

---

## Phase 4 — SQL (avec SQLite, zéro installation serveur)

- [ ] Modéliser : tables, colonnes, types, clés primaires
- [ ] `CREATE TABLE`, `INSERT`
- [ ] `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`
- [ ] `UPDATE`, `DELETE`
- [ ] Fonctions d'agrégation (`COUNT`, `SUM`, `AVG`, `GROUP BY`)
- [ ] Jointures (`JOIN`)
- [ ] Index (et pourquoi ça accélère)
- [ ] **Mini-projet :** stocker les données du script d'inventaire (Phase 3) dans une base SQLite et l'interroger

---

## Phase 5 — JavaScript : fondamentaux *(plus léger)*

- [ ] Variables (`let`, `const`), types
- [ ] Conditions, boucles, fonctions (comparer avec Python)
- [ ] Tableaux et objets
- [ ] Méthodes de tableaux (`map`, `filter`, `forEach`)
- [ ] Notions d'asynchrone (`promise`, `async` / `await`) — introduction
- [ ] Exécuter du JS avec Node.js

---

## Phase 6 — TypeScript *(une fois JS à l'aise)*

- [ ] Pourquoi typer ? types de base
- [ ] Interfaces et types personnalisés
- [ ] Configuration d'un projet TS

---

## Phase 7 — Projets intégrateurs *(orientés infra/DevOps)*

- [ ] Choisir un projet ensemble mêlant plusieurs briques (ex. : outil qui collecte des infos réseau en Python → stocke en SQL → petite interface web)
- [ ] Découverte des pistes d'orientation : DevOps, SRE, automatisation, cloud
- [ ] Bilan : vers quelle spécialité Ruben veut aller

---

## Idées d'orientation à explorer en chemin
DevOps / SRE, automatisation d'infra (Infrastructure as Code), scripting réseau, cloud (Azure/AWS), cybersécurité défensive. On affinera selon ce qui te plaît **en pratiquant**.
