# Fiche de cours — Séance 38 : mini-outil de supervision HTTP (`requests`)

> Support de révision (séance du 2026-09-22). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Compléments Python. Thème : surveiller un site/serveur en Python.

---

## 1. Le code de réponse HTTP : `status_code`

Quand `requests.get(url)` réussit à joindre le serveur, la réponse contient un **code HTTP** :

```python
import requests

reponse = requests.get("https://www.google.com")
print(reponse.status_code)   # 200
```

| Code | Sens |
|------|------|
| **200** | OK ✅ |
| 301 / 302 | redirection |
| 404 | page pas trouvée |
| 500 | erreur serveur |

Tester si un site répond bien :
```python
if reponse.status_code == 200:
    print("EN LIGNE")
else:
    print("Répond, mais code :", reponse.status_code)
```

## 2. Site injoignable = une EXCEPTION (pas un code)

Si le domaine n'existe pas, ou que le serveur est éteint, `requests.get` **ne renvoie aucun code** : il **plante** avec une exception. Il faut donc l'entourer d'un `try` / `except`.

L'exception à attraper : **`requests.exceptions.RequestException`** (la classe qui couvre toutes les erreurs réseau de `requests`).

```python
try:
    reponse = requests.get(url)
    ...
except requests.exceptions.RequestException:
    print("Site INJOIGNABLE")
```

## 3. L'outil complet (`site_online.py`)

```python
import requests

url = input("Entrer une URL : ")

try:
    reponse = requests.get(url)
    if reponse.status_code == 200:
        print("Le site est EN LIGNE (200)")
    else:
        print("Le site répond, code :", reponse.status_code)
except requests.exceptions.RequestException:
    print("Site INJOIGNABLE")
```

- `google.com` → `EN LIGNE (200)`
- `sitequinexistepas12345.org` → `INJOIGNABLE` (le `try`/`except` attrape le plantage)

## 4. Le bug "silencieux" à retenir

Une faute dans le nom de l'exception (`ReequestException`) **ne se voit pas** sur un site qui répond 200 : le `except` n'est jamais utilisé. Elle n'apparaît **que** quand on tombe sur le cas d'erreur.
→ **Toujours tester le chemin d'erreur**, pas seulement le cas qui marche.

## 5. Pourquoi c'est utile (infra / DevOps)
C'est le cœur d'un **monitoring** : un script comme ça, lancé toutes les X minutes (cron / tâche planifiée), permet d'alerter quand un serveur tombe.

---

## 6. Questions de révision (auto-test)

1. Que contient `reponse.status_code` ?
2. Que vaut ce code si tout va bien ?
3. Comment tester qu'un site répond correctement ?
4. Que se passe-t-il si le domaine n'existe pas — un code, ou autre chose ?
5. Quelle structure Python gère ce cas ?
6. Quel est le nom exact de l'exception à attraper avec `requests` ?
7. Pourquoi une faute dans le nom de l'exception peut rester invisible longtemps ?
8. Écris le squelette `try` / `except` autour d'un `requests.get`.
9. À quoi sert ce type d'outil en infra ?
10. Comment l'automatiser pour surveiller un serveur en continu ?

<details>
<summary>Réponses</summary>

1. Le code HTTP renvoyé par le serveur.
2. `200`.
3. `if reponse.status_code == 200:`.
4. Autre chose : `requests.get` **plante** (lève une exception), il ne renvoie pas de code.
5. `try` / `except`.
6. `requests.exceptions.RequestException`.
7. Elle n'est lue que dans le `except`, donc jamais déclenchée tant que tout va bien (code 200) — seul le cas d'erreur la révèle.
8. `try:` `    reponse = requests.get(url)` … `except requests.exceptions.RequestException:` `    print("injoignable")`.
9. Superviser / monitorer : détecter qu'un site ou serveur est tombé.
10. Le lancer périodiquement via une tâche planifiée / un cron.

</details>
