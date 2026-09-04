# Séance 27 — 2026-08-02 — RÉVISION SQL (Phase 3)

## Objectif
Révision SQL à la demande de Ruben (après la révision Python) : 6 requêtes pratiques sur `machines.db` couvrant SELECT/WHERE/LIKE, COUNT, GROUP BY, ORDER BY, UPDATE, INSERT, DELETE.

## Déroulé & erreurs (rappel à froid rouillé)
- A d'abord **oublié comment ouvrir DB Browser** / la base → rappelé (Démarrer → DB Browser → Ouvrir une base → machines.db).
- **Q1** : `SELECT nom WHERE reseau LIKE 192.168.1` → oubli du `FROM machines`, pas de guillemets, `LIKE` au lieu de `=` sur la colonne `reseau` (valeur exacte). Corrigé : `SELECT * FROM machines WHERE reseau = '192.168.1';`.
- **Q2** COUNT total : **juste**.
- **Q3** : `SELECT *, COUNT(*) ... GROUP BY` → recadré vers `SELECT reseau, COUNT(*) ... GROUP BY reseau`.
- **Q4** ORDER BY nom DESC : **juste**.
- **Q5** UPDATE ip WHERE ip = ... : **juste** (WHERE présent, bonne ligne ciblée ; ciblage par ip au lieu du nom, signalé).
- **Q6** : `INSERT INTO table` (placeholder laissé) + `DELETE ... WHERE nom = Test-Rev` (guillemets manquants) → corrigé (`machines`, `'Test-Rev'`). Puis juste.

## Diagnostic
- **Reconnaissance OK avec une référence** (l'antisèche a débloqué la plupart des requêtes), mais **production à froid rouillée**.
- Points fragiles à froid : le **`FROM`**, les **guillemets simples**, **`=` vs `LIKE`** (exact vs motif), **`SELECT col, COUNT(*)`** (pas `*`) en GROUP BY, **`WHERE`** obligatoire, utiliser le **vrai nom de table** (pas le placeholder).
- A eu besoin qu'on redonne les consignes + une antisèche → normal pour une réactivation.

## Reco pédagogique
- Faire **écrire des requêtes à froid** régulièrement (sans antisèche) pour ancrer la production, pas seulement la reconnaissance. Recroiser : FROM, guillemets, `=` vs LIKE.

## Bilan
- Python (séance 26) + SQL (séance 27) **révisés**. SQL : les concepts sont là, la syntaxe à froid demande encore de la pratique.

## Prochaine étape prévue
Reprendre le **cours SQL aux jointures (`JOIN`)** : créer une 2e table (ex. `reseaux`) et la joindre à `machines`. Continuer à driller la production de requêtes à froid.
