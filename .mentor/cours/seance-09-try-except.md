# Fiche de cours — Séance 9 : Python — la gestion d'erreurs (`try` / `except`)

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : empêcher un programme de planter sur une entrée invalide.

---

## 1. Le problème

Certaines opérations peuvent **échouer** et faire **planter** le programme (une **exception** est levée). Exemple : `int("abc")` échoue, car « abc » n'est pas un nombre → erreur **`ValueError`**, et le programme s'arrête brutalement.

Un vrai outil ne doit jamais planter sur une saisie humaine.

## 2. La solution : `try` / `except`

```python
try:
    age = int(input("Ton age ? "))
    print("Dans 10 ans tu auras", age + 10)
except ValueError:
    print("Ce n'est pas un nombre valide.")
```

- **`try:`** contient le code **risqué**. Python le tente.
- Si tout se passe bien → le bloc `except` est **ignoré**.
- Si une erreur survient → Python **saute** immédiatement dans le bloc **`except`** (pas de crash).
- **`except ValueError:`** attrape spécifiquement ce type d'erreur.

## 3. Les exceptions courantes

| Exception | Quand |
|---|---|
| `ValueError` | conversion impossible : `int("abc")` |
| `ZeroDivisionError` | division par zéro : `10 / 0` |
| `KeyError` | clé absente d'un dictionnaire |
| `FileNotFoundError` | fichier introuvable |

On peut cibler l'erreur qu'on attend (recommandé) plutôt que d'attraper tout en aveugle.

## 4. Nuance : convertir pour tester vs pour réutiliser

```python
int(nb)          # teste si nb est convertible, mais JETTE le résultat
nb = int(nb)     # convertit ET garde le nombre pour le réutiliser
```
Pour une simple **validation**, `int(nb)` seul suffit (s'il échoue, l'erreur nous le dit). Pour **calculer** ensuite avec, il faut **stocker** : `nb = int(nb)`.

## 5. Vers une saisie robuste (prochaine étape)

Combiné à une boucle, `try`/`except` permet de **redemander** jusqu'à obtenir une entrée correcte, sans jamais planter :
```python
while True:
    try:
        prefixe = int(input("Prefixe (0-32) : "))
    except ValueError:
        print("Ce n'est pas un nombre, reessaie.")
        continue
    if 0 <= prefixe <= 32:
        break
    print("Hors de 0-32, reessaie.")
```
(`while True` + `break` + `continue` : à voir à la séance suivante.)

---

## 6. Questions de révision (auto-test)

1. Qu'est-ce qu'une « exception » ?
2. Quelle erreur lève `int("abc")` ?
3. À quoi sert le bloc `try` ?
4. Que se passe-t-il si le code du `try` réussit sans erreur ?
5. Que se passe-t-il s'il échoue ?
6. Pourquoi vaut-il mieux cibler `except ValueError` plutôt qu'attraper tout ?
7. Différence entre `int(nb)` et `nb = int(nb)` ?
8. Cite deux exceptions Python en dehors de `ValueError`.
9. Pourquoi un programme qui demande une saisie ne doit-il pas planter sur une mauvaise entrée ?
10. Écris un `try`/`except` qui demande un nombre et affiche « pas un nombre » si la saisie est invalide.

<details>
<summary>Réponses</summary>

1. Une erreur levée pendant l'exécution qui, non gérée, arrête le programme.
2. `ValueError`.
3. À contenir le code risqué que Python va tenter d'exécuter.
4. Le bloc `except` est ignoré, le programme continue.
5. Python saute dans le bloc `except` correspondant (au lieu de planter).
6. Pour ne gérer que l'erreur attendue et ne pas masquer d'autres bugs par erreur.
7. `int(nb)` teste la conversion mais jette le résultat ; `nb = int(nb)` garde le nombre pour le réutiliser.
8. Par ex. `ZeroDivisionError`, `FileNotFoundError` (ou `KeyError`).
9. Parce qu'un utilisateur peut toujours taper n'importe quoi ; l'outil doit rester robuste et guider, pas s'arrêter.
10. `try:` / `    n = int(input("Nombre ? "))` / `except ValueError:` / `    print("pas un nombre")`.

</details>
