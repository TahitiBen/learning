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

**Phase 1 — Python fondamentaux : TERMINÉE** 🎉 (séance 10). **Phase 2 — Python pour l'infra** : module fichiers/parsing validé (bilan séance 17). **Phase 2 — Python pour l'infra** : bien couverte (fichiers, parsing, structuration en fonctions — séances 11-20). **Phase 3 — SQL : DÉMARRÉE** (séance 21, choix de Ruben). Outil : DB Browser for SQLite ; base `sql/machines.db`. Phase 0 (git) terminée.

## Concepts

### Acquis (sans indice, ≥ 2 fois)
- **Python types & règle guillemets = texte** (`str`/`int`/`float`/`bool`, `type()`) — corrigé seul en séance 2, puis répondu juste sans indice en révision séance 3.
- **Git : les 4 zones** (working directory → staging → repository → remote) — restituées correctement plusieurs séances de suite (5, 6, 7).
- **Git : `-u` (set upstream)** — enregistre la branche de destination du push ; compris et reformulé correctement séances 7 puis 9 (sans « fichiers »).

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
- **Python conditions `if`/`elif`/`else`** (indentation, comparaisons, `==` vs `=`, `and`/`or`) — `elif` écrit seul en séance 8 ; **`and` (dedans) vs `or` (dehors)** compris ; `else` sans condition (auto-diagnostiqué) ; `&` ≠ `and`. Presque solide, reconfirmer.
- **Python boucles `for`/`range` + `while`** — `for`/`range` séance 6 ; **`while` en validation** pratiqué séance 8 (redemander tant qu'invalide), réussi. À reconfirmer seul.
- **Python fonctions** (`def`, paramètre, `return`, appel `nom(arg)`) — vu séance 7. Définition acquise seul ; appel + `return` vs `print` compris après guidage. À recroiser sur un nouvel exemple.
- **Python `try`/`except`** (+ `ValueError`) — vu séance 9, structure correcte du 1er coup ; réutilisé séance 10. À recroiser.
- **Python `while True` + `break` + `continue`** — vu séance 10, assemblé en autonomie dans une boucle de saisie robuste. À reconfirmer.
- **mots logiques `and`/`or`/`not`** — enfin justes séance 10 (drill réussi). À garder espacé pour confirmer.
- **⚠️ Propreté du code** : tendance à laisser du code mort/redondant (le corrige quand pointé, pas encore repéré seul). À travailler en continu.
- **Python fichiers** (`open`/`with`/`read`/`write`, `\n`, chemin relatif = répertoire courant) — vu séance 11 ; **oublie les faits (modes `r`/`w`/`a`, chemin) entre séances** → garder en révision.
- **Python lecture ligne par ligne** (`for ligne in f:`, `.strip()`) + **compteur** (`+= 1`) — vu séance 12, assemblé correctement (bonne indentation avant/dans/après). À reconfirmer.
- **Python filtrage `if "x" in ligne:`** (grep-like) + **piège de sous-chaîne** (`"192.168.1"` matche `"192.168.10"` → parade : ajouter le point) — vu séance 13, fix trouvé avec 1 indice. À recroiser.
- **Python `.split()` + listes + indexation `[i]` (commence à 0) + appel de méthode `()`** — vu séance 14, assemblé après guidage (scalabilité + `.strip()` vs `.strip`). À recroiser.
- **Python écrire un rapport** (2 fichiers ouverts en même temps, `f.write` d'une chaîne construite avec `+`, `\n`) — vu séance 15, cycle read→parse→write complet. À recroiser.
- **Python `import` + module `datetime`** (`datetime.datetime.now()`, `.strftime(...)`) — vu séance 16, réussi seul. À recroiser.
- **⚠️ Nommage des variables** (a nommé une variable `là`) — point de style récurrent à travailler.
- **⚠️ ARCHITECTURE de programme** (révélé par le projet-bilan séance 17) : les concepts isolés sont solides, mais **assembler un programme multi-étapes en autonomie** est fragile (quoi mettre avant/dans/après la boucle, stocker l'input, une logique vs branches en dur, écrire DANS la boucle). → point n°1 à travailler, d'où le passage aux fonctions.
- **Compréhension `if <expression>`** : a compris qu'un `if` agit sur toute expression valant True/False (ex. `if reseau + "." in ligne:`), et la version 2 lignes (`motif = reseau + "."`). Bon réflexe : extraire une condition dense dans une variable.
- **Structurer avec des fonctions** — 2 extractions (`est_sur_reseau`, `formater_machine`) + **fonction principale `auditer(reseau)` + `if __name__ == "__main__"`** (séance 20). Refactor complet réussi. Applique les conventions seul (`import` en haut). **Architecture = désormais un point fort.** `if __name__ == "__main__"` compris dans le principe, à recroiser (abstrait).
- **SQL : `CREATE TABLE` + `INSERT`** (types `INTEGER`/`TEXT`, `PRIMARY KEY` auto, guillemets simples ; base = fichier `.db`) — vu séance 21 (réactivation du BTS). Compris : CREATE une fois vs INSERT répétable. À recroiser.

### Acquis récents
- **`a` = append** : confirmé 2 fois (séances 15 & 16) → **acquis**.
- **Module fichiers/parsing** (read, ligne par ligne, filtrage `in`+point, `split`+index, write, rapport daté) — **validé par le projet-bilan** séance 17.

### À voir (prochainement)
- **SQL `SELECT`** : `SELECT * FROM`, `WHERE` (filtrer), `ORDER BY`. Puis `UPDATE`/`DELETE`, agrégations (`COUNT`, `GROUP BY`), jointures. Plus tard : relier SQL à Python (`sqlite3`).
- Compléments Python en attente : `pathlib`, `pip`, POO.
- NB : scripts Python renommés `01_`…`13_` ; base SQL = `sql/machines.db`.

## Points d'attention pédagogiques
- Ne pas s'attarder sur la théorie : donner un exemple minimal puis passer vite à la pratique.
- Exploiter son bagage SISR : ancrer les exercices dans des cas système/réseau qui lui parlent.
- Rythme court (1 h) : viser 1 concept + 1 exercice par séance, pas plus.
- **Demande explicite de Ruben (séance 4) : NE JAMAIS lâcher un point non maîtrisé.** Le remettre en révision à CHAQUE séance jusqu'à ancrage complet (ex. noms des 3 zones de git). Privilégier la restitution active (lui faire redire/reproduire) plutôt que de simplement re-répéter.
- Se décourage vite quand il bloque → décomposer, valoriser ce qui est déjà juste.
