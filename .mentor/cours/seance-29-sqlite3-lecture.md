# Fiche de cours — Séance 29 : exécuter du SQL depuis Python (`sqlite3`, lecture)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Le pont entre Python et SQL. Thème : lire une base SQLite depuis un script Python.

---

## 1. Le module `sqlite3`

Python inclut **`sqlite3`** pour parler à une base SQLite **par du code** (sans DB Browser). Le schéma est toujours le même :

```python
import sqlite3

conn = sqlite3.connect("sql/machines.db")   # 1. se connecter au fichier de base
curseur = conn.cursor()                      # 2. créer un curseur

curseur.execute("SELECT * FROM machines")    # 3. exécuter une requête (chaîne SQL)
for ligne in curseur.fetchall():             # 4. récupérer + parcourir les résultats
    print(ligne)

conn.close()                                 # 5. fermer la connexion
```

## 2. Rôle de chaque étape

| Étape | Rôle |
|---|---|
| `sqlite3.connect("fichier.db")` | ouvre le **fichier** de base, renvoie une **connexion** |
| `conn.cursor()` | crée un **curseur** : l'objet qui lance les requêtes et tient les résultats |
| `curseur.execute("SQL")` | exécute une requête SQL, écrite comme une **chaîne** Python |
| `curseur.fetchall()` | renvoie **toutes les lignes** du résultat |
| `conn.close()` | ferme proprement la connexion |

Les **noms** des variables sont libres (`conn`/`curseur` sont des conventions) — ce sont des **objets** avec un rôle.

## 3. Forme des résultats

Chaque ligne renvoyée est un **tuple** :
```
(1, 'Server-Web', '192.168.1.0', '192.168.1')
```
On accède aux champs par index (comme une liste) : `ligne[0]` = id, `ligne[1]` = nom, `ligne[2]` = ip…

## 4. ⚠️ Verrou : fermer DB Browser

Une base SQLite = **un fichier**. SQLite n'autorise qu'**un seul écrivain à la fois**. Si DB Browser tient la base ouverte (surtout avec des modifs non enregistrées), un script Python qui écrit peut planter avec **« database is locked »**. → **fermer DB Browser** avant de lancer les scripts (surtout ceux qui écrivent).

---

## 5. Questions de révision (auto-test)

1. Quel module Python pour parler à une base SQLite ?
2. Quelle fonction ouvre la base ? Que prend-elle en argument ?
3. À quoi sert le curseur ?
4. Comment exécute-t-on une requête SQL depuis Python ?
5. Que renvoie `fetchall()` ?
6. Sous quelle forme est chaque ligne renvoyée ?
7. Comment récupérer le nom (2e colonne) d'une ligne `ligne` ?
8. Pourquoi faut-il fermer DB Browser avant de lancer un script qui écrit ?
9. Faut-il garder les noms `conn` et `curseur` ?
10. Écris les 2 lignes qui se connectent à `data.db` et créent un curseur.

<details>
<summary>Réponses</summary>

1. `sqlite3`.
2. `sqlite3.connect(...)` ; elle prend le **chemin du fichier** `.db`.
3. À exécuter les requêtes et tenir les résultats.
4. `curseur.execute("...requête SQL...")`.
5. Toutes les lignes du résultat (une liste de tuples).
6. Un **tuple** (ex. `(1, 'Server-Web', '192.168.1.0', '192.168.1')`).
7. `ligne[1]` (l'index commence à 0).
8. Parce que SQLite n'autorise qu'un seul écrivain ; DB Browser peut verrouiller le fichier (« database is locked »).
9. Non, les noms sont libres ; ce sont juste des objets (connexion, curseur).
10. `conn = sqlite3.connect("data.db")` puis `curseur = conn.cursor()`.

</details>
