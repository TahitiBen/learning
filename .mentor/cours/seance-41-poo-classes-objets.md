# Fiche de cours — Séance 41 : Intro POO (classes et objets)

> Support de révision (séance du 2026-09-23). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Compléments Python. Thème : premier contact avec la programmation orientée objet.

---

## 1. Le problème que la POO résout

Avant, une machine = des données **éparpillées** dans un tuple :
```python
ligne = ('Serveur1', '192.168.1.50', '192.168.1')
ligne[0]   # le nom ? faut deviner l'index
ligne[1]   # l'ip ?
```
Illisible, et les **données** sont séparées des **actions** qu'on fait dessus.

## 2. L'idée : classe = moule, objet = exemplaire

- Une **classe** regroupe au même endroit les **données** (attributs) et ce que la chose **sait faire** (méthodes).
- Un **objet** = un exemplaire concret fabriqué avec ce moule.

Au lieu de `ligne[1]`, on écrit **`machine.ip`** → lisible, et l'objet transporte ses données avec lui.

## 3. La syntaxe de base

```python
class Machine:
    def __init__(self, nom, ip):     # constructeur : appelé À LA CRÉATION
        self.nom = nom               # range le nom DANS l'objet
        self.ip = ip                 # range l'ip DANS l'objet

# créer des objets (chacun indépendant) :
serveur = Machine("Serveur1", "192.168.1.50")
pc      = Machine("PCAdmin",  "192.168.17.1")

print(serveur.nom)    # Serveur1
print(pc.ip)          # 192.168.17.1
```

## 4. Les 3 mots-clés

| Mot | Rôle |
|-----|------|
| **`class`** | définit le moule |
| **`__init__`** | fonction spéciale appelée **automatiquement** à la création ; range les données |
| **`self`** | « l'objet lui-même » ; `self.nom = nom` = « range le nom dans moi » |

- `serveur` et `pc` sont **2 objets indépendants** de la **même** classe : chacun a **ses propres** valeurs.

## 5. Pourquoi c'est utile (infra / DevOps)
Modéliser proprement ce qu'on manipule (une machine, un utilisateur, un serveur, un ticket…) : les données et les actions restent **ensemble**, le code devient lisible et réutilisable. C'est la base de presque tous les gros programmes et frameworks.

---

## 6. Questions de révision (auto-test)

1. Quelle est la différence entre une classe et un objet ?
2. Quel mot-clé définit une classe ?
3. À quoi sert `__init__` ? Quand est-il appelé ?
4. Que représente `self` ?
5. Que fait `self.nom = nom` ?
6. Écris une classe `Machine` avec un `__init__` rangeant `nom` et `ip`.
7. Crée un objet `Machine` nommé « Serveur1 » d'IP « 192.168.1.50 ».
8. Comment affiches-tu l'ip de cet objet ?
9. Deux objets de la même classe partagent-ils leurs valeurs ?
10. Qu'est-ce qu'un **attribut** ?

<details>
<summary>Réponses</summary>

1. La classe est le **moule** (le modèle) ; l'objet est un **exemplaire concret** fabriqué avec.
2. `class`.
3. C'est le **constructeur** : il range les données de l'objet ; appelé **automatiquement** à la création (`Machine(...)`).
4. L'**objet lui-même** (celui en train d'être créé/utilisé).
5. Il **range** la valeur `nom` dans l'objet, sous l'attribut `self.nom`.
6. `class Machine:` / `    def __init__(self, nom, ip):` / `        self.nom = nom` / `        self.ip = ip`.
7. `serveur = Machine("Serveur1", "192.168.1.50")`.
8. `print(serveur.ip)`.
9. Non : chaque objet a ses **propres** valeurs (indépendants).
10. Une **donnée rangée dans l'objet** (ex. `self.nom`, `self.ip`).

</details>
