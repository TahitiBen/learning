# Fiche de cours — Séance 24 : SQL — `COUNT` (agrégations)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module SQL (4). Thème : compter et résumer des données.

---

## 1. Qu'est-ce qu'une agrégation

Une **fonction d'agrégation** calcule **une seule valeur** à partir de **plusieurs lignes** (compter, additionner, moyenner…). C'est ce qui transforme une table en **statistiques**.

## 2. `COUNT` : compter des lignes

```sql
SELECT COUNT(*) FROM machines;
```
→ le **nombre total** de lignes de la table.

Avec un `WHERE`, on compte seulement les lignes qui correspondent :
```sql
SELECT COUNT(*) FROM machines WHERE ip LIKE '192.168.1.%';
```
→ le **nombre de machines** sur le réseau 192.168.1. (C'est le `compteur` de l'audit Python, en une requête.)

## 3. Les autres agrégats (sur colonnes numériques)

| Fonction | Rôle |
|---|---|
| `COUNT(*)` | compter les lignes |
| `SUM(col)` | somme |
| `AVG(col)` | moyenne |
| `MIN(col)` | minimum |
| `MAX(col)` | maximum |

Exemple : `SELECT AVG(ram) FROM machines;` (moyenne d'une colonne `ram`).

## 4. Rappels qui reviennent (à ancrer)

- **`LIKE` a besoin du `%`** : `LIKE '192.168.5'` (sans joker) = `=` → ne matche rien ; il faut `LIKE '192.168.5.%'`.
- **Règle d'or** : `UPDATE`/`DELETE` **toujours** avec un `WHERE`, sinon toute la table est touchée.

---

## 5. Questions de révision (auto-test)

1. Qu'est-ce qu'une fonction d'agrégation ?
2. Que renvoie `SELECT COUNT(*) FROM machines;` ?
3. Écris une requête qui compte les machines du réseau `10.0.0`.
4. Quelle fonction pour la moyenne d'une colonne ? Pour la somme ?
5. Pourquoi `LIKE '192.168.5'` (sans `%`) ne renvoie-t-il rien sur des IP comme `192.168.5.0` ?
6. Cite les 5 fonctions d'agrégation vues.
7. `COUNT(*)` compte quoi exactement ?
8. Comment compter uniquement les lignes qui remplissent une condition ?
9. Règle d'or à ne jamais oublier avec `UPDATE`/`DELETE` ?
10. En quoi `COUNT(*) ... WHERE` ressemble-t-il au « compteur » d'un script ?

<details>
<summary>Réponses</summary>

1. Une fonction qui calcule une seule valeur à partir de plusieurs lignes (compter, sommer, moyenner…).
2. Le nombre total de lignes de la table `machines`.
3. `SELECT COUNT(*) FROM machines WHERE ip LIKE '10.0.0.%';`.
4. Moyenne = `AVG(col)` ; somme = `SUM(col)`.
5. Sans `%`, `LIKE` cherche une valeur exacte (comme `=`) ; « 192.168.5.0 » ≠ « 192.168.5 ».
6. `COUNT`, `SUM`, `AVG`, `MIN`, `MAX`.
7. Le nombre de lignes.
8. En ajoutant un `WHERE` : `SELECT COUNT(*) FROM table WHERE condition;`.
9. Toujours mettre un `WHERE` (sinon toute la table est modifiée/supprimée).
10. Il fait le comptage automatiquement, en une requête, au lieu d'une boucle + variable `+= 1`.

</details>
