# Fiche de cours — Séance 8 : Mini-projet & logique de validation

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : assembler un vrai programme (fonction + saisie + validation + classification) et maîtriser la logique `and`/`or`.

---

## 1. Le programme complet (référence)

```python
def hotes_utilisables(prefixe):
    return 2 ** (32 - prefixe) - 2

prefixe = int(input("Ecris un nombre entre 0 et 32: "))
while prefixe < 0 or prefixe > 32:
    print("Ce nombre n'est pas entre 0 et 32")
    prefixe = int(input("Ecris un nombre entre 0 et 32: "))

print(prefixe, "->", hotes_utilisables(prefixe))

if prefixe <= 24:
    print("Grand reseau")
elif prefixe <= 28:
    print("Reseau moyen")
else:
    print("Petit reseau")
```

## 2. Le motif « boucle de validation » (`while`)

Redemander une saisie **tant qu'elle est invalide** :
```python
valeur = int(input("..."))
while <condition_d_invalidité>:
    print("Erreur, reessaie.")
    valeur = int(input("..."))
# ici la valeur est forcément valide
```
- On demande **une fois** avant la boucle.
- La boucle **redemande** tant que la condition d'invalidité est vraie.
- Après la boucle, **pas besoin de `else`** : si on en est sorti, c'est que la valeur est bonne. On continue avec une ligne normale.

## 3. ⭐ `and` vs `or` : le basculement dedans / dehors

Pour un intervalle 0–32 :
- **VALIDE = à l'intérieur** → `prefixe >= 0 and prefixe <= 32` (il faut **les deux** → `and`).
- **INVALIDE = à l'extérieur** → `prefixe < 0 or prefixe > 32` (une seule suffit → `or`).

👉 Quand on passe de « dedans » à « dehors » (ou qu'on inverse une condition), **`and` devient `or`** (et vice-versa). Un nombre ne peut pas être « < 0 **et** > 32 » en même temps : ce serait toujours faux.

## 4. `if` / `elif` / `else` : l'aiguillage

- Python teste **de haut en bas**, s'arrête au **premier vrai**.
- Chaque `elif` profite du fait que les cas précédents sont **faux** → conditions plus simples. Ex. : après `if prefixe <= 24`, le `elif prefixe <= 28` n'a pas besoin de revérifier `> 24`.
- **`else` ne prend JAMAIS de condition** : c'est le « dans tous les autres cas ». On écrit `else:`, pas `else quelquechose:`.

## 5. Pièges d'opérateurs (à mémoriser)

Des symboles qui existent en Python mais ne veulent **pas** dire ce qu'on croit :

| Tu veux… | ✅ Python | ❌ Piège |
|---|---|---|
| puissance | `**` | `^` (XOR binaire) |
| et logique | `and` | `&` (ET binaire) |
| ou logique | `or` | `|` (OU binaire) |

Règle : pour la **logique**, on utilise des **mots** (`and`, `or`, `not`), pas des symboles.

---

## 6. Questions de révision (auto-test)

1. Pour valider qu'un nombre est **dans** 0–32, utilise-t-on `and` ou `or` ?
2. Et pour détecter qu'il est **en dehors** de 0–32 ?
3. Pourquoi `while prefixe < 0 and prefixe > 32:` ne rejette-t-il jamais rien ?
4. Après une boucle `while` de validation, a-t-on besoin d'un `else` pour la suite ?
5. Le mot-clé `else` peut-il être suivi d'une condition ?
6. Dans un `if/elif`, pourquoi `elif prefixe <= 28:` suffit-il après `if prefixe <= 24:` ?
7. Quel opérateur écrit le « et logique » en Python ? Lequel NE PAS confondre avec ?
8. Écris une boucle qui redemande un âge tant qu'il est négatif.
9. Dans quel ordre Python évalue-t-il les branches d'un `if/elif/elif/else` ?
10. Cite trois symboles qui, en Python, ne signifient pas ce qu'on croit (puissance / et / ou).

<details>
<summary>Réponses</summary>

1. `and` (`prefixe >= 0 and prefixe <= 32`).
2. `or` (`prefixe < 0 or prefixe > 32`).
3. Parce qu'un nombre ne peut pas être à la fois `< 0` **et** `> 32` : la condition est toujours fausse, la boucle ne tourne jamais.
4. Non : si on sort de la boucle, c'est que la valeur est valide ; on continue avec une ligne normale.
5. Non : `else:` seul (aucune condition). Pour une condition supplémentaire, on utilise `elif`.
6. Parce qu'on n'atteint le `elif` que si `prefixe <= 24` est faux, donc `prefixe > 24` est déjà garanti.
7. `and` ; ne pas confondre avec `&` (ET binaire).
8. `age = int(input("Age ? "))` puis `while age < 0:` / `    print("negatif")` / `    age = int(input("Age ? "))`.
9. De haut en bas, en s'arrêtant à la première condition vraie.
10. `^` (n'est pas la puissance mais XOR), `&` (n'est pas `and` mais ET binaire), `|` (n'est pas `or` mais OU binaire).

</details>
