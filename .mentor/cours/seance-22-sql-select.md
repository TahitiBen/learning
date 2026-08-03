# Fiche de cours — Séance 22 : SQL — `SELECT` (interroger)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module SQL (2). Thème : lire/filtrer des données — le cœur de SQL.

---

## 1. La forme générale

```sql
SELECT colonnes FROM table WHERE condition ORDER BY colonne;
```
`WHERE` et `ORDER BY` sont **optionnels**.

## 2. Choisir les colonnes

```sql
SELECT * FROM machines;        -- toutes les colonnes (* = tout)
SELECT nom, ip FROM machines;  -- seulement ces colonnes
```

## 3. Filtrer les lignes : `WHERE`

```sql
SELECT * FROM machines WHERE nom = 'Server-Web';
```
- Comparaison avec **un seul `=`** (en SQL, `=` compare ; pas de `==`).
- Texte entre **guillemets simples**.
- Autres opérateurs : `!=` (ou `<>`), `<`, `>`, `<=`, `>=`, et `AND` / `OR` pour combiner.

## 4. Filtrer par motif : `LIKE` et le joker `%`

```sql
SELECT * FROM machines WHERE ip LIKE '192.168.1.%';
```
- **`LIKE`** compare à un **motif**.
- **`%`** = joker : « n'importe quels caractères ».
- `'192.168.1.%'` = « commence par `192.168.1.` puis n'importe quoi ».
- Le **point** assure la précision (exclut `192.168.10.x`) — même logique que le filtre Python, mais en une ligne.

*(Autre joker : `_` = exactement un caractère.)*

## 5. Le lien avec ton audit Python

Tout ton outil d'audit (ouvrir le fichier, boucler, filtrer, compter) se résume, côté base de données, à :
```sql
SELECT * FROM machines WHERE ip LIKE '192.168.1.%';
```
On **décrit** ce qu'on veut, la base le trouve.

---

## 6. Questions de révision (auto-test)

1. Que veut dire `SELECT *` ?
2. Comment n'afficher que les colonnes `nom` et `ip` ?
3. Quel mot-clé filtre les lignes ?
4. En SQL, on compare avec `=` ou `==` ?
5. Que fait `LIKE` ? Que signifie `%` ?
6. Écris une requête qui renvoie les machines dont l'IP commence par `10.0.`.
7. Pourquoi met-on un point dans `'192.168.1.%'` ?
8. Écris une requête qui renvoie la machine nommée `PC de Caroline`.
9. `WHERE` et `ORDER BY` sont-ils obligatoires ?
10. Comment renvoyer TOUTES les lignes d'une table `users` ?

<details>
<summary>Réponses</summary>

1. Toutes les colonnes.
2. `SELECT nom, ip FROM machines;`.
3. `WHERE`.
4. `=` (un seul).
5. `LIKE` compare à un motif ; `%` = n'importe quels caractères (joker).
6. `SELECT * FROM machines WHERE ip LIKE '10.0.%';`.
7. Pour la précision : distinguer `192.168.1.x` de `192.168.10.x` (sinon on attraperait les deux).
8. `SELECT * FROM machines WHERE nom = 'PC de Caroline';`.
9. Non, ils sont optionnels.
10. `SELECT * FROM users;`.

</details>
