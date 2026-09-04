# Séance 26 — 2026-08-02 — RÉVISION PYTHON (série de TP)

## Objectif
À la demande de Ruben (se sentait rouillé, « oublié une grande partie ») : révision Python complète via une **série de TP pratiques** (son mode d'apprentissage), avant de réviser le SQL.

## Quiz initial (diagnostic)
- **Solide** : types (`int`/`str`), `range` (borne exclue), `input`+`int`.
- **Fragile/oublié** : `or` pour « dehors » (a répondu `and`), l'**appel** de fonction / `return` (confusion), le nom `ValueError`, les **fichiers**, `if __name__ == "__main__"`.

## TP réalisés
- **TP1 (variables/opérateurs/print)** : erreurs `:` au lieu de `/` (division), et `print` avec éléments **juxtaposés** sans virgule ni `+`. Recadré (division `/` ; print via virgules OU `+ str()`). Réussi.
- **TP2 (input + conditions)** : réussi du 1er coup (`float(input())`, `if`/`elif`/`else`).
- **TP3 (boucles + compteur)** : a d'abord réutilisé la variable de boucle `k` comme total (juste **par coïncidence**) → recadré vers un **vrai compteur** robuste. Réussi.
- **TP4 (fonctions)** : réussi du 1er coup (2 paramètres, `return`, 2 appels).
- **TP5 (try/except)** : réussi (`str(val)` redondant signalé).
- **TP6 (fichiers)** : point oublié — a d'abord juste compté sans **afficher** les lignes → ajout de `print(ligne.strip())`. Réussi. Fichiers ré-ancrés.
- **TP7 (capstone : fonction + `while True` + `break` + input)** : a oublié à quoi sert `while True` (ré-expliqué) ; puis bug `float(pour)` **non stocké** → passait une chaîne à la fonction → `TypeError`. Recadré : **convertir ET stocker** (`pour = float(pour)`). Réussi.

## Récurrents ré-ancrés
- **Convertir ET stocker** (`x = int(x)` / `float(...)`) — sinon la conversion est perdue (revu en TP7, cf. `int(nb)` vs `nb=int(nb)`).
- **`print` texte + variables** : virgules (auto-espaces) OU `+` avec `str()`.
- **Vrai compteur** vs réutiliser la variable de boucle.
- **Appel de fonction** (mettre la logique DANS la fonction + l'appeler).

## À surveiller encore (garder en révision)
- `while True` (oublié en cours de route), `or` pour « dehors », `if __name__ == "__main__"`, nom `ValueError`, division `/`.

## Concepts — bilan
- Refresh Python réussi : les fondamentaux sont **réactivés** et reconfirmés en pratique (variables, opérateurs, input/conditions, boucles/compteur, fonctions, try/except, fichiers, while True/break). Plusieurs pièges récurrents ré-ancrés par la pratique.

## Prochaine étape prévue
**Révision SQL** (comme demandé par Ruben) : quiz + quelques requêtes pratiques sur toute la Phase 3 (CREATE/INSERT/SELECT/WHERE/LIKE/ORDER BY/UPDATE/DELETE/COUNT/GROUP BY/ALTER). Puis reprise du cours SQL aux **jointures (`JOIN`)**.
