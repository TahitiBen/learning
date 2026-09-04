# Fiche de cours — Séance 28 : SQL — les jointures (`JOIN`)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module SQL (6). Thème : croiser deux tables — le cœur du modèle relationnel.

---

## 1. Pourquoi les jointures

Le principe du **relationnel** : ne pas répéter une information. Au lieu d'écrire la localisation d'un réseau dans **chaque** machine, on la met **une seule fois** dans une table à part, et on **relie** les tables au moment de la requête.

- `machines` : `nom`, `ip`, `reseau` (ex. `192.168.1`)
- `reseaux` : `reseau` (ex. `192.168.1`), `localisation` (ex. `Bureau`)
- Le **lien** : `machines.reseau` = `reseaux.reseau`.

## 2. La syntaxe `JOIN ... ON`

```sql
SELECT machines.nom, machines.ip, reseaux.localisation
FROM machines
JOIN reseaux ON machines.reseau = reseaux.reseau;
```
- **`JOIN reseaux`** : « en combinant avec la table `reseaux` ».
- **`ON machines.reseau = reseaux.reseau`** : la **condition de liaison** — quelles lignes vont ensemble (celles qui ont le même réseau).
- On **préfixe** les colonnes par leur table (`machines.nom`, `reseaux.localisation`) pour lever toute ambiguïté.

Résultat : chaque machine affichée **avec** la localisation de son réseau, sans avoir stocké cette localisation dans `machines`.

## 3. Pièges rencontrés (à éviter)
- **Pas de virgule** après la dernière colonne d'un `CREATE TABLE`.
- `INSERT INTO` la **bonne table** (les localisations vont dans `reseaux`, pas `machines`).
- Le `ON` doit **comparer** deux colonnes avec `=` : `ON machines.reseau = reseaux.reseau` (pas `machines.reseaux.reseau`).

---

## 4. Questions de révision (auto-test)

1. À quoi sert une jointure `JOIN` ?
2. Pourquoi éviter de répéter la localisation dans chaque ligne de `machines` ?
3. Que fait la clause `ON` ?
4. Écris une jointure qui affiche `machines.nom` et `reseaux.localisation`.
5. Pourquoi préfixe-t-on les colonnes par le nom de la table ?
6. Que relie-t-on dans le `ON` de cet exemple ?
7. Vrai/faux : la donnée `localisation` est stockée dans la table `machines`.
8. Corrige : `JOIN reseaux ON machines.reseaux.reseau`.
9. Quelle erreur dans `CREATE TABLE t (a TEXT, b TEXT,);` ?
10. Dans quelle table faut-il insérer les localisations ?

<details>
<summary>Réponses</summary>

1. À combiner les lignes de deux tables selon une condition de correspondance.
2. Pour ne pas dupliquer l'info ; on la range une fois dans `reseaux` et on relie.
3. Elle définit la **condition de liaison** : quelles lignes des deux tables vont ensemble.
4. `SELECT machines.nom, reseaux.localisation FROM machines JOIN reseaux ON machines.reseau = reseaux.reseau;`.
5. Pour lever l'ambiguïté quand une colonne pourrait exister dans les deux tables.
6. `machines.reseau` et `reseaux.reseau` (via `=`).
7. Faux : elle est dans `reseaux`, récupérée par la jointure.
8. `JOIN reseaux ON machines.reseau = reseaux.reseau`.
9. Une **virgule en trop** après `b TEXT` (avant la parenthèse fermante).
10. Dans la table `reseaux`.

</details>
