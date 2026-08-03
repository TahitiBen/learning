# Fiche de cours — Séance 23 : SQL — `ORDER BY`, `UPDATE`, `DELETE` (CRUD complet)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module SQL (3). Thème : trier, modifier, supprimer — et la règle de sécurité du `WHERE`.

---

## 1. Le CRUD : les 4 opérations de base

| Lettre | Sens | Commande SQL |
|---|---|---|
| **C** | Create (créer) | `INSERT INTO` |
| **R** | Read (lire) | `SELECT` |
| **U** | Update (modifier) | `UPDATE` |
| **D** | Delete (supprimer) | `DELETE` |

## 2. Trier : `ORDER BY`

```sql
SELECT * FROM machines ORDER BY nom;        -- A → Z (par défaut = ASC)
SELECT * FROM machines ORDER BY nom DESC;   -- Z → A
SELECT * FROM machines ORDER BY id DESC;    -- du plus récent au plus ancien
```

## 3. Modifier : `UPDATE`

```sql
UPDATE machines SET ip = '192.168.1.10' WHERE nom = 'Server-Web';
```
Forme : `UPDATE table SET colonne = nouvelle_valeur WHERE condition`. On peut modifier plusieurs colonnes : `SET nom = '...', ip = '...'`.

## 4. Supprimer : `DELETE`

```sql
DELETE FROM machines WHERE nom = 'Test';
```
Forme : `DELETE FROM table WHERE condition`.

## 5. ⚠️⚠️ LA règle d'or : toujours un `WHERE`

Sans `WHERE`, `UPDATE` et `DELETE` s'appliquent à **TOUTES les lignes** :
- `UPDATE machines SET ip = '0.0.0.0';` → écrase **toutes** les IP.
- `DELETE FROM machines;` → **vide toute la table**.

Réflexe de survie : **avant tout `UPDATE`/`DELETE`, vérifier la présence d'un `WHERE`**. Astuce pro : tester d'abord la condition avec un `SELECT ... WHERE ...` pour voir **quelles lignes** seraient touchées.

---

## 6. Questions de révision (auto-test)

1. Que veut dire CRUD, et quelle commande SQL pour chaque lettre ?
2. Comment trier les résultats de Z à A ?
3. Écris une requête qui change l'IP de `PC de Caroline` en `192.168.10.5`.
4. Écris une requête qui supprime la machine `Imprimante du bureau`.
5. Que se passe-t-il si on fait `DELETE FROM machines;` (sans WHERE) ?
6. Que se passe-t-il si on fait `UPDATE machines SET ip = '0.0.0.0';` (sans WHERE) ?
7. Quelle astuce pour vérifier ce qu'un UPDATE/DELETE va toucher avant de le lancer ?
8. Peut-on modifier deux colonnes dans un seul `UPDATE` ?
9. Quel mot-clé pour trier ? Quel suffixe pour l'ordre décroissant ?
10. Dans quelle commande le `WHERE` est-il le plus « dangereux » d'oublier ?

<details>
<summary>Réponses</summary>

1. Create=`INSERT`, Read=`SELECT`, Update=`UPDATE`, Delete=`DELETE`.
2. `ORDER BY colonne DESC`.
3. `UPDATE machines SET ip = '192.168.10.5' WHERE nom = 'PC de Caroline';`.
4. `DELETE FROM machines WHERE nom = 'Imprimante du bureau';`.
5. Toute la table est vidée (toutes les lignes supprimées).
6. Toutes les machines reçoivent l'IP `0.0.0.0` (toutes les lignes modifiées).
7. Lancer d'abord un `SELECT ... WHERE ...` avec la même condition pour voir les lignes concernées.
8. Oui : `SET col1 = ..., col2 = ...`.
9. `ORDER BY` ; suffixe `DESC`.
10. `UPDATE` et `DELETE` (elles modifient/suppriment les données).

</details>
