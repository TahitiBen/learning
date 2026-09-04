# Fiche de cours — Séance 30 : écrire dans une base depuis Python (`sqlite3`)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Le pont Python↔SQL (2). Thème : modifier une base SQLite depuis un script, et lire des colonnes précises.

---

## 1. Accéder aux colonnes d'une ligne

Chaque ligne renvoyée par `fetchall()` est un **tuple** `(id, nom, ip, reseau)`. On pioche par index (comme une liste) :
```python
for ligne in curseur.fetchall():
    print(ligne[1], "->", ligne[2])   # nom -> ip
```
`ligne[0]` = id, `ligne[1]` = nom, `ligne[2]` = ip, `ligne[3]` = reseau.

## 2. Écrire : `execute(INSERT)` + `commit()`

```python
curseur.execute("INSERT INTO machines (nom, ip, reseau) VALUES ('Python-Test', '192.168.1.99', '192.168.1')")
conn.commit()     # ← SAUVEGARDE la modification (le "Ctrl+S" du code)
```
- Une requête qui **modifie** la base (`INSERT`, `UPDATE`, `DELETE`) doit être **validée** avec **`conn.commit()`**.
- Sans `commit()`, le changement est **perdu** à la fermeture.

## 3. ⭐ Connexion vs curseur : qui fait quoi

| Objet | Méthodes | Rôle |
|---|---|---|
| **Connexion** (`conn`) | `connect`, **`commit`**, `close` | gère la base dans son ensemble (transactions) |
| **Curseur** (`cursor`) | `execute`, `fetchall` | lance les requêtes, tient les résultats |

→ `commit()` s'appelle sur la **connexion**, pas sur le curseur (`conn.commit()`, pas `curseur.commit()`).

## 4. Rappels
- **Fermer DB Browser** avant de lancer un script qui écrit (verrou SQLite → « database is locked »).
- Attention à ne pas relancer un script d'INSERT en boucle (sinon **doublons**).

---

## 5. Questions de révision (auto-test)

1. Sous quelle forme `fetchall()` renvoie-t-il chaque ligne ?
2. Comment récupérer l'ip (3e colonne) d'une ligne `ligne` ?
3. Quelle méthode faut-il appeler après un `INSERT` pour sauvegarder ?
4. Sur quel objet appelle-t-on `commit()` : la connexion ou le curseur ?
5. Que se passe-t-il si on oublie `commit()` après un `INSERT` ?
6. Quelles méthodes appartiennent au **curseur** ?
7. Quelles méthodes appartiennent à la **connexion** ?
8. Pourquoi fermer DB Browser avant un script qui écrit ?
9. Écris la ligne Python qui insère une ligne dans `machines`.
10. À quoi correspond `ligne[0]` ?

<details>
<summary>Réponses</summary>

1. Un **tuple**.
2. `ligne[2]`.
3. `commit()`.
4. La **connexion** (`conn.commit()`).
5. La modification est **perdue** (non enregistrée dans le fichier).
6. `execute`, `fetchall`.
7. `connect`, `commit`, `close`.
8. Parce que SQLite n'autorise qu'un écrivain à la fois ; DB Browser verrouille le fichier (« database is locked »).
9. `curseur.execute("INSERT INTO machines (nom, ip, reseau) VALUES ('X', 'Y', 'Z')")` puis `conn.commit()`.
10. À l'`id` (la 1re colonne).

</details>
