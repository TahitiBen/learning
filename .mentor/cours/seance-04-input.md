# Fiche de cours — Séance 4 : Python — `input()` et conversions

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : rendre un programme interactif et convertir les types.

---

## 1. `input()` — demander une saisie

- **`input("message")`** affiche un message, **attend** que l'utilisateur tape quelque chose, et **renvoie** ce qu'il a saisi.
- On range en général le résultat dans une variable :
  ```python
  nom = input("Ton nom ? ")
  print("Bonjour", nom)
  ```

## 2. ⚠️ LE point clé : `input()` renvoie toujours un `str`

- Même si l'utilisateur tape des chiffres, `input()` renvoie du **texte** (`str`).
- Taper `24` donne `"24"` (texte), **pas** `24` (nombre).
- Conséquence : impossible de calculer directement. `"24" * 2` donnerait `"2424"`, pas `48`.

## 3. Convertir : `int()`, `float()`, `str()`

- **`int(x)`** transforme en entier : `int("24")` → `24`.
- **`float(x)`** transforme en nombre à virgule : `float("3.5")` → `3.5`.
- **`str(x)`** transforme en texte : `str(24)` → `"24"`.

```python
reponse = input("Combien de machines ? ")
nombre = int(reponse)     # "5" (texte) -> 5 (nombre)
print(nombre * 2)
```

### Version emboîtée (courante)
On peut convertir directement la saisie sur une seule ligne :
```python
prefixe = int(input("Préfixe du sous-réseau (ex. 24) : "))
```
Python fait d'abord `input(...)` (renvoie du texte), puis `int(...)` convertit → le tout d'un coup.

## 4. Bonne pratique : nommer les variables

- Un nom de variable doit dire **ce qu'elle contient**. `prefixe` = bon ; `sufixe` pour un préfixe = trompeur (mauvais).
- Un bon nom = du code lisible par les autres… et par soi-même plus tard.

## 5. Exemple complet vu en cours (subnet interactif)

```python
prefixe = int(input("Préfixe du sous-réseau (ex. 24) : "))
print(2 ** (32 - prefixe) - 2)
```
Tape `24` → `254` ; `26` → `62`.

---

## 6. Questions de révision (auto-test)

1. Que fait la fonction `input()` ?
2. De quel type est TOUJOURS la valeur renvoyée par `input()` ?
3. Si l'utilisateur tape `24`, `input()` renvoie `24` ou `"24"` ?
4. Pourquoi faut-il convertir la saisie avant de faire un calcul avec ?
5. Quelle fonction convertit `"24"` en entier ? Et en nombre à virgule ?
6. Que vaut `int("7") + 1` ? Et `"7" + 1` (attention) ?
7. Réécris en une seule ligne : demander un âge et le stocker comme entier dans `age`.
8. Pourquoi `sufixe` est-il un mauvais nom pour une variable qui contient un préfixe ?

<details>
<summary>Réponses</summary>

1. Elle affiche un message, attend une saisie de l'utilisateur et renvoie ce qu'il a tapé.
2. Une chaîne de caractères (`str`).
3. `"24"` (du texte).
4. Parce que `input()` renvoie du texte ; sans conversion, `+`/`*` traitent la valeur comme du texte, pas comme un nombre.
5. `int("24")` → entier ; `float("24")` → nombre à virgule.
6. `int("7") + 1` → `8` ; `"7" + 1` → **erreur** (on ne peut pas additionner un `str` et un `int`).
7. `age = int(input("Ton âge ? "))`.
8. Parce que la variable contient un **préfixe**, pas un suffixe : le nom doit refléter le contenu, sinon il induit en erreur.

</details>
