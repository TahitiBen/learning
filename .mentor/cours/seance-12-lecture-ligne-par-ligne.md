# Fiche de cours — Séance 12 : lire un fichier ligne par ligne & compter

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » (2/…). Thème : traiter un fichier ligne par ligne — la base du parsing.

---

## 1. Lire ligne par ligne : `for ligne in f`

`f.read()` lit **tout** d'un coup. Pour **traiter** un fichier (compter, filtrer, chercher), on le lit **ligne par ligne** :

```python
with open("hosts.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
```
- `for ligne in f:` parcourt le fichier **une ligne à la fois** ; `ligne` prend chaque ligne tour à tour.
- C'est la boucle `for`… appliquée directement à un fichier ouvert.

## 2. Nettoyer avec `.strip()`

⚠️ Chaque ligne lue **contient le `\n` de fin**. Un `print(ligne)` brut donne donc des lignes **doublement espacées**.

- **`.strip()`** est une **méthode de chaîne** qui enlève les espaces et sauts de ligne au début et à la fin.
- `ligne.strip()` = la ligne propre.

## 3. Compter : le motif « compteur »

Pour compter des éléments dans une boucle :

```python
compteur = 0                      # AVANT la boucle (une seule fois)
with open("hosts.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
        compteur += 1             # DANS la boucle (à chaque tour)
print("Total :", compteur, "machines")   # APRÈS la boucle
```

Trois règles d'or :
- `compteur = 0` **avant** la boucle (sinon il repartirait à zéro à chaque tour).
- `compteur += 1` **dans** la boucle.
- l'affichage du total **après** la boucle (une fois tout compté).

**`+= 1`** est le raccourci de `compteur = compteur + 1` (« ajoute 1 à la variable »). Il existe aussi `-=`, `*=`, etc.

## 4. Ce que ça ouvre (parsing)

Lire ligne par ligne, c'est la base pour : compter des entrées d'un inventaire, analyser un log, filtrer des lignes, extraire des infos. On y ajoutera bientôt le **filtrage** (`if "x" in ligne:`).

---

## 5. Questions de révision (auto-test)

1. Quelle est la différence entre `f.read()` et `for ligne in f:` ?
2. Que contient chaque `ligne` lue, en plus du texte ?
3. Que fait `.strip()` ?
4. Pourquoi `print(ligne)` (sans strip) donne-t-il des lignes doublement espacées ?
5. Où place-t-on `compteur = 0` : avant, dans, ou après la boucle ? Pourquoi ?
6. Que veut dire `compteur += 1` ?
7. Où affiche-t-on le total, et pourquoi pas dans la boucle ?
8. Que se passerait-il si `compteur = 0` était placé DANS la boucle ?
9. Écris une boucle qui affiche chaque ligne de `log.txt` proprement.
10. Cite deux usages concrets de la lecture ligne par ligne en infra.

<details>
<summary>Réponses</summary>

1. `f.read()` lit tout le fichier d'un coup (une chaîne) ; `for ligne in f:` le parcourt ligne par ligne.
2. Le caractère de saut de ligne `\n` à la fin.
3. Elle enlève les espaces et sauts de ligne au début et à la fin d'une chaîne.
4. Parce que la ligne contient déjà un `\n`, et `print` en ajoute un autre → double saut.
5. **Avant** la boucle : sinon il serait remis à 0 à chaque tour et ne compterait jamais.
6. Ajoute 1 à `compteur` (raccourci de `compteur = compteur + 1`).
7. **Après** la boucle : pour n'afficher le total qu'une fois tout compté (dans la boucle, il s'afficherait à chaque tour).
8. Il repartirait à 0 à chaque tour → le total afficherait toujours 1 (ou resterait faux).
9. `with open("log.txt", "r") as f:` / `    for ligne in f:` / `        print(ligne.strip())`.
10. Ex. : compter les machines d'un inventaire ; analyser/filtrer un fichier de logs.

</details>
