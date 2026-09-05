# Fiche de cours — Séance 31 : requêtes paramétrées & injection SQL 🔐

> Support de révision (séance du 2026-09-04). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Sécurité + pont Python↔SQL. Thème : manipuler des données utilisateur sans danger.

---

## 1. L'injection SQL (la faille)

Quand on **colle** une donnée utilisateur dans une requête avec `+`, son texte devient une **partie de la commande** :

```python
curseur.execute("SELECT * FROM machines WHERE nom = '" + nom + "'")   # ❌ DANGEREUX
```

Si l'utilisateur tape `' OR '1'='1` :
```sql
SELECT * FROM machines WHERE nom = '' OR '1'='1'
```
- son `'` **ferme** la chaîne plus tôt,
- son `OR '1'='1'` ajoute une condition **toujours vraie**,
- → la requête renvoie **TOUTES les lignes** (filtre contourné). Avec un texte pire, on pourrait modifier/supprimer des données.

C'est l'**injection SQL** — une des failles les plus connues (top OWASP).

## 2. La parade : les requêtes paramétrées (`?`)

```python
curseur.execute("SELECT * FROM machines WHERE nom = ?", (nom,))   # ✅ SÛR
```
- Le **`?`** est un **emplacement** ; la valeur est passée **séparément**, dans un **tuple** `(nom,)`.
- ⚠️ Tuple à un élément → **virgule obligatoire** : `(nom,)`.
- La base traite la valeur comme une **donnée pure**, jamais comme du SQL → **injection impossible**. Même `' OR '1'='1` sera cherché comme un nom littéral (0 résultat).

Plusieurs valeurs : `execute("INSERT INTO machines (nom, ip) VALUES (?, ?)", (nom, ip))`.

## 3. La règle d'or

**Dès qu'une donnée vient de l'extérieur (utilisateur, fichier, réseau) → toujours des `?`, jamais de `+` dans la requête.**

---

## 4. Questions de révision (auto-test)

1. C'est quoi une injection SQL, en une phrase ?
2. Que se passe-t-il si un utilisateur tape `' OR '1'='1` dans une requête construite avec `+` ?
3. Comment écrire une requête paramétrée pour chercher par `nom` ?
4. Où passe-t-on la valeur dans une requête paramétrée ?
5. Pourquoi la virgule dans `(nom,)` est-elle importante ?
6. Pourquoi le `?` empêche-t-il l'injection ?
7. La règle d'or dès qu'une donnée vient de l'extérieur ?
8. Écris un INSERT paramétré avec 2 valeurs (`nom`, `ip`).
9. Avec la version `?`, que renvoie l'attaque `' OR '1'='1` ?
10. Pourquoi ce sujet est-il important pour un profil cybersécurité ?

<details>
<summary>Réponses</summary>

1. Quand le texte d'un utilisateur, collé dans une requête, est exécuté comme une partie de la commande SQL.
2. La condition devient toujours vraie → la requête renvoie toutes les lignes (filtre contourné).
3. `curseur.execute("SELECT * FROM machines WHERE nom = ?", (nom,))`.
4. Séparément, dans un **tuple** en 2e argument de `execute`.
5. Sans virgule, `(nom)` n'est pas un tuple mais juste une parenthèse ; un tuple à un élément s'écrit `(nom,)`.
6. Parce que la valeur est envoyée à part et traitée comme une donnée pure, jamais interprétée comme du SQL.
7. Toujours des `?` (requête paramétrée), jamais de `+` / concaténation.
8. `execute("INSERT INTO machines (nom, ip) VALUES (?, ?)", (nom, ip))`.
9. 0 résultat (elle cherche une machine littéralement nommée `' OR '1'='1`).
10. L'injection SQL est une faille classique et répandue ; savoir l'éviter (et la comprendre) est une compétence de base en sécurité.

</details>
