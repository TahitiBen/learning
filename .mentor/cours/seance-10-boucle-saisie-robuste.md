# Fiche de cours — Séance 10 : `while True`, `break`, `continue` & saisie robuste

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : boucles contrôlées et saisie utilisateur increvable. **Clôture de la Phase 1.**

---

## 1. `while True` : la boucle infinie contrôlée

```python
while True:
    reponse = input("Tape 'ok' pour sortir : ")
    if reponse == "ok":
        break          # seule sortie
    print("Pas encore...")
```
- `while True:` tourne **indéfiniment** (la condition est toujours vraie).
- On en sort **volontairement** avec `break`. ⚠️ Sans `break`, c'est une boucle infinie sans fin.

## 2. `break` et `continue`

- **`break`** : sort **immédiatement** de la boucle.
- **`continue`** : arrête le tour courant et **passe directement au tour suivant** (ignore le reste du corps).

```python
for n in range(1, 6):
    if n == 3:
        continue       # saute le 3
    print(n)           # 1, 2, 4, 5
```
⚠️ Toute ligne écrite **après** un `break` ou un `continue` dans le même bloc est **morte** (jamais exécutée).

## 3. Le motif « saisie robuste »

Combiner `while True` + `try`/`except` pour redemander jusqu'à une entrée **valide**, sans jamais planter :

```python
while True:
    try:
        prefixe = int(input("Prefixe (0-32) : "))
    except ValueError:
        print("Ce n'est pas un nombre, reessaie.")
        continue                       # pas un nombre -> on redemande
    if 0 <= prefixe <= 32:
        break                          # valide -> on sort
    print("Hors de 0-32, reessaie.")   # nombre mais hors bornes -> on reboucle
```

Trois cas gérés :
1. **Pas un nombre** → `except` → message + `continue`.
2. **Nombre valide** → `break` (sortie).
3. **Nombre hors bornes** → message, la boucle recommence.

## 4. Propreté du code (rappel)

- Pas de **code mort** (après `break`/`continue`).
- Pas de **test redondant** : `prefixe == int(prefixe)` est inutile si `prefixe` est déjà un `int`.
- Un nom de variable = ce qu'il contient.

---

## 5. 🎉 Récap Phase 1 — les fondamentaux acquis

- **Variables & types** : `str`, `int`, `float`, `bool` ; guillemets = texte ; `type()`.
- **Affichage / saisie** : `print`, `input` (toujours un `str`), conversions `int()`/`float()`.
- **Opérateurs** : `+ - * / // % **` ; comparaisons ; logiques **`and`/`or`/`not`** (des mots !).
- **Conditions** : `if`/`elif`/`else`, indentation, `and` (dedans) vs `or` (dehors).
- **Boucles** : `for`/`range` (borne exclue), `while`, `while True` + `break`/`continue`.
- **Fonctions** : `def`, paramètres, `return` (≠ `print`), appel `nom(arg)`.
- **Erreurs** : `try`/`except` (+ `ValueError`).
- **Git** : clone, `add`/`commit`/`push`, `-u`, les 4 zones, `--amend`, `log`.

---

## 6. Questions de révision (auto-test)

1. Comment sort-on d'une boucle `while True` ?
2. Différence entre `break` et `continue` ?
3. Que devient une ligne écrite juste après un `continue` ?
4. Écris le squelette d'une boucle qui redemande un nombre tant que la saisie n'est pas un entier.
5. Dans le motif « saisie robuste », quels sont les trois cas gérés ?
6. Pourquoi `while True` sans `break` est-il dangereux ?
7. Pourquoi `prefixe == int(prefixe)` est-il inutile si `prefixe` vient de `int(input(...))` ?
8. Quel mot-clé attrape une erreur ? Quel mot-clé contient le code risqué ?
9. Cite les trois opérateurs logiques (les mots).
10. Range dans l'ordre les étapes git : commit, add, push.

<details>
<summary>Réponses</summary>

1. Avec `break`.
2. `break` sort de la boucle ; `continue` passe au tour suivant sans finir le tour courant.
3. Elle est « morte » : jamais exécutée.
4. `while True:` / `    try:` / `        n = int(input("Nombre ? "))` / `        break` / `    except ValueError:` / `        print("pas un nombre")`.
5. Pas un nombre (`except` + `continue`) ; nombre valide (`break`) ; nombre hors bornes (message + reboucle).
6. Parce qu'elle tourne à l'infini : sans `break`, le programme ne s'arrête jamais.
7. Parce que `prefixe` est déjà un `int` : le comparer à `int(prefixe)` est toujours vrai, donc sans effet.
8. `except` attrape l'erreur ; `try` contient le code risqué.
9. `and`, `or`, `not`.
10. `add` → `commit` → `push`.

</details>
