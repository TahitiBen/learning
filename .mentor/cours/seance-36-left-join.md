# Fiche de cours — Séance 36 : SQL — `LEFT JOIN`

> Support de révision (séance du 2026-09-04). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module SQL. Thème : garder toutes les lignes d'une table dans une jointure.

---

## 1. Rappel : `INNER JOIN` (le `JOIN` simple)

Ne renvoie que les lignes qui ont une **correspondance dans les DEUX tables**.
```sql
SELECT machines.nom, reseaux.localisation
FROM machines
JOIN reseaux ON machines.reseau = reseaux.reseau;
```
→ une machine dont le `reseau` n'est **pas** dans `reseaux` est **exclue**.

## 2. `LEFT JOIN`

Renvoie **TOUTES les lignes de la table de GAUCHE** (celle après `FROM`), même sans correspondance à droite. Les colonnes de droite manquantes valent **`NULL`**.
```sql
SELECT machines.nom, reseaux.localisation
FROM machines
LEFT JOIN reseaux ON machines.reseau = reseaux.reseau;
```
→ toutes les machines s'affichent ; celles sans réseau documenté ont `localisation = NULL`.

## 3. Quand l'utiliser
- « Liste **tout** X, avec l'info de Y **si elle existe** ».
- Repérer les **trous** : les lignes de gauche **sans** correspondance à droite (localisation NULL = réseau non documenté).

## 4. Exemple vu en cours
Machine `Orpheline` sur `172.16.0` (réseau absent de `reseaux`) :
- INNER JOIN → 6 lignes (Orpheline **absente**).
- LEFT JOIN → 7 lignes (Orpheline **présente**, `localisation = NULL`).

## 5. Rappel-clé
La condition d'une jointure va dans **`ON`** (pas `WHERE`) : `JOIN ... ON t1.cle = t2.cle`.

---

## 6. Questions de révision (auto-test)

1. Que renvoie un `INNER JOIN` (le `JOIN` simple) ?
2. Que renvoie un `LEFT JOIN` en plus ?
3. Quelle valeur prennent les colonnes de droite sans correspondance ?
4. Quelle est la table « de gauche » dans `FROM machines LEFT JOIN reseaux` ?
5. Dans quelle clause écrit-on la condition de jointure ?
6. Écris un LEFT JOIN affichant `machines.nom` et `reseaux.localisation`.
7. Une machine sur un réseau absent de `reseaux` : apparaît-elle en INNER JOIN ? en LEFT JOIN ?
8. À quoi sert concrètement un LEFT JOIN (repérage) ?
9. `NULL`, ça veut dire quoi ?
10. Différence de nombre de lignes entre INNER et LEFT dans l'exemple ?

<details>
<summary>Réponses</summary>

1. Seulement les lignes ayant une correspondance dans les deux tables.
2. Aussi les lignes de la table de gauche **sans** correspondance à droite.
3. `NULL` (vide).
4. `machines` (la table après `FROM`).
5. Dans `ON` (`JOIN ... ON ...`).
6. `SELECT machines.nom, reseaux.localisation FROM machines LEFT JOIN reseaux ON machines.reseau = reseaux.reseau;`.
7. INNER JOIN : non ; LEFT JOIN : oui (avec `NULL`).
8. À lister tout en gardant les lignes non appariées → repérer les données manquantes/non documentées.
9. L'absence de valeur (vide).
10. INNER = 6, LEFT = 7 (la machine orpheline en plus).

</details>
