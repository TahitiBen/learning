# Fiche de cours — Séance 7 : Python — les fonctions

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : créer et utiliser des fonctions (`def`, `return`, appel).

---

## 1. À quoi sert une fonction

Une **fonction** (*function*) est une **machine réutilisable** : on la définit **une fois**, on l'appelle **autant de fois qu'on veut**. On lui donne des entrées, elle fait un travail, et elle peut **renvoyer** un résultat.

Avantages : éviter de répéter du code, le rendre lisible, le réutiliser partout.

## 2. Définir une fonction : `def`

```python
def double(x):
    return x * 2
```
- **`def`** = mot-clé pour définir une fonction.
- **`double`** = le nom (choisi par toi, parlant).
- **`x`** = un **paramètre** : une entrée, une « boîte vide » remplie au moment de l'appel.
- Le corps est **indenté** (comme un `if` ou une boucle).
- **`return`** renvoie une valeur à celui qui a appelé la fonction.

## 3. Appeler une fonction

```python
resultat = double(5)     # on APPELLE double avec x = 5
print(resultat)          # 10
```
- On appelle par **son nom + parenthèses + argument** : `double(5)`.
- La valeur renvoyée par `return` peut être stockée, affichée, réutilisée…
- ⚠️ **`return` ne s'écrit QUE dans la définition** de la fonction, jamais à l'extérieur. Pour récupérer le résultat dehors, on **appelle** la fonction (`double(5)`), on n'écrit pas `return`.

## 4. ⭐ `return` ≠ `print`

| | Rôle | Après |
|---|---|---|
| `print(x)` | **affiche** x à l'écran (pour l'humain) | la valeur est perdue |
| `return x` | **renvoie** x au programme (pour la machine) | la valeur est réutilisable |

Bonne pratique : une fonction **calcule et `return`** ; c'est **celui qui l'appelle** qui décide d'afficher.

## 5. Piège : ne pas réutiliser le nom de la fonction comme variable

```python
for hotes_utilisables in range(...):   # ✘ écrase la fonction !
```
Si la variable de boucle porte le même nom que la fonction, elle **remplace** la fonction. Utiliser un nom distinct (`prefixe`).

## 6. Exemple complet vu en cours

```python
def hotes_utilisables(prefixe):
    return 2 ** (32 - prefixe) - 2

for prefixe in range(24, 31):
    print(prefixe, "->", hotes_utilisables(prefixe))
```
On **appelle** la fonction directement dans le `print`, avec le préfixe du tour courant — pas de variable intermédiaire inutile.

---

## 7. Questions de révision (auto-test)

1. Quel mot-clé sert à définir une fonction ?
2. Qu'est-ce qu'un paramètre ?
3. Que fait `return` ?
4. Différence entre `return` et `print` ?
5. Comment appelle-t-on une fonction nommée `double` avec la valeur 7 ?
6. Peut-on écrire `return` en dehors d'une fonction ?
7. Que se passe-t-il si la variable de boucle porte le même nom que la fonction ?
8. Écris une fonction `carre(n)` qui renvoie le carré de `n`.
9. Avec la fonction précédente, comment afficher le carré de 9 ?
10. Pourquoi vaut-il mieux qu'une fonction `return` sa valeur plutôt que de la `print` directement ?

<details>
<summary>Réponses</summary>

1. `def`.
2. Une entrée de la fonction (une variable « boîte vide » remplie à l'appel).
3. Il renvoie une valeur à celui qui a appelé la fonction.
4. `return` renvoie la valeur au programme (réutilisable) ; `print` ne fait que l'afficher (valeur perdue ensuite).
5. `double(7)`.
6. Non : `return` ne s'utilise qu'à l'intérieur d'une fonction.
7. La variable écrase la fonction : le nom ne désigne plus la fonction mais la valeur de boucle.
8. `def carre(n):` puis `    return n * n`.
9. `print(carre(9))`.
10. Parce qu'une valeur renvoyée est **réutilisable** (calcul, stockage, boucle…), alors qu'un `print` interne fige l'usage à un simple affichage.

</details>
