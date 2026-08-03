# Fiche de cours — Séance 21 : SQL — bases, `CREATE TABLE`, `INSERT`

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module SQL (1). Thème : créer une base, une table, y insérer des données.

---

## 1. Vocabulaire des bases de données

- **Base de données** (*database*) : l'ensemble ; en SQLite = **un seul fichier** (`machines.db`).
- **Table** : un tableau de données (ex. `machines`). Comme une feuille Excel.
- **Colonnes** : les champs (ex. `id`, `nom`, `ip`) — chacune a un **type**.
- **Lignes** (*rows*) : les enregistrements (une machine = une ligne).

## 2. Serveur vs sans serveur

- **MySQL / MariaDB** (ex. via Laragon) : base **serveur** — un programme tourne en fond, on s'y connecte (phpMyAdmin…). Données dans le dossier data du serveur.
- **SQLite** : base **sans serveur** — toute la base tient dans **un fichier** ouvrable directement. Idéal pour apprendre. Le **langage SQL est quasi identique** entre les deux.

## 3. `CREATE TABLE` — définir la structure (une seule fois)

```sql
CREATE TABLE machines (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    ip TEXT
);
```
- Chaque colonne : un **nom** + un **type** (`INTEGER` = entier, `TEXT` = texte, aussi `REAL` = décimal).
- **`PRIMARY KEY`** : identifiant **unique** de chaque ligne. `INTEGER PRIMARY KEY` en SQLite se **remplit automatiquement** (1, 2, 3…).
- ⚠️ On crée une table **une seule fois**. La relancer donne l'erreur *« table already exists »*.

## 4. `INSERT INTO` — ajouter des données (autant qu'on veut)

```sql
INSERT INTO machines (nom, ip) VALUES ('Server-Web', '192.168.1.0');
```
- On liste les **colonnes** qu'on remplit, puis les **valeurs** correspondantes.
- ⚠️ En SQL, le **texte** se met entre **guillemets simples** `'...'` (pas doubles).
- On ne remplit pas `id` : il est auto-généré.

## 5. Enregistrer / voir (dans DB Browser)

- **Enregistrer les modifications** (Ctrl+S) : écrit vraiment les changements dans le fichier `.db` (avant, ils sont « en attente », comme un commit non fait).
- Onglet **Parcourir les données** : voir le contenu d'une table visuellement.
- **Exécuter le SQL** : F5 (tout) ; on peut aussi **surligner** une portion pour n'exécuter qu'elle.

---

## 6. Questions de révision (auto-test)

1. En SQLite, une base de données, c'est quoi physiquement ?
2. Différence entre une base « serveur » (MySQL) et « sans serveur » (SQLite) ?
3. À quoi sert `CREATE TABLE` ? Combien de fois l'exécute-t-on ?
4. Que fait `PRIMARY KEY` ? Faut-il remplir `id` à la main en SQLite ?
5. Écris une commande qui crée une table `users` avec `id`, `nom`, `email`.
6. Quelle commande ajoute une ligne dans une table ?
7. Texte en SQL : guillemets simples ou doubles ?
8. Que signifie l'erreur « table already exists » ?
9. Dans DB Browser, à quoi sert « Enregistrer les modifications » ?
10. Cite deux types de colonnes SQLite.

<details>
<summary>Réponses</summary>

1. Un seul fichier (ex. `machines.db`).
2. Serveur = un programme tourne en fond, on s'y connecte ; sans serveur = tout dans un fichier ouvert directement.
3. À définir la structure d'une table (colonnes + types) ; on l'exécute **une seule fois**.
4. Identifiant unique de chaque ligne ; non, `INTEGER PRIMARY KEY` s'auto-remplit en SQLite.
5. `CREATE TABLE users (id INTEGER PRIMARY KEY, nom TEXT, email TEXT);`.
6. `INSERT INTO ...`.
7. Guillemets **simples** (`'...'`).
8. Que la table existe déjà (on a relancé un `CREATE TABLE` sur une table déjà créée).
9. À écrire réellement les changements dans le fichier `.db` (persister).
10. `INTEGER`, `TEXT` (et `REAL`).

</details>
