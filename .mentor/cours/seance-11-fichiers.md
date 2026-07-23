# Fiche de cours — Séance 11 : Python — lire et écrire des fichiers

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » (1/…). Thème : manipuler des fichiers, la base de l'automatisation.

---

## 1. Ouvrir un fichier : `open`

`open(chemin, mode)` ouvre un fichier. Les modes :

| Mode | Sens | Effet |
|---|---|---|
| `"r"` | *read* | lire (défaut) |
| `"w"` | *write* | écrire — **écrase** tout le contenu existant |
| `"a"` | *append* | ajouter à la **fin** sans effacer |

## 2. La bonne pratique : `with`

```python
with open("test.txt", "w") as f:
    f.write("bonjour\n")
```
- `with open(...) as f:` ouvre le fichier, le met dans `f`, et le **referme automatiquement** à la fin du bloc indenté.
- Sans `with`, il faudrait penser à `f.close()` soi-même. `with` = plus sûr, on l'utilise toujours.

## 3. Écrire

```python
with open("hosts.txt", "w") as f:
    f.write("serveur-web: 192.168.1.10\n")
    f.write("imprimante: 192.168.1.20\n")
```
⚠️ **`f.write()` n'ajoute PAS de retour à la ligne.** Pour passer à la ligne suivante, on met `\n` soi-même (le code du saut de ligne).

## 4. Lire

```python
with open("hosts.txt", "r") as f:
    contenu = f.read()      # tout le fichier dans une seule chaîne
print(contenu)
```
- `f.read()` → tout le contenu en une chaîne.
- (À venir : `for ligne in f:` pour lire **ligne par ligne**.)

## 5. ⭐ Où est stocké le fichier ? (chemin relatif)

- Un nom simple comme `"hosts.txt"` est un **chemin relatif** : le fichier est créé/cherché dans le **répertoire courant** — le dossier d'où on **lance** le script, pas forcément où est le `.py`.
- Pour cibler un dossier précis : `"python/hosts.txt"`. En Python, le `/` fonctionne aussi sous Windows.
- C'est la même notion de **répertoire courant** que dans le terminal (`cd`, `ls`).

---

## 6. Questions de révision (auto-test)

1. Quelle fonction ouvre un fichier ?
2. Que font les modes `"r"`, `"w"`, `"a"` ?
3. Quel mode **efface** le contenu existant ?
4. À quoi sert le `with` devant `open` ?
5. `f.write("abc")` ajoute-t-il un retour à la ligne automatiquement ?
6. Comment passe-t-on à la ligne suivante dans un fichier ?
7. Que renvoie `f.read()` ?
8. Où est créé un fichier ouvert avec le chemin `"hosts.txt"` ?
9. Comment écrire dans le sous-dossier `python` ?
10. Écris un `with` qui ouvre `log.txt` en lecture et stocke tout son contenu dans `data`.

<details>
<summary>Réponses</summary>

1. `open(chemin, mode)`.
2. `"r"` lire, `"w"` écrire (écrase), `"a"` ajouter à la fin.
3. `"w"`.
4. À refermer automatiquement le fichier à la fin du bloc (plus sûr que `close()` manuel).
5. Non : il faut ajouter `\n` soi-même.
6. En écrivant `\n` (le saut de ligne).
7. Tout le contenu du fichier, sous forme d'une seule chaîne de caractères.
8. Dans le répertoire courant (le dossier d'où on lance le script).
9. `open("python/hosts.txt", "w")`.
10. `with open("log.txt", "r") as f:` puis `    data = f.read()`.

</details>
