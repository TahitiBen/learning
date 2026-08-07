# Fiche de cours — Séance 25 : SQL — `GROUP BY` (& `ALTER TABLE`)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module SQL (5). Thème : agréger par groupe pour obtenir des récapitulatifs.

---

## 1. `ALTER TABLE` : modifier la structure d'une table

```sql
ALTER TABLE machines ADD COLUMN reseau TEXT;
```
- Ajoute une **colonne** à une table déjà existante.
- Les lignes existantes ont la nouvelle colonne à `NULL` (vide) tant qu'on ne la remplit pas.
- On la remplit ensuite avec `UPDATE` :
  ```sql
  UPDATE machines SET reseau = '192.168.1' WHERE ip LIKE '192.168.1.%';
  ```

## 2. `GROUP BY` : agréger par groupe

`COUNT(*)` seul donne **un** total. `GROUP BY` donne un total **par catégorie**.

```sql
SELECT reseau, COUNT(*) FROM machines GROUP BY reseau;
```
- `GROUP BY reseau` **regroupe** les lignes qui ont la même valeur de `reseau`.
- L'agrégat (`COUNT(*)`) est calculé **pour chaque groupe** → **une ligne de résultat par groupe**.

Résultat (exemple) :
| reseau | COUNT(*) |
|---|---|
| 192.168.1 | 3 |
| 192.168.10 | 1 |
| 192.168.5 | 1 |

Règle : les colonnes du `SELECT` doivent être soit la colonne de regroupement, soit un agrégat.

On peut combiner avec d'autres agrégats : `SELECT reseau, COUNT(*), MAX(ip) FROM machines GROUP BY reseau;`.

## 3. À quoi ça sert (infra)
Récapitulatifs instantanés : nombre de machines **par réseau**, nombre d'erreurs **par type** dans des logs, etc. C'est le cœur du **reporting** et de la **supervision**.

---

## 4. Questions de révision (auto-test)

1. À quoi sert `ALTER TABLE ... ADD COLUMN` ?
2. Que valent les lignes existantes dans la nouvelle colonne, avant qu'on la remplisse ?
3. Quelle commande pour remplir la colonne ajoutée ?
4. Quelle est la différence entre `COUNT(*)` seul et `COUNT(*)` avec `GROUP BY` ?
5. Écris une requête qui compte les machines **par réseau**.
6. Combien de lignes renvoie un `GROUP BY reseau` s'il y a 3 réseaux distincts ?
7. Dans un `SELECT ... GROUP BY col`, que peut-on mettre dans le SELECT ?
8. Écris une requête qui, pour chaque réseau, donne le nombre de machines ET l'IP max.
9. Donne un cas d'usage infra concret du `GROUP BY`.
10. `GROUP BY` regroupe selon quoi ?

<details>
<summary>Réponses</summary>

1. À ajouter (ou modifier) une colonne dans une table existante.
2. `NULL` (vide) tant qu'on ne les remplit pas.
3. `UPDATE ... SET colonne = ... WHERE ...`.
4. `COUNT(*)` seul = un total global ; avec `GROUP BY` = un total par groupe (une ligne par valeur distincte).
5. `SELECT reseau, COUNT(*) FROM machines GROUP BY reseau;`.
6. 3 lignes (une par réseau distinct).
7. La (les) colonne(s) de regroupement et/ou des fonctions d'agrégat.
8. `SELECT reseau, COUNT(*), MAX(ip) FROM machines GROUP BY reseau;`.
9. Ex. : nombre de machines par réseau, nombre d'erreurs par type dans un log (reporting/supervision).
10. Selon la (les) valeur(s) de la colonne indiquée après `GROUP BY`.

</details>
