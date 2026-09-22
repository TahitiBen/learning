# Fiche de cours — Séance 37 : `pip` & modules externes (`requests`)

> Support de révision (séance du 2026-09-22). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Compléments Python. Thème : élargir Python avec des bibliothèques de la communauté.

---

## 1. `pip` : installer des bibliothèques

- La **bibliothèque standard** (`sqlite3`, `datetime`, `os`…) est livrée avec Python.
- **PyPI** est le dépôt central des bibliothèques créées par la communauté (des centaines de milliers).
- **`pip`** = le gestionnaire de paquets de Python :
```
pip install requests
python -m pip install requests   # si "pip" n'est pas reconnu
```

## 2. `requests` : parler à des sites / API en HTTP

```python
import requests

reponse = requests.get("https://api.ipify.org?format=json")
print(reponse.json())     # {'ip': '80.75.x.x'}
```
- `requests.get(url)` envoie une requête **HTTP GET** et renvoie une **réponse**.
- `.json()` transforme la réponse (du JSON) en objet Python (souvent un **dictionnaire**).
- Utile aussi : `reponse.status_code` (200 = OK, 404 = pas trouvé…), `reponse.text` (le contenu brut).

## 3. Accéder à un champ (dictionnaire)

`reponse.json()` renvoie souvent un **dict** → on accède par clé :
```python
donnees = reponse.json()      # {'ip': '80.75.x.x'}
print(donnees["ip"])          # 80.75.x.x
```

## 4. Pourquoi c'est utile (infra / DevOps)
Appeler des **API** = récupérer des données, piloter des services, superviser… C'est un pilier de l'automatisation moderne.

---

## 5. Questions de révision (auto-test)

1. Quelle commande installe une bibliothèque externe ?
2. C'est quoi PyPI ?
3. Différence entre bibliothèque standard et externe ?
4. Quelle bibliothèque pour faire des requêtes HTTP ?
5. Que fait `requests.get(url)` ?
6. Que fait `.json()` sur une réponse ?
7. Comment récupérer la valeur de la clé `"ip"` dans le dict renvoyé ?
8. Que vaut `reponse.status_code` si tout va bien ?
9. Écris les 2 lignes qui installent puis importent `requests`.
10. En quoi appeler des API est-il utile en infra/DevOps ?

<details>
<summary>Réponses</summary>

1. `pip install <paquet>` (ou `python -m pip install <paquet>`).
2. Le dépôt central des bibliothèques Python de la communauté.
3. La standard est livrée avec Python ; l'externe s'installe avec `pip`.
4. `requests`.
5. Elle envoie une requête HTTP GET et renvoie une réponse.
6. Elle transforme le JSON de la réponse en objet Python (souvent un dict).
7. `reponse.json()["ip"]`.
8. `200`.
9. `pip install requests` (terminal) puis `import requests` (dans le script).
10. Pour récupérer des données et piloter des services automatiquement (supervision, intégrations…).

</details>
