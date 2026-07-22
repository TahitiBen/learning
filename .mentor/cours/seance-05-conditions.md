# Fiche de cours — Séance 5 : Python — les conditions

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : faire réagir un programme selon des conditions.

---

## 1. Les opérateurs de comparaison

Ils posent une question et renvoient un booléen (`True` / `False`) :

| Opérateur | Sens | Exemple vrai |
|---|---|---|
| `==` | égal à | `3 == 3` |
| `!=` | différent de | `3 != 4` |
| `<` | inférieur | `2 < 5` |
| `>` | supérieur | `5 > 2` |
| `<=` | inférieur ou égal | `3 <= 3` |
| `>=` | supérieur ou égal | `4 >= 3` |

### ⚠️ Piège : `==` vs `=`
- **`=`** (un seul) → **affecte** une valeur : `x = 5`.
- **`==`** (deux) → **compare** : `x == 5` (« est-ce que x vaut 5 ? »).

## 2. La structure `if` / `elif` / `else`

```python
age = 20
if age >= 18:
    print("Majeur")
else:
    print("Mineur")
```

Avec plusieurs cas, on ajoute `elif` (« sinon si ») :
```python
note = 12
if note >= 16:
    print("Tres bien")
elif note >= 10:
    print("Passable")
else:
    print("Insuffisant")
```

Règles :
- La ligne `if` / `elif` / `else` se termine par **deux points `:`**.
- Python teste les cas **de haut en bas** et s'arrête au **premier vrai**.
- `else` (optionnel) = « dans tous les autres cas ».

## 3. ⭐ L'indentation : la grande particularité de Python

- Ce qui est « à l'intérieur » d'un bloc est **indenté** (décalé, 4 espaces) vers la droite.
- **En Python, l'indentation EST la structure** — il n'y a pas d'accolades `{}` comme en Bash / PowerShell / C.
- Une mauvaise indentation = erreur (`IndentationError`) ou logique fausse.

## 4. Les opérateurs logiques

Pour combiner plusieurs conditions :

| Opérateur | Vrai quand… | Exemple |
|---|---|---|
| `and` | **les deux** conditions sont vraies | `x >= 0 and x <= 32` |
| `or` | **au moins une** est vraie | `jour == "sam" or jour == "dim"` |
| `not` | inverse le résultat | `not connecte` |

Astuce Python : la double comparaison enchaînée `0 <= x <= 32` remplace élégamment `x >= 0 and x <= 32`.

## 5. Exemple complet vu en cours (subnet validé)

```python
prefixe = int(input("Prefixe du sous-reseau (ex. 24) : "))
if prefixe >= 0 and prefixe <= 32:
    print(2 ** (32 - prefixe) - 2)
else:
    print("Prefixe invalide (0 a 32)")
```
`24` → `254` ; `40` → message d'erreur ; `-5` → message d'erreur.

---

## 6. Questions de révision (auto-test)

1. Quelle est la différence entre `=` et `==` ?
2. Que renvoie une comparaison comme `5 > 2` (quel type de valeur) ?
3. Par quel caractère se termine une ligne `if` ?
4. En Python, qu'est-ce qui définit qu'une instruction est « à l'intérieur » d'un `if` ?
5. À quoi sert `elif` ?
6. Quand la condition `a and b` est-elle vraie ?
7. Quand la condition `a or b` est-elle vraie ?
8. Écris une condition qui n'est vraie que si `x` est entre 10 et 20 (bornes incluses).
9. Pourquoi `if prefixe <= 32:` seul est-il insuffisant pour valider un préfixe réseau ?
10. Que se passe-t-il si on indente mal le bloc d'un `if` ?

<details>
<summary>Réponses</summary>

1. `=` affecte une valeur à une variable ; `==` compare deux valeurs.
2. Un booléen (`True` ou `False`), type `bool`.
3. Par deux points `:`.
4. Son **indentation** (le décalage vers la droite).
5. À tester un cas supplémentaire quand le `if` précédent est faux (« sinon si »).
6. Seulement quand **les deux** conditions `a` et `b` sont vraies.
7. Dès qu'**au moins une** des deux est vraie.
8. `if x >= 10 and x <= 20:` (ou `if 10 <= x <= 20:`).
9. Parce qu'elle ne vérifie que la borne haute ; un nombre négatif (ex. `-5`) passerait. Il faut aussi `>= 0`.
10. On obtient une erreur (`IndentationError`) ou un comportement logique faux.

</details>
