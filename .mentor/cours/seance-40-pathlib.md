# Fiche de cours — Séance 40 : `pathlib` (gérer les chemins de fichiers)

> Support de révision (séance du 2026-09-23). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Compléments Python. Thème : manipuler les chemins proprement, parcourir un dossier.

---

## 1. Le problème des chemins « en texte »

Avant, on écrivait les chemins à la main :
```python
open("python/hosts.txt")
```
Fragile : le séparateur diffère selon l'OS (`/` Linux, `\` Windows), coller des bouts avec `+` est source de fautes, et on ne peut pas facilement vérifier/filtrer/lister.

`pathlib` = module **standard** (aucun `pip`) qui traite les chemins comme des **objets**.

## 2. La base : `Path` et l'assemblage avec `/`

```python
from pathlib import Path

dossier = Path("python")            # chemin vers le dossier
fichier = dossier / "hosts.txt"     # on assemble avec /  →  python\hosts.txt
```
👉 L'opérateur **`/`** met le bon séparateur selon l'OS, automatiquement. Fini le bricolage.

## 3. Les méthodes utiles

```python
fichier = Path("python/hosts.txt")

fichier.exists()   # True si le fichier existe  → éviter de planter
fichier.name       # 'hosts.txt'  (le nom seul)
fichier.suffix     # '.txt'       (l'extension)
fichier.parent     # 'python'     (le dossier parent)
```

## 4. Parcourir un dossier : `.iterdir()`

```python
from pathlib import Path

doss = Path("python")
for f in doss.iterdir():             # chaque élément du dossier
    print(f.name, "->", f.suffix)    # ⚠️ virgules entre les arguments de print !
```

Filtrer par type :
```python
for f in Path("python").iterdir():
    if f.suffix == ".txt":           # que les fichiers texte
        print("Texte :", f.name)
```

## 5. Pourquoi c'est utile (infra / DevOps)

C'est ce qui fait passer un script de **« je lis 1 fichier codé en dur »** à **« je parcours un dossier, je vérifie, je filtre, je traite tout ce qui s'y trouve »** :
- auditer **tous** les logs / configs d'un dossier d'un coup ;
- vérifier qu'un fichier existe **avant** de l'ouvrir (`.exists()`) → le script ne plante plus ;
- ne traiter qu'un type de fichier (`.suffix == ".conf"`).

---

## 6. Questions de révision (auto-test)

1. Faut-il installer `pathlib` avec `pip` ?
2. Comment importe-t-on `Path` ?
3. Avec quel opérateur assemble-t-on deux morceaux de chemin ?
4. Quelle méthode dit si un fichier existe ?
5. Que renvoient `.name` et `.suffix` ?
6. Quelle méthode parcourt le contenu d'un dossier ?
7. Écris la boucle qui affiche le nom de chaque fichier du dossier `python`.
8. Comment ne garder que les fichiers `.txt` ?
9. Dans `print(a, "->", b)`, à quoi servent les virgules ?
10. Cite un cas d'usage infra de `pathlib`.

<details>
<summary>Réponses</summary>

1. Non, il est dans la **bibliothèque standard**.
2. `from pathlib import Path`.
3. L'opérateur **`/`** : `Path("python") / "hosts.txt"`.
4. `.exists()`.
5. `.name` = le nom du fichier ; `.suffix` = l'extension (`.txt`).
6. `.iterdir()`.
7. `for f in Path("python").iterdir(): print(f.name)`.
8. `if f.suffix == ".txt":` dans la boucle.
9. À **séparer les arguments** de `print` (chacun est affiché à la suite, espacés).
10. Auditer tous les logs/configs d'un dossier, vérifier l'existence d'un fichier avant de l'ouvrir, filtrer par extension…

</details>
