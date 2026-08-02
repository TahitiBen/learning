# Fiche de cours — Séance 19 : fonctions (suite) — renvoyer une chaîne

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » — structuration (2). Thème : des fonctions qui fabriquent des données.

---

## 1. Une fonction peut renvoyer n'importe quoi

Séance 18 : une fonction renvoyait un **bool** (`est_sur_reseau`). Mais `return` peut renvoyer **tout type** : un nombre, une **chaîne**, une liste…

```python
def saluer(nom):
    return "Bonjour " + nom + " !"

print(saluer("Ruben"))   # Bonjour Ruben !
```
La fonction **fabrique** une valeur et la renvoie ; l'appelant décide quoi en faire (l'afficher, l'écrire…).

## 2. Exemple vu en cours : `formater_machine`

Au lieu d'écrire une longue ligne dans la boucle, on nomme la mise en forme :

```python
def formater_machine(morceau):
    return "Machine : " + morceau[0] + " - IP : " + morceau[1].strip() + "\n"

# dans la boucle :
sortie.write(formater_machine(morceau))
```
La boucle devient lisible : « écris la machine formatée ».

## 3. Un fichier bien structuré

```python
import datetime                     # 1) imports en haut

def est_sur_reseau(ligne, reseau):  # 2) les fonctions
    return reseau + "." in ligne

def formater_machine(morceau):
    return "Machine : " + morceau[0] + " - IP : " + morceau[1].strip() + "\n"

# 3) le code principal
reseau = input("...")
with open(...) as entree, open(...) as sortie:
    for ligne in entree:
        morceau = ligne.split(":")
        if est_sur_reseau(ligne, reseau):
            sortie.write(formater_machine(morceau))
```
Chaque fonction = un job ; le code principal = l'enchaînement des étapes.

---

## 4. Questions de révision (auto-test)

1. Un `return` peut-il renvoyer autre chose qu'un booléen ?
2. Que renvoie `formater_machine(["web", " 10.0.0.1\n"])` ?
3. Pourquoi extraire la mise en forme dans une fonction rend-il la boucle plus lisible ?
4. Dans quel ordre organise-t-on un fichier (imports / fonctions / code principal) ?
5. Écris une fonction `en_majuscules(texte)` qui renvoie le texte en majuscules (`.upper()`).
6. Qui décide quoi faire de la valeur renvoyée par une fonction ?
7. Combien de « jobs » vise-t-on par fonction ?
8. `sortie.write(formater_machine(morceau))` — que se passe-t-il en premier ?
9. Une fonction sans `return` renvoie quoi ? (piège)
10. Pourquoi nommer `formater_machine` plutôt que laisser la ligne brute ?

<details>
<summary>Réponses</summary>

1. Oui : un nombre, une chaîne, une liste, un booléen… tout type.
2. `"Machine : web - IP : 10.0.0.1\n"`.
3. Parce que la ligne devient une intention lisible (« écris la machine formatée ») au lieu d'une longue concaténation.
4. Imports en haut, puis les fonctions, puis le code principal.
5. `def en_majuscules(texte): return texte.upper()`.
6. Celui qui appelle la fonction (le code principal).
7. Un seul.
8. Python appelle d'abord `formater_machine(morceau)` (qui renvoie la chaîne), puis passe cette chaîne à `sortie.write(...)`.
9. `None` (rien d'utile) — d'où l'importance de mettre `return` quand on veut récupérer une valeur.
10. Pour documenter l'intention et pouvoir réutiliser/modifier la mise en forme à un seul endroit.

</details>
