# Fiche de cours — Séance 18 : structurer son code avec des fonctions

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » — structuration. Thème : rendre un programme clair en le découpant en fonctions.

---

## 1. Pourquoi des fonctions pour structurer

Un long script « en vrac » est dur à lire et à corriger. On le découpe en **petites fonctions au nom parlant**, chacune faisant **un seul job**. Avantages :
- **Lisibilité** : le nom de la fonction documente ce que fait le code.
- **Réutilisation** : on l'appelle autant de fois qu'on veut.
- **Débogage** : on isole le problème dans une fonction.

## 2. Extraire une logique dans une fonction

Au lieu d'un test brut, on lui donne un nom :

```python
def est_majeur(age):
    return age >= 18        # renvoie True ou False

if est_majeur(20):
    print("Majeur")
```
Le `if est_majeur(20):` se lit comme une phrase. La logique vit dans la fonction ; le code principal devient limpide.

## 3. Exemple vu en cours : extraire le filtre

Avant (logique brute dans le `if`) :
```python
if reseau + "." in ligne:
    ...
```
Après (logique nommée) :
```python
def est_sur_reseau(ligne, reseau):
    return reseau + "." in ligne

# ...
if est_sur_reseau(ligne, reseau):
    ...
```
Même comportement, mais l'intention est claire : « si cette ligne est sur ce réseau ».

## 4. L'ordre d'un fichier Python (convention)

1. les **`import`** (tout en haut),
2. les **fonctions** (`def ...`),
3. le **code principal** (input, boucles, appels de fonctions).

## 5. Rappel : définir vs appeler

- **Définir** : `def nom(paramètres):` + corps + `return valeur`.
- **Appeler** : `nom(argument)` — **avec les parenthèses** (elles exécutent la fonction) ; on récupère la valeur renvoyée (dans une variable ou directement dans un `if`).

---

## 6. Questions de révision (auto-test)

1. Cite deux avantages de découper un programme en fonctions.
2. Qu'est-ce qu'une fonction qui `return` un booléen permet de faire dans un `if` ?
3. Réécris `if x % 2 == 0:` en passant par une fonction `est_pair(x)`.
4. Dans quel ordre organise-t-on un fichier Python (imports, fonctions, code) ?
5. Quelle est la différence entre définir et appeler une fonction ?
6. Pourquoi `est_sur_reseau(ligne, reseau)` est-il plus clair que `reseau + "." in ligne` en plein milieu d'un `if` ?
7. Combien de « jobs » une bonne petite fonction devrait-elle faire ?
8. Que renvoie `est_sur_reseau("web: 192.168.1.0", "192.168.1")` ?
9. Où placer les `import` dans un fichier ?
10. Une fonction peut-elle être appelée plusieurs fois ?

<details>
<summary>Réponses</summary>

1. Lisibilité (le nom documente), réutilisation, débogage plus facile (au choix, deux).
2. L'utiliser directement comme condition : `if ma_fonction(...):`.
3. `def est_pair(x): return x % 2 == 0` puis `if est_pair(x):`.
4. Imports en haut, puis les fonctions, puis le code principal.
5. Définir = écrire la fonction (`def`) ; appeler = l'exécuter avec `nom(arg)` (parenthèses).
6. Parce que le nom exprime l'intention (« est sur ce réseau »), au lieu d'une expression technique à décoder.
7. Idéalement un seul.
8. `True`.
9. Tout en haut du fichier.
10. Oui, autant de fois qu'on veut.

</details>
