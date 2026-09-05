# Fiche de cours — Séance 34 : robustesse & messages de feedback (sqlite3)

> Support de révision (séance du 2026-09-04). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Rendre une app SQLite « pro » : ne jamais rester muet.

---

## 1. Recherche vide → message

On **stocke** le résultat de `fetchall()`, puis on teste s'il est vide :
```python
resultats = cur.fetchall()
if not resultats:                  # liste vide = rien trouvé
    print("Aucune machine trouvee.")
else:
    for ligne in resultats:
        print(ligne)
```
- `if not resultats:` est vrai quand la liste est **vide** (`[]`).

## 2. UPDATE/DELETE sans effet → message, via `cur.rowcount`

`cur.rowcount` = le **nombre de lignes affectées** par la dernière requête.
```python
cur.execute("DELETE FROM machines WHERE nom = ?", (nom,))
conn.commit()
if cur.rowcount == 0:
    print("Aucune machine a ce nom.")   # rien n'a matché
else:
    print("Machine supprimee !")
```
Idem pour `UPDATE` (0 = aucune ligne modifiée).

## 3. Rappel : `DELETE`/`UPDATE` ne prennent pas de `*`
- `SELECT *` → choisir des colonnes.
- `DELETE FROM table WHERE ...` → supprime des **lignes** (pas de `*`).
- `UPDATE table SET col = ... WHERE ...` → modifie des colonnes via `SET` (pas de `*`).

---

## 4. Questions de révision (auto-test)

1. Comment détecter qu'une recherche n'a rien renvoyé ?
2. Que vaut `if not resultats:` quand la liste est vide ?
3. Que donne `cur.rowcount` après un DELETE ?
4. Comment savoir qu'un DELETE n'a supprimé aucune ligne ?
5. Pourquoi stocker `fetchall()` dans une variable ?
6. `DELETE` prend-il un `*` ?
7. Écris le test qui affiche « rien trouvé » si `resultats` est vide.
8. Après un UPDATE, comment savoir si une ligne a été modifiée ?
9. Quelle commande utilise `*` : SELECT, DELETE ou UPDATE ?
10. Pourquoi ces messages rendent l'outil « pro » ?

<details>
<summary>Réponses</summary>

1. En stockant `fetchall()` et en testant si la liste est vide.
2. `True` (une liste vide est « fausse », donc `not []` = vrai).
3. Le nombre de lignes supprimées.
4. `cur.rowcount == 0`.
5. Pour pouvoir tester si elle est vide ET la parcourir (on ne relit pas `fetchall()` deux fois).
6. Non.
7. `if not resultats: print("rien trouve")`.
8. `cur.rowcount` (0 = aucune modifiée).
9. `SELECT`.
10. Il ne reste jamais muet : l'utilisateur sait toujours ce qui s'est passé (cas limites gérés).

</details>
