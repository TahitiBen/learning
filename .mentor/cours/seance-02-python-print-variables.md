# Fiche de cours — Séance 2 : Python — `print`, variables & types

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : premier programme Python, affichage, variables et types de base.

---

## 1. Un script Python

- **Script** : un fichier texte qui finit par **`.py`**. Python exécute les instructions de haut en bas.
- **Exécuter un script** : `python chemin\du\fichier.py` (ex. `python python\bonjour.py`).
- Vérifier que Python est installé : `python --version`.

## 2. `print` — afficher

- **`print(...)`** est une **fonction** (*function*) : elle affiche à l'écran ce qu'on met entre parenthèses.
- Du **texte** se met entre guillemets : `print("Bonjour")` → affiche `Bonjour`.
- On peut afficher **plusieurs choses** en les séparant par une virgule : `print(ram, "Go")` → affiche `2 Go` (Python ajoute un espace entre les éléments).

### Style (PEP 8)
- Convention : **pas d'espace** entre le nom de la fonction et sa parenthèse → `print("x")`, pas `print ("x")`.
- L'espace ne change **pas** le résultat : c'est purement une question de lisibilité.

## 3. Les variables

- **Variable** (*variable*) : une **boîte étiquetée** qui stocke une valeur pour la réutiliser.
- On la crée par **affectation** avec `=` : `nom = "Optiplex 780"`. Le `=` veut dire « range cette valeur dans cette boîte » (ce n'est **pas** une égalité mathématique).
- Distinction clé : la **variable** = la boîte (`ram`) ; la **valeur** = ce qu'il y a dedans ; le **type** = la nature de cette valeur.

## 4. Les types de base

| Type | Nom complet | Exemple | Remarque |
|---|---|---|---|
| `str` | *string* | `"Paris"` | Du texte, **entre guillemets** |
| `int` | *integer* | `21` | Nombre entier, **sans guillemets** |
| `float` | *float* | `3.5` | Nombre à virgule (point décimal) |
| `bool` | *boolean* | `True` / `False` | Vrai / Faux (majuscule) |

- En Python, **on ne déclare pas le type** : Python le devine d'après la valeur.
- **`type(valeur)`** renvoie le type. Ex. `print(type(21))` → `<class 'int'>`.

### ⚠️ Règle à retenir : guillemets = texte
- `ram = 2` → un **nombre** (`int`).
- `ram = "2"` → du **texte** (`str`), même si ça ressemble à un chiffre !
- Conséquence : `"2" + "2"` donne `"22"` (collage de texte), alors que `2 + 2` donne `4` (addition).

---

## 5. Questions de révision (auto-test)

1. Par quelle extension se termine un fichier de script Python ?
2. Quelle commande exécute le script `bonjour.py` situé dans le dossier `python` ?
3. Que fait la fonction `print` ?
4. Comment afficher une valeur et du texte sur la même ligne avec un seul `print` ?
5. Que signifie le signe `=` dans `nom = "Optiplex 780"` ?
6. Cite les 4 types de base et un exemple de chacun.
7. Quelle est la différence entre `2` et `"2"` pour Python ?
8. Que renvoie `type("3.5")` ? Et `type(3.5)` ?
9. Que vaut `"2" + "2"` ? Et `2 + 2` ?
10. `print ("ok")` et `print("ok")` : y a-t-il une différence de résultat ? Pourquoi préférer la seconde ?

<details>
<summary>Réponses</summary>

1. `.py`.
2. `python python\bonjour.py`.
3. Elle affiche à l'écran ce qu'on met entre parenthèses.
4. En séparant les éléments par une virgule : `print(ram, "Go")`.
5. C'est une **affectation** : « range cette valeur dans la variable » (pas une égalité maths).
6. `str` → `"Paris"` ; `int` → `21` ; `float` → `3.5` ; `bool` → `True`/`False`.
7. `2` est un nombre (`int`) ; `"2"` est du texte (`str`) à cause des guillemets.
8. `type("3.5")` → `<class 'str'>` ; `type(3.5)` → `<class 'float'>`.
9. `"2" + "2"` → `"22"` (texte collé) ; `2 + 2` → `4` (addition).
10. Aucune différence de résultat ; on préfère `print("ok")` par convention (PEP 8), pour la lisibilité.

</details>
