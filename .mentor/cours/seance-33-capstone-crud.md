# Fiche de cours — Séance 33 : Capstone CRUD complet (Modifier + Supprimer)

> Support de révision (séance du 2026-09-04). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Compléter le gestionnaire d'inventaire : les 5 opérations CRUD dans une app Python + SQLite.

---

## 1. Modifier (UPDATE) depuis Python

```python
def modifier():
    conn = sqlite3.connect("sql/machines.db")
    cur = conn.cursor()
    nom = input("Machine a modifier : ")
    ip = input("Nouvelle IP : ")
    cur.execute("UPDATE machines SET ip = ? WHERE nom = ?", (ip, nom))
    conn.commit()
    conn.close()
    print("Machine modifiee !")
```
⚠️ **Ordre des `?`** : les valeurs du tuple suivent l'ordre des `?` → ici `(ip, nom)` (le `?` du `SET` d'abord, celui du `WHERE` ensuite).

## 2. Supprimer (DELETE) depuis Python

```python
def supprimer():
    conn = sqlite3.connect("sql/machines.db")
    cur = conn.cursor()
    nom = input("Machine a supprimer : ")
    cur.execute("DELETE FROM machines WHERE nom = ?", (nom,))
    conn.commit()
    conn.close()
    print("Machine supprimee !")
```
⚠️ **Règle d'or** : toujours un `WHERE` (sinon on vide toute la table).

## 3. Le CRUD complet dans l'app
| Opération | Menu | SQL |
|---|---|---|
| **C**reate | Ajouter | `INSERT INTO ... VALUES (?, ?, ?)` |
| **R**ead | Lister / Rechercher | `SELECT *` / `SELECT ... WHERE nom = ?` |
| **U**pdate | Modifier | `UPDATE ... SET ip = ? WHERE nom = ?` |
| **D**elete | Supprimer | `DELETE FROM ... WHERE nom = ?` |

Toutes les opérations qui modifient la base → **`conn.commit()`** (sur la connexion, **avec les parenthèses**).

## 4. Pièges vus
- **`commit` sans parenthèses** (`conn.commit` ≠ `conn.commit()`) → la sauvegarde ne se fait pas. Une méthode s'appelle avec `()`.
- **Menu affiché ≠ logique** : penser à mettre à jour le **texte** du menu quand on ajoute des options.
- **Typo de variable** (`chox` vs `choix`) → `NameError`.

---

## 5. Questions de révision (auto-test)

1. Quelle requête pour modifier une valeur ? Pour supprimer une ligne ?
2. Dans `UPDATE ... SET ip = ? WHERE nom = ?`, quel est l'ordre des valeurs du tuple ?
3. Quelle règle d'or pour UPDATE et DELETE ?
4. Que se passe-t-il si on écrit `conn.commit` sans les parenthèses ?
5. Sur quel objet appelle-t-on `commit()` ?
6. Les 4 lettres du CRUD et leur commande SQL ?
7. Pourquoi des `?` dans modifier et supprimer ?
8. Écris un DELETE paramétré sur `nom`.
9. Quelle erreur si on tape `chox` au lieu de `choix` ?
10. Après un UPDATE depuis Python, quoi faire pour sauvegarder ?

<details>
<summary>Réponses</summary>

1. `UPDATE` (modifier) ; `DELETE` (supprimer).
2. L'ordre des `?` : d'abord la valeur du `SET` (ip), puis celle du `WHERE` (nom) → `(ip, nom)`.
3. Toujours un `WHERE` (sinon toute la table est touchée).
4. La méthode n'est pas appelée → la modification n'est **pas** sauvegardée.
5. La **connexion** (`conn.commit()`).
6. Create=`INSERT`, Read=`SELECT`, Update=`UPDATE`, Delete=`DELETE`.
7. Sécurité : éviter l'injection SQL (données utilisateur traitées comme valeurs).
8. `cur.execute("DELETE FROM machines WHERE nom = ?", (nom,))`.
9. `NameError` (variable `chox` non définie).
10. Appeler `conn.commit()`.

</details>
