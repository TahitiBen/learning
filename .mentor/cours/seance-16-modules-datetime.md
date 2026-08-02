# Fiche de cours — Séance 16 : les modules (`import`) & `datetime`

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » (6/…). Thème : réutiliser du code tout fait via les modules.

---

## 1. Qu'est-ce qu'un module

Un **module** est une **boîte à outils** de code déjà écrit, prête à l'emploi. Python en fournit des centaines (la **bibliothèque standard** — « batteries incluses »). Inutile de tout réécrire.

On active un module avec **`import`**, en haut du fichier :
```python
import datetime
```

## 2. Le module `datetime` : date et heure

```python
import datetime

maintenant = datetime.datetime.now()
print(maintenant)   # 2026-08-02 03:18:07.123456
```
- ⚠️ **`datetime.datetime`** : le **module** s'appelle `datetime`, et il contient un outil (une classe) aussi nommé `datetime` — d'où la répétition.
- `.now()` renvoie l'instant présent.

## 3. Formater une date : `.strftime()`

La date brute est illisible (microsecondes). On la met en forme avec `.strftime(...)` et des **codes** :

```python
maintenant.strftime("%d/%m/%Y %Hh%M")   # 02/08/2026 03h18
```

| Code | Sens |
|---|---|
| `%d` | jour |
| `%m` | mois |
| `%Y` | année (4 chiffres) |
| `%H` | heure (24 h) |
| `%M` | minute |

## 4. Exemple vu en cours : dater un rapport

```python
import datetime

maintenant = datetime.datetime.now()
with open("hosts.txt", "r") as entree, open("rapport.txt", "w") as sortie:
    sortie.write("Rapport genere le " + maintenant.strftime("%d/%m/%Y %Hh%M") + "\n")
    for ligne in entree:
        morceau = ligne.split(":")
        sortie.write("Machine : " + morceau[0] + " - IP : " + morceau[1].strip() + "\n")
```

## 5. Bonne pratique : nommer clairement

`maintenant` est un meilleur nom que `là` : un nom de variable doit dire **ce qu'elle contient**. Éviter les accents dans les noms de variables.

---

## 6. Questions de révision (auto-test)

1. Qu'est-ce qu'un module en Python ?
2. Quel mot-clé active un module ?
3. Où place-t-on les `import` en général ?
4. Pourquoi écrit-on `datetime.datetime.now()` avec `datetime` deux fois ?
5. Que renvoie `.now()` ?
6. À quoi sert `.strftime()` ?
7. Que produit `strftime("%d/%m/%Y")` ?
8. Comment s'appelle l'ensemble des modules fournis avec Python ?
9. Pourquoi `maintenant` est-il un meilleur nom de variable que `là` ?
10. Écris le code qui importe `datetime` et affiche la date du jour au format `JJ/MM/AAAA`.

<details>
<summary>Réponses</summary>

1. Une boîte à outils de code déjà écrit, réutilisable.
2. `import`.
3. En haut du fichier.
4. Le module `datetime` contient une classe aussi nommée `datetime` ; on écrit donc `module.classe.now()`.
5. L'instant présent (date + heure courantes).
6. À formater une date/heure en une chaîne lisible.
7. La date du jour au format jour/mois/année, ex. `02/08/2026`.
8. La bibliothèque standard.
9. Parce qu'il décrit ce que contient la variable (l'instant présent) ; `là` n'a pas de sens et contient un accent.
10. `import datetime` puis `print(datetime.datetime.now().strftime("%d/%m/%Y"))`.

</details>
