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

**Phase 1 — Python fondamentaux** (en cours, séance 5). Phase 0 (environnement & git) terminée.

## Concepts

### Acquis (sans indice, ≥ 2 fois)
- **Python types & règle guillemets = texte** (`str`/`int`/`float`/`bool`, `type()`) — corrigé seul en séance 2, puis répondu juste sans indice en révision séance 3.

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
- **Git : noms des 3 zones** — restitués en entier séances 4 et 5 (léger pointage). Presque acquis, reconfirmer 1 fois encore.
- **Git : `-u` (set upstream)** — toujours oublié (3 fois). À driller en priorité.
- **Python conditions** (`if`/`else`, `:` + indentation, comparaisons `== != < > <= >=`, `and`) — vu séance 5, réussi (guidage sur la 2e borne). `==` vs `=` signalé. `elif` pas encore pratiqué. À recroiser.

### À voir (prochainement)
- Python : boucles (`while`, `for`, `range`), `elif` en pratique ; puis fonctions.

## Points d'attention pédagogiques
- Ne pas s'attarder sur la théorie : donner un exemple minimal puis passer vite à la pratique.
- Exploiter son bagage SISR : ancrer les exercices dans des cas système/réseau qui lui parlent.
- Rythme court (1 h) : viser 1 concept + 1 exercice par séance, pas plus.
- **Demande explicite de Ruben (séance 4) : NE JAMAIS lâcher un point non maîtrisé.** Le remettre en révision à CHAQUE séance jusqu'à ancrage complet (ex. noms des 3 zones de git). Privilégier la restitution active (lui faire redire/reproduire) plutôt que de simplement re-répéter.
- Se décourage vite quand il bloque → décomposer, valoriser ce qui est déjà juste.
