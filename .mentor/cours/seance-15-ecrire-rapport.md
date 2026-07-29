# Fiche de cours — Séance 15 : écrire un rapport (lire → parser → écrire)

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » (5/…). Thème : produire un fichier de sortie — un vrai mini-outil d'admin.

---

## 1. Ouvrir deux fichiers à la fois

Un outil lit souvent une **source** et écrit un **résultat**. On peut ouvrir les deux d'un coup :

```python
with open("hosts.txt", "r") as entree, open("rapport.txt", "w") as sortie:
    for ligne in entree:
        ...
        sortie.write(...)
```
- `entree` : le fichier à **lire** (`"r"`).
- `sortie` : le fichier à **écrire** (`"w"`, qui écrase / crée).
- Les deux `open` sont séparés par une **virgule**, et les deux fichiers se referment tout seuls à la fin du bloc.

## 2. `f.write()` prend UNE seule chaîne

Contrairement à `print` (qui accepte plusieurs éléments séparés par des virgules), **`write()` veut une seule chaîne**. On la **construit** avec le `+` (concaténation) :

```python
sortie.write("Machine : " + nom + " - IP : " + ip + "\n")
```
- Le `+` colle les chaînes (`"a" + "b"` → `"ab"`).
- ⚠️ Ne pas oublier le **`\n`** à la fin, sinon tout s'écrit sur une seule ligne.
- Si une donnée est un **nombre**, il faut la convertir : `str(nombre)` (on ne peut pas coller un `int` à une chaîne avec `+`).

## 3. Nettoyer avant d'écrire

Les lignes lues gardent leur `\n` (et parfois des espaces). Si on ne fait pas `.strip()`, le rapport aura des **lignes vides** (double `\n`) et des espaces en trop. Toujours nettoyer les champs avec `.strip()` avant d'écrire.

## 4. Le motif complet « lire → parser → écrire »

```python
with open("hosts.txt", "r") as entree, open("rapport.txt", "w") as sortie:
    for ligne in entree:
        morceau = ligne.split(":")
        nom = morceau[0].strip()
        ip = morceau[1].strip()
        sortie.write("Machine : " + nom + " - IP : " + ip + "\n")
```
C'est le squelette de **tout script d'automatisation** : prendre une source, la transformer, produire un résultat.

---

## 5. Questions de révision (auto-test)

1. Comment ouvrir deux fichiers dans un seul `with` ?
2. Quel mode pour le fichier qu'on lit ? Pour celui qu'on écrit ?
3. `f.write()` accepte-t-il plusieurs arguments séparés par des virgules comme `print` ?
4. Comment construire la chaîne à écrire à partir de plusieurs morceaux ?
5. Que se passe-t-il si on oublie le `\n` dans `write` ?
6. Pourquoi faut-il `.strip()` les champs avant de les écrire ?
7. Comment écrire un nombre (`int`) dans un fichier avec `+` ?
8. Le mode `"w"` conserve-t-il le contenu existant du fichier ?
9. Quel mode utiliser pour AJOUTER à la fin sans effacer ?
10. Décris en une phrase le motif « lire → parser → écrire ».

<details>
<summary>Réponses</summary>

1. `with open("a.txt","r") as entree, open("b.txt","w") as sortie:`.
2. Lecture = `"r"` ; écriture = `"w"`.
3. Non : `write()` prend **une seule** chaîne.
4. Avec le `+` (concaténation) : `"Nom : " + nom + "\n"`.
5. Tout s'écrit sur une seule et même ligne (pas de saut de ligne).
6. Parce que les lignes lues contiennent un `\n` (et parfois des espaces) → sinon lignes vides / espaces en trop dans le rapport.
7. En le convertissant : `str(nombre)`.
8. Non : `"w"` **écrase** tout le contenu existant.
9. Le mode `"a"` (append = ajouter).
10. On prend une source (lire), on la transforme (parser), et on produit un résultat (écrire) — le squelette de tout script d'automatisation.

</details>
