# Fiche de cours — Séance 3 : Python — les opérateurs

> Support de révision (séance du 2026-07-20). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Thème : opérateurs arithmétiques, priorité, et un piège classique (`^`).

---

## 1. Les opérateurs arithmétiques

| Opérateur | Rôle | Exemple | Résultat |
|---|---|---|---|
| `+` | addition | `10 + 3` | `13` |
| `-` | soustraction | `10 - 3` | `7` |
| `*` | multiplication | `10 * 3` | `30` |
| `/` | division | `10 / 3` | `3.33…` (toujours un **float**) |
| `//` | division entière | `10 // 3` | `3` (on jette la partie décimale) |
| `%` | modulo (le **reste**) | `10 % 3` | `1` |
| `**` | puissance | `2 ** 3` | `8` |

À retenir en priorité :
- **`**`** = puissance (deux étoiles collées).
- **`%`** (modulo) = le **reste** d'une division. Très utile : tester pair/impair (`n % 2 == 0`), gérer des cycles, etc.
- **`/`** renvoie toujours un `float` (`10 / 2` → `5.0`), alors que **`//`** garde un entier.

## 2. Priorité des opérateurs

Comme en maths :
1. les **parenthèses** d'abord,
2. puis `**` (puissance),
3. puis `*`, `/`, `//`, `%`,
4. puis `+`, `-`.

→ Les **parenthèses** servent à forcer l'ordre. Exemple : dans `2 ** (32 - 24) - 2`, on veut que `32 - 24` soit calculé **avant** la puissance, d'où les parenthèses autour.

## 3. ⚠️ Piège : `^` n'est PAS la puissance en Python

- En maths et dans Excel, `^` signifie « puissance ». **Pas en Python.**
- En Python, `^` est un opérateur **binaire** (XOR) → il donne des résultats surprenants si on l'utilise pour une puissance.
- **La puissance en Python, c'est `**`.**

## 4. Rappel : `+` dépend du type

- Sur des **nombres**, `+` additionne : `2 + 2` → `4`.
- Sur des **chaînes** (`str`), `+` **colle** (concatène) : `"2" + "2"` → `"22"`.

## 5. Cas pratique vu en cours : hôtes utilisables d'un sous-réseau

Formule réseau : `hôtes utilisables = 2 ** (32 - préfixe) - 2`
(le `- 2` exclut l'adresse réseau et l'adresse de broadcast).

```python
prefixe = 24
print(2 ** (32 - prefixe) - 2)   # 254
```
- `/24` → 254 hôtes ; `/26` → 62 hôtes ; `/30` → 2 hôtes.

---

## 6. Questions de révision (auto-test)

1. Quel opérateur donne la **puissance** en Python ? Et lequel NE faut-il PAS utiliser pour ça ?
2. Que fait l'opérateur `%` (modulo) ?
3. Quelle est la différence entre `/` et `//` ?
4. Combien vaut `10 / 2` exactement, et de quel type est le résultat ?
5. Dans quel ordre Python évalue-t-il `2 + 3 * 4` ? Quel résultat ?
6. Comment forcer `2 + 3` à être calculé avant la multiplication dans `(...) * 4` ?
7. Combien vaut `7 % 2` ? À quoi ce test sert-il souvent ?
8. Que vaut `2 ** (32 - 30) - 2` ? (pense sous-réseau /30)
9. Que vaut `"3" + "4"` ? Et `3 + 4` ?
10. Pourquoi met-on des parenthèses dans `2 ** (32 - prefixe) - 2` ?

<details>
<summary>Réponses</summary>

1. Puissance = `**`. À ne PAS utiliser : `^` (c'est un XOR binaire en Python).
2. Il donne le **reste** d'une division entière.
3. `/` = division normale (renvoie un `float`) ; `//` = division entière (jette la décimale).
4. `5.0`, de type `float`.
5. La multiplication d'abord : `3 * 4 = 12`, puis `2 + 12 = 14`.
6. En mettant des parenthèses : `(2 + 3) * 4` → `20`.
7. `7 % 2` = `1`. Sert souvent à tester si un nombre est pair/impair (`n % 2 == 0` → pair).
8. `2 ** 2 - 2` = `4 - 2` = `2` (un /30 offre 2 hôtes utilisables).
9. `"3" + "4"` → `"34"` (collage) ; `3 + 4` → `7` (addition).
10. Pour que `32 - prefixe` soit calculé **avant** la puissance (sinon la priorité ferait la puissance d'abord).

</details>
