# PROGRESSION — Ruben

> État global de l'élève. Mis à jour à la fin de chaque séance.
> Règle : un concept n'est **acquis** que s'il a été utilisé correctement **sans indice**, dans au moins **deux exercices espacés dans le temps**.

## Profil

- **Élève :** Ruben
- **Bagage :** BTS SIO option SISR (systèmes, réseaux, infra). À l'aise en informatique générale.
- **Déjà pratiqué :** Windows Server 2022/2025, Active Directory, pare-feu Windows Defender, Linux (ArchLinux + Hyprland, Debian 12/13), Windows 10/11, winget, PowerShell 7 (scripts simples), Bash (scripts simples). Notions connues mais **non maîtrisées**.
- **Terminal :** à l'aise. Tape à dix doigts sans regarder.
- **Objectif :** explorer les domaines de l'informatique pour trouver son orientation, viser ce qui **recrute**, avec une appétence forte pour **système & réseau**.
- **Temps :** ~1 h/semaine en moyenne, flexible (parfois plus quand motivé).
- **Style d'apprentissage :** apprend **en pratiquant**. La théorie l'ennuie et ne s'ancre qu'**après** la pratique. → ~20 % théorie / 80 % pratique, sessions courtes, exercices orientés infra/réseau quand c'est possible.

## Phase actuelle

**Phase 1 — Python fondamentaux** (en cours, séance 8). Phase 0 (environnement & git) terminée. 🎉 1er programme complet réalisé (mini-projet subnet interactif).

## Concepts

### Acquis (sans indice, ≥ 2 fois)
- **Python types & règle guillemets = texte** (`str`/`int`/`float`/`bool`, `type()`) — corrigé seul en séance 2, puis répondu juste sans indice en révision séance 3.
- **Git : les 4 zones** (working directory → staging → repository → remote) — restituées correctement plusieurs séances de suite (5, 6, 7).

### Fragiles (vus, mais avec indice ou une seule fois)
- **Terminal / navigation** : `cd`, `mkdir`, `ls`, `Copy-Item`, `$HOME`, `~` — vus aujourd'hui, à consolider.
- **Git de base** : `git clone`, `git status`, notion de repo / remote / branche `main` — vus aujourd'hui.
- **`.gitkeep` / dossiers vides invisibles pour git** — compris aujourd'hui.
- **Cycle git `add` → `commit` → `push`** : commandes bien retenues (séance 2) ; mais **noms des 3 zones**, `.gitkeep` et `-u` **oubliés** à la révision → à recroiser.
- **Python `print`** : affichage, chaînes entre guillemets — vu séance 2. Découverte de `print(val, "texte")`.
- **Python variables & types** (`str`/`int`/`float`/`bool`, `type()`) — vu séance 2. Piège **guillemets = texte** rencontré et corrigé seul ; à confirmer une 2e fois.
- **Exécuter un script** (`python fichier.py`) — vu séance 2.
- **Python opérateurs** (`+ - * / // % **`, priorité, parenthèses) — vu séance 3, reconsolidé séance 4 (révision juste). Presque acquis.
- **Python `input()` + conversion `int(input(...))`** — vu séance 4, réussi sans blocage. À confirmer une 2e fois. Rappel : `input()` renvoie toujours un `str`.
- **Git : `-u` (set upstream)** — enfin compris séance 7 (fausse piste « fichiers » levée : c'est l'adresse de destination, mémorisée au 1er push). Confirmer 1 dernière fois.
- **Python conditions `if`/`elif`/`else`** (indentation, comparaisons, `==` vs `=`, `and`/`or`) — `elif` écrit seul en séance 8 ; **`and` (dedans) vs `or` (dehors)** compris ; `else` sans condition (auto-diagnostiqué) ; `&` ≠ `and`. Presque solide, reconfirmer.
- **Python boucles `for`/`range` + `while`** — `for`/`range` séance 6 ; **`while` en validation** pratiqué séance 8 (redemander tant qu'invalide), réussi. À reconfirmer seul.
- **Python fonctions** (`def`, paramètre, `return`, appel `nom(arg)`) — vu séance 7. Définition acquise seul ; appel + `return` vs `print` compris après guidage. À recroiser sur un nouvel exemple.

### À voir (prochainement)
- Gestion d'erreurs (`try`/`except`) pour rendre le programme increvable (saisie non numérique) → fin de Phase 1. Puis Phase 2 (fichiers, modules) ou démarrage SQL.

## Points d'attention pédagogiques
- Ne pas s'attarder sur la théorie : donner un exemple minimal puis passer vite à la pratique.
- Exploiter son bagage SISR : ancrer les exercices dans des cas système/réseau qui lui parlent.
- Rythme court (1 h) : viser 1 concept + 1 exercice par séance, pas plus.
- **Demande explicite de Ruben (séance 4) : NE JAMAIS lâcher un point non maîtrisé.** Le remettre en révision à CHAQUE séance jusqu'à ancrage complet (ex. noms des 3 zones de git). Privilégier la restitution active (lui faire redire/reproduire) plutôt que de simplement re-répéter.
- Se décourage vite quand il bloque → décomposer, valoriser ce qui est déjà juste.
