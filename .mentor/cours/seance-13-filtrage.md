# Fiche de cours — Séance 13 : filtrer des lignes (`in`) & le piège de la sous-chaîne

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » (3/…). Thème : chercher/filtrer dans un fichier, comme un `grep`.

---

## 1. Le mot-clé `in` : chercher une sous-chaîne

`in` teste si un texte est **contenu dans** un autre. Il renvoie un booléen (`True`/`False`).

```python
texte = "bonjour le monde"
if "monde" in texte:
    print("trouve !")
```

## 2. Filtrer un fichier (l'équivalent de `grep`)

On combine `in` avec la lecture ligne par ligne :

```python
compteur = 0
with open("hosts.txt", "r") as f:
    for ligne in f:
        if "192.168.1." in ligne:
            print(ligne.strip())
            compteur += 1
print("il y a", compteur, "machine(s)")
```
→ n'affiche (et ne compte) que les lignes contenant le motif.

## 3. ⚠️ LE piège : `in` compare des caractères, pas du sens

`in` fait une recherche de **sous-chaîne brute**. Il ne « comprend » pas les IP, les mots, etc.

```python
"192.168.1" in "192.168.10.0"   # True !  (sur-matche)
```
Filtrer sur `"192.168.1"` attrape aussi `192.168.**10**.x`, qui est un **autre réseau**. C'est un vrai bug de parsing d'admin.

### La parade : rendre le motif plus précis
```python
"192.168.1." in "192.168.10.0"   # False  (après 192.168.1 il y a un 0, pas un point)
"192.168.1." in "192.168.1.0"    # True
```
Ajouter le **point** distingue `192.168.1.x` de `192.168.10.x`. Règle générale : plus le motif est spécifique, moins il sur-matche.

*(Pour des cas plus fins, on verra plus tard `.startswith()`, `.split()`, ou les expressions régulières.)*

---

## 4. Questions de révision (auto-test)

1. Que fait le mot-clé `in` entre deux chaînes ?
2. Quel type de valeur renvoie `"a" in "chat"` ?
3. Écris un filtre qui n'affiche que les lignes contenant « ERROR ».
4. Pourquoi `"192.168.1" in "192.168.10.0"` renvoie-t-il `True` ?
5. Comment corriger ce filtre pour ne PAS attraper `192.168.10.x` ?
6. `in` comprend-il qu'il s'agit d'une adresse IP ?
7. Que vaut `"cat" in "concatener"` ? Pourquoi est-ce un piège ?
8. Règle générale pour éviter le sur-matching ?
9. Quel est l'équivalent, côté terminal, de ce filtrage ?
10. Combine `in` et un compteur pour compter les lignes contenant « fail ».

<details>
<summary>Réponses</summary>

1. Il teste si la 1re chaîne est contenue (sous-chaîne) dans la 2e.
2. Un booléen (`True`/`False`).
3. `for ligne in f:` / `    if "ERROR" in ligne:` / `        print(ligne.strip())`.
4. Parce que les caractères « 192.168.1 » apparaissent littéralement au début de « 192.168.10.0 ».
5. Ajouter le point : filtrer `"192.168.1."` (exclut `192.168.10.x`).
6. Non : il compare seulement des caractères, sans notion de sens.
7. `True` — « cat » est dans « conCATener » : un mot peut être caché dans un autre → sur-matching.
8. Rendre le motif le plus spécifique possible (ajouter un séparateur comme un point, un espace…).
9. `grep`.
10. `compteur = 0` / `for ligne in f:` / `    if "fail" in ligne:` / `        compteur += 1`.

</details>
