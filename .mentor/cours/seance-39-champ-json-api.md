# Fiche de cours — Séance 39 : lire un champ précis d'une API JSON

> Support de révision (séance du 2026-09-22). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Compléments Python. Thème : extraire une valeur précise d'une réponse d'API.

---

## 1. `.json()` renvoie un dictionnaire

`requests.get(url).json()` transforme la réponse JSON en **dictionnaire Python**.
Dans un dict, on lit une valeur par sa **clé, entre crochets** :

```python
import requests

reponse = requests.get("https://api.github.com/users/TahitiBen")
donnees = reponse.json()          # {'login': 'TahitiBen', 'public_repos': 1, 'created_at': '2024-...', ...}

print(donnees["public_repos"])    # 1
print(donnees["created_at"])      # 2024-01-15T10:42:43Z
```

- `donnees["public_repos"]` → va chercher **la valeur** rangée sous la clé `"public_repos"`.
- La clé doit être écrite **exactement** comme dans le JSON (au caractère près).

## 2. Découvrir les clés disponibles

Avant de piocher, on peut afficher tout le dict une fois :

```python
print(donnees)     # on lit les clés, puis on choisit celles qui nous intéressent
```

## 3. Le script complet (`github_info.py`)

```python
import requests

reponse = requests.get("https://api.github.com/users/TahitiBen")
donnees = reponse.json()

print("Dépôts publics :", donnees["public_repos"])
print("Compte créé le :", donnees["created_at"])
```

## 4. Pourquoi c'est utile (infra / DevOps)
Toutes les API renvoient du JSON. Savoir en extraire **le champ qui t'intéresse** (état d'un service, IP, nombre d'alertes, statut d'un build…) = la base de l'automatisation et de la supervision.

---

## Rappel SQL de la séance — `UPDATE` (production à froid)

```sql
UPDATE machines SET ip = '192.168.1.50' WHERE nom = 'Serveur1';
```

- **4 morceaux** : `UPDATE` table → `SET` colonne = valeur → `WHERE` condition.
- Cibler par la **bonne colonne** (`nom`, pas `ip`) pour ne toucher que la bonne ligne.
- **Règle d'or** : jamais d'`UPDATE`/`DELETE` sans `WHERE`.
- Valeurs texte entre **guillemets simples**, et **au caractère près** (`'Server1'` ≠ `'Serveur1'`).

---

## 5. Questions de révision (auto-test)

1. Que renvoie `reponse.json()` comme type Python ?
2. Comment lit-on une valeur dans un dictionnaire ?
3. Écris la ligne qui récupère la valeur de la clé `"public_repos"`.
4. Que se passe-t-il si tu écris mal la clé ?
5. Comment voir toutes les clés d'un JSON inconnu ?
6. Pourquoi savoir lire un champ JSON est-il utile en infra ?
7. Cite les 4 morceaux d'une requête `UPDATE`.
8. Sur quelle colonne cibler pour modifier la machine « Serveur1 » ?
9. Quelle règle d'or ne jamais oublier avec `UPDATE` / `DELETE` ?
10. `'Server1'` et `'Serveur1'` : le `=` SQL les considère-t-il identiques ?

<details>
<summary>Réponses</summary>

1. Un **dictionnaire** (dict).
2. Par sa **clé, entre crochets** : `dict["cle"]`.
3. `donnees["public_repos"]`.
4. Erreur `KeyError` (la clé n'existe pas) — la clé doit être exacte.
5. `print(donnees)` (ou `print(reponse.json())`).
6. Les API renvoient du JSON ; extraire le bon champ = base de l'automatisation/supervision.
7. `UPDATE` table / `SET` colonne = valeur / `WHERE` condition.
8. La colonne `nom` : `WHERE nom = 'Serveur1'`.
9. **Toujours un `WHERE`** (sinon toutes les lignes sont modifiées).
10. Non : le `=` cherche une correspondance **exacte**, ils sont différents.

</details>
