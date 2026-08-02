# Fiche de cours — Séance 17 : Projet-bilan (outil d'audit réseau)

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Projet de synthèse du module « Python pour l'infra ». Thème : assembler un programme complet + structurer son code.

---

## 1. Le programme final (référence)

```python
import datetime

maintenant = datetime.datetime.now()
reseau = input("Donner le reseau a auditer (ex. 192.168.1) : ")

compteur = 0
with open("hosts.txt", "r") as entree, open("audit.txt", "w") as sortie:
    sortie.write("Audit du reseau " + reseau + " - genere le " + maintenant.strftime("%d/%m/%Y %Hh%M") + "\n")
    for ligne in entree:
        morceau = ligne.split(":")
        if reseau + "." in ligne:
            sortie.write("Machine : " + morceau[0] + " - IP : " + morceau[1].strip() + "\n")
            compteur += 1
    sortie.write("Total : " + str(compteur) + " machine(s)\n")
    if compteur == 0:
        print("Aucune machine sur ce reseau")
```

## 2. Comprendre `if reseau + "." in ligne:`

À lire de l'intérieur vers l'extérieur, dans l'ordre où Python calcule :
1. `reseau` = ce que l'utilisateur a tapé, ex. `"192.168.1"`.
2. `reseau + "."` = **concaténation** → une nouvelle chaîne `"192.168.1."`.
3. `"192.168.1." in ligne` = test **`in`** → `True` / `False`.
4. `if <True/False>:` → exécute si vrai.

👉 **Un `if` agit sur n'importe quelle expression qui vaut `True`/`False`** : une variable, une comparaison, un test `in`, ou un petit calcul fait à la volée. Python calcule l'expression d'abord, puis le `if` regarde le résultat.

**Astuce lisibilité** : si une condition paraît dense, extrais-la dans une variable —
```python
motif = reseau + "."
if motif in ligne:
```
C'est **identique**, et plus clair. Code clair > code court.

## 3. ⭐ Structurer un programme : avant / dans / après la boucle

C'est le vrai enjeu d'un programme multi-étapes :
- **Avant la boucle** : ce qui se fait UNE fois (l'en-tête du rapport, `compteur = 0`).
- **Dans la boucle** : ce qui se fait POUR CHAQUE élément (tester, écrire la machine trouvée, `compteur += 1`).
- **Après la boucle** : ce qui se fait UNE fois à la fin (le total, le message « aucune machine »).

⚠️ **Piège vécu** : écrire la machine **après** la boucle → `morceau` ne contient plus que la **dernière ligne** lue. Toute écriture « par élément » doit être **dans** la boucle.

## 4. Rappels réunis dans ce projet
`input` (stocker le résultat !), `datetime` + `strftime`, ouvrir 2 fichiers, `for ligne in f`, filtrage `in` + point, `split` + index `[0]`/`[1]` + `.strip()`, compteur `+= 1`, `str()` pour écrire un nombre.

---

## 5. Questions de révision (auto-test)

1. Dans `if reseau + "." in ligne:`, qu'est-ce que Python calcule en premier ?
2. Pourquoi ajouter `"."` au réseau saisi ?
3. Réécris cette condition en 2 lignes plus lisibles.
4. Qu'est-ce qui doit se placer AVANT la boucle ? Donne 2 exemples.
5. Qu'est-ce qui doit se placer DANS la boucle ?
6. Qu'est-ce qui doit se placer APRÈS la boucle ?
7. Que vaut `morceau` une fois la boucle terminée ?
8. Pourquoi `print(input(...))` est-il une erreur si on veut réutiliser la saisie ?
9. Pourquoi `str(compteur)` dans le `write` du total ?
10. Un `if` peut-il tester autre chose qu'une simple variable ?

<details>
<summary>Réponses</summary>

1. L'expression `reseau + "."` (il fabrique la chaîne), puis il fait le test `in`.
2. Pour un filtre précis : distinguer `192.168.1.x` de `192.168.10.x` (piège de sous-chaîne).
3. `motif = reseau + "."` puis `if motif in ligne:`.
4. Ce qui se fait une seule fois : l'en-tête du rapport, l'initialisation `compteur = 0`.
5. Ce qui se fait pour chaque ligne : le test, l'écriture de la machine trouvée, `compteur += 1`.
6. Ce qui se fait une fois à la fin : écrire le total, le message si `compteur == 0`.
7. La **dernière** ligne lue du fichier (la boucle est finie).
8. Parce que ça affiche la saisie mais ne la **stocke** pas ; il faut `reseau = input(...)`.
9. Parce que `write` veut une chaîne : on ne peut pas coller un `int` avec `+`, il faut le convertir.
10. Oui : n'importe quelle expression valant `True`/`False` (comparaison, `in`, calcul…).

</details>
