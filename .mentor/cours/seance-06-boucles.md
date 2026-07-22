# Fiche de cours — Séance 6 : Python — les boucles

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : répéter une action avec `for` / `range` et `while`.

---

## 1. À quoi servent les boucles

Une **boucle** (*loop*) répète automatiquement un bloc d'instructions, au lieu de le réécrire. Comme un `if`, le corps de la boucle est **indenté**.

## 2. `for` + `range` (la plus courante)

```python
for i in range(1, 4):
    print(i)
```
→ affiche `1`, `2`, `3`.

- **`range(début, fin)`** génère une suite de nombres.
- ⚠️ **La borne de fin est EXCLUE** : `range(1, 4)` donne `1, 2, 3` (pas 4). Pour aller **jusqu'à 30 inclus**, il faut `range(24, 31)`.
- **`range(fin)`** avec un seul argument part de 0 : `range(5)` → `0, 1, 2, 3, 4`.
- La **variable de boucle** (`i`, ou un nom parlant comme `prefixe`) prend tour à tour chaque valeur : **c'est le `for` qui la pilote**, pas toi.

### Point clé : la variable est réaffectée à chaque tour
Dans un `for`, inutile d'incrémenter la variable soi-même — le `for` lui donne la valeur suivante automatiquement. Écrire `prefixe = prefixe + 1` dans le corps ne sert à rien (c'est aussitôt écrasé au tour suivant).

## 3. `while` (répéter tant qu'une condition tient)

```python
n = 3
while n > 0:
    print(n)
    n = n - 1        # ICI il FAUT faire évoluer la condition
```
→ `3, 2, 1`.

- Répète **tant que** la condition est vraie.
- ⚠️ Contrairement au `for`, **c'est à toi de faire évoluer** la variable. Si tu oublies, la condition reste vraie pour toujours → **boucle infinie**.

## 4. `for` vs `while` — quand utiliser quoi ?

- **`for`** : quand on sait **sur quoi** on itère (une plage de nombres, une liste). Le plus fréquent.
- **`while`** : quand on répète **jusqu'à ce qu'une condition change**, sans savoir combien de fois à l'avance.

## 5. Exemple complet vu en cours (tableau de sous-réseaux)

```python
for prefixe in range(24, 31):
    hotes = 2 ** (32 - prefixe) - 2
    print(prefixe, "->", hotes)
```
Affiche les tailles de /24 (254) à /30 (2).

---

## 6. Questions de révision (auto-test)

1. À quoi sert une boucle ?
2. Que produit `range(1, 4)` ? Et `range(4)` ?
3. La borne de fin d'un `range` est-elle incluse ou exclue ?
4. Quel `range` faut-il pour parcourir les nombres de 24 à 30 **inclus** ?
5. Dans un `for i in range(...)`, qui décide de la valeur de `i` à chaque tour ?
6. Pourquoi `prefixe = prefixe + 1` est-il inutile dans un `for prefixe in range(...)` ?
7. Dans un `while`, que se passe-t-il si on oublie de faire évoluer la condition ?
8. Quand vaut-il mieux un `for` plutôt qu'un `while` ?
9. Combien de fois s'exécute le corps de `for i in range(0, 5)` ?
10. Écris une boucle qui affiche les nombres de 1 à 10 inclus.

<details>
<summary>Réponses</summary>

1. À répéter automatiquement un bloc d'instructions sans le réécrire.
2. `range(1, 4)` → `1, 2, 3` ; `range(4)` → `0, 1, 2, 3`.
3. **Exclue**.
4. `range(24, 31)`.
5. Le `for` lui-même (il réaffecte `i` à la valeur suivante à chaque tour).
6. Parce que le `for` réaffecte `prefixe` au tour suivant ; l'incrément manuel est aussitôt écrasé, donc sans effet.
7. La condition reste vraie indéfiniment → **boucle infinie**.
8. Quand on connaît la plage/collection à parcourir (nombre de tours défini).
9. 5 fois (i = 0, 1, 2, 3, 4).
10. `for n in range(1, 11):` puis `    print(n)`.

</details>
