# Fiche de cours — Séance 14 : extraire des champs avec `.split()`

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » (4/…). Thème : découper une ligne pour en extraire les données (comme `cut`).

---

## 1. `.split(séparateur)` : découper une chaîne

`.split(sep)` coupe une chaîne en une **liste** de morceaux, à chaque séparateur.

```python
ligne = "Server-Web: 192.168.1.0"
morceau = ligne.split(":")
print(morceau)   # ['Server-Web', ' 192.168.1.0']
```
- Sans argument, `.split()` découpe sur les espaces.
- Le résultat est une **liste** (`list`) : une boîte **ordonnée** de plusieurs valeurs.

## 2. Les listes et l'indexation

On accède à chaque élément par sa **position (index)** — qui **commence à 0** :

```python
print(morceau[0])   # Server-Web       (1er élément)
print(morceau[1])   # ' 192.168.1.0'   (2e élément)
```
⚠️ Le **premier** élément est `[0]`, pas `[1]`.

## 3. Nettoyer : `.strip()` — avec les parenthèses !

Après un `split(":")`, les morceaux peuvent garder des espaces ou un `\n`. On nettoie avec `.strip()` :

```python
ip = morceau[1].strip()
```
⚠️ **Une méthode s'appelle avec `()`.** `.strip()` **exécute** la méthode et renvoie le texte nettoyé. `.strip` (sans parenthèses) renvoie la **méthode elle-même** (`<built-in method strip...>`), pas le résultat. Même principe que l'appel d'une fonction : `carre(9)`, pas `carre`.

## 4. Le motif « parser un fichier ligne par ligne »

La vraie puissance : combiner lecture ligne par ligne + `split` **par ligne** → ça marche pour 4 ou 10 000 lignes, sans indexer à la main.

```python
with open("hosts.txt", "r") as f:
    for ligne in f:
        morceau = ligne.split(":")
        print("Nom:", morceau[0].strip(), "| IP:", morceau[1].strip())
```

---

## 5. Questions de révision (auto-test)

1. Que renvoie `.split(":")` sur une chaîne ?
2. Que fait `.split()` sans argument ?
3. Quel est l'index du **premier** élément d'une liste ?
4. Que vaut `"a:b:c".split(":")[1]` ?
5. Différence entre `.strip` et `.strip()` ?
6. Pourquoi doit-on mettre `()` après le nom d'une méthode ?
7. Pourquoi vaut-il mieux `split` **dans** la boucle plutôt qu'une grande chaîne indexée à la main ?
8. Écris le code qui, pour la ligne `"web: 10.0.0.1"`, affiche l'IP proprement.
9. Que se passe-t-il si tu accèdes à `morceau[5]` mais que la liste n'a que 2 éléments ?
10. `.split()` modifie-t-il la chaîne d'origine ou en crée-t-il une nouvelle (liste) ?

<details>
<summary>Réponses</summary>

1. Une **liste** des morceaux séparés par `:`.
2. Elle découpe sur les espaces (blancs).
3. `0`.
4. `"b"`.
5. `.strip()` exécute la méthode (renvoie le texte nettoyé) ; `.strip` renvoie la méthode elle-même, sans l'exécuter.
6. Parce qu'une méthode, comme une fonction, doit être **appelée** avec `()` pour s'exécuter et renvoyer un résultat.
7. Parce que ça marche pour n'importe quel nombre de lignes automatiquement, sans réécrire un `print`/index par élément.
8. `morceau = "web: 10.0.0.1".split(":")` puis `print(morceau[1].strip())`.
9. Une erreur `IndexError` (index hors de la liste).
10. Elle crée une nouvelle **liste** ; la chaîne d'origine n'est pas modifiée.

</details>
