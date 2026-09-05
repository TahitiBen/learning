# Fiche de cours — Séance 32 : Capstone — gestionnaire d'inventaire (Python + SQLite)

> Support de révision (séance du 2026-09-04). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Projet de synthèse : une application CLI qui réunit Python + SQL + sécurité.

---

## 1. L'idée : une application pilotée par menu

Un programme qui tourne en boucle, propose des options, et appelle une **fonction** par option. Chaque fonction parle à la base via `sqlite3`.

## 2. Le code de référence

```python
import sqlite3

def lister():
    conn = sqlite3.connect("sql/machines.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM machines")
    for ligne in cur.fetchall():
        print(ligne)
    conn.close()

def ajouter():
    conn = sqlite3.connect("sql/machines.db")
    cur = conn.cursor()
    nom = input("Nom : ")
    ip = input("IP : ")
    reseau = input("Reseau : ")
    cur.execute("INSERT INTO machines (nom, ip, reseau) VALUES (?, ?, ?)", (nom, ip, reseau))
    conn.commit()          # ← sur la CONNEXION
    conn.close()
    print("Machine ajoutee !")

def rechercher():
    conn = sqlite3.connect("sql/machines.db")
    cur = conn.cursor()
    nom = input("Nom a rechercher : ")
    cur.execute("SELECT * FROM machines WHERE nom = ?", (nom,))
    for ligne in cur.fetchall():
        print(ligne)
    conn.close()

while True:
    print("1. Lister")
    print("2. Ajouter")
    print("3. Rechercher")
    print("4. Quitter")
    choix = input("Ton choix : ")
    if choix == "1":
        lister()
    elif choix == "2":
        ajouter()
    elif choix == "3":
        rechercher()
    elif choix == "4":
        break
    else:
        print("Choix invalide")
```

## 3. Ce que ce projet réunit
- **Structure** : `import` en haut → fonctions → boucle principale.
- **Contrôle** : `while True` + `if`/`elif`/`else` + `break`.
- **Base de données** : `sqlite3` (connect / cursor / execute / fetchall / commit / close).
- **Sécurité** : requêtes **paramétrées `?`** dès qu'il y a une donnée utilisateur (INSERT, recherche).

## 4. Pièges à retenir
- **`commit()` s'appelle sur la CONNEXION** (`conn.commit()`), pas sur le curseur.
- `connect` = **ouvrir** la base ; `execute` = **lancer** une requête.
- **Lister** = `SELECT *` (tout, sans input/WHERE) ; **Rechercher** = `WHERE nom = ?` (avec input).
- Pas de **code mort** (input inutilisé, etc.).

---

## 5. Questions de révision (auto-test)

1. Quelle structure fait tourner le menu en boucle et permet d'en sortir ?
2. Sur quel objet appelle-t-on `commit()` ?
3. Différence entre `lister()` et `rechercher()` en SQL ?
4. Pourquoi des `?` dans `ajouter()` et `rechercher()` ?
5. Que fait `connect` ? Que fait `execute` ?
6. Écris la requête paramétrée d'un INSERT à 3 valeurs.
7. Après un INSERT depuis Python, quoi faire pour que ça reste ?
8. Dans quel ordre organise-t-on le fichier ?
9. Que renvoie une recherche `WHERE nom = ?` si on tape `' OR '1'='1` ?
10. Cite 3 domaines que ce projet réunit.

<details>
<summary>Réponses</summary>

1. `while True:` + `break`.
2. La **connexion** (`conn.commit()`).
3. `lister()` = `SELECT *` (toutes les lignes) ; `rechercher()` = `SELECT ... WHERE nom = ?` (filtré par saisie).
4. Pour éviter l'injection SQL (données utilisateur traitées comme des valeurs, pas du SQL).
5. `connect` ouvre le fichier de base ; `execute` exécute une requête SQL.
6. `cur.execute("INSERT INTO machines (nom, ip, reseau) VALUES (?, ?, ?)", (nom, ip, reseau))`.
7. Appeler `conn.commit()`.
8. imports → fonctions → boucle principale.
9. 0 résultat (cherche une machine littéralement nommée ainsi).
10. Python (fonctions/boucles/conditions), SQL (base de données), sécurité (requêtes paramétrées).

</details>
