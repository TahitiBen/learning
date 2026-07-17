# Fiche de cours — Séance 1 : Terminal & Git

> Support de révision (séance du 2026-07-17). Pensé pour être relu ou importé dans un outil de quiz (NotebookLM, Anki…).
> Thème : prendre en main le terminal et les bases de git, jusqu'au premier commit/push.

---

## 1. Le terminal

### Définitions
- **Terminal** : application où l'on tape des commandes texte pour piloter l'ordinateur (ici : PowerShell sur Windows).
- **Répertoire courant** (*current / working directory*) : le dossier dans lequel le terminal est « posé » à un instant donné. Le début de la ligne l'indique (ex. `PS C:\Users\ben\Documents\learning>`).
- **Répertoire personnel** (*home*) : ton dossier utilisateur, ex. `C:\Users\ben`.

### Commandes de navigation
| Commande | Sens | Rôle |
|---|---|---|
| `cd <dossier>` | *change directory* | Se déplacer dans un dossier |
| `cd ~` | — | Aller dans le répertoire personnel (le `~` = home) |
| `mkdir <nom>` | *make directory* | Créer un dossier |
| `mkdir a, b, c` | — | Créer plusieurs dossiers d'un coup (PowerShell) |
| `mkdir dossier\sous-dossier` | — | Créer des dossiers imbriqués en une fois |
| `ls` | *list* | Lister le contenu du dossier courant |
| `Copy-Item <source> <destination>` | — | Copier un fichier (PowerShell) |

### Raccourcis / repères utiles
- **`~`** = répertoire personnel. **`$HOME`** = même chose (variable). **`.`** = « le dossier courant ».
- Touche **Tab** = auto-complète les noms de dossiers/fichiers → évite les fautes de frappe dans les chemins.
- Dans la sortie de `ls`, la colonne **Mode** : commence par **`d`** = un dossier (*directory*), par **`-`** = un fichier.
- Le terminal est **littéral** : une lettre de travers (ex. `Dwnloads` au lieu de `Downloads`) et il refuse. Il ne devine jamais.

### Convention : les noms commençant par un point
Un nom qui commence par `.` (ex. `.git`, `.mentor`, `.gitkeep`) est un élément de **configuration**, « caché » par convention. Ce sont des dossiers/fichiers normaux.

---

## 2. Git — les concepts

### Définitions
- **Git** : logiciel de **gestion de versions** (*version control*). Il enregistre l'historique des changements d'un projet.
- **Dépôt / repository (repo)** : un projet suivi par git.
- **Remote** : le dépôt distant (ici sur GitHub) — la copie « en ligne ».
- **Cloner** (*clone*) : télécharger une copie complète d'un dépôt distant sur sa machine.
- **Branche** (*branch*) : une ligne de développement. La branche par défaut s'appelle en général **`main`**.
- **Commit** : un **instantané** (snapshot) daté du projet, accompagné d'un message. Les commits forment l'**historique**.
- **Push** : envoyer ses commits locaux vers le remote (GitHub).

### Les 3 zones de git (à connaître par cœur)
1. **Working directory** — ton dossier de travail (où tu crées/modifies les fichiers).
2. **Staging area / index** — la « zone de préparation » : ce que tu as **choisi** d'inclure dans le prochain commit.
3. **Repository** — le dépôt local, où les commits sont figés.

Puis, séparément : **remote** (GitHub), atteint via `push`.
Flux : *working dir* → (`git add`) → *staging* → (`git commit`) → *repo local* → (`git push`) → *remote*.

### Pourquoi `.gitkeep` ?
Git **ne suit que les fichiers, pas les dossiers vides** : un dossier vide est invisible pour lui. Pour forcer git à conserver un dossier vide, on y met un fichier vide nommé **`.gitkeep`** (simple convention).

---

## 3. Git — les commandes

| Commande | Rôle |
|---|---|
| `git --version` | Vérifier que git est installé et sa version |
| `git clone <url> .` | Cloner un dépôt dans le dossier courant (le `.`) |
| `git status` | Voir l'état : fichiers suivis, en attente, branche |
| `git add .` | Ajouter tout à la zone de préparation (staging) |
| `git commit -m "message"` | Figer un instantané avec un message |
| `git push -u origin main` | 1er envoi : pousser + mémoriser la destination (`-u`) |
| `git push` | Envois suivants (destination déjà mémorisée) |

### Lire `git status`
- **Untracked files** (rouge) = fichiers non suivis, pas encore ajoutés.
- **Changes to be committed** (vert) = fichiers stagés, prêts pour le commit.

### Convention de message de commit
Format : **`type: description courte à l'impératif`**
Types utiles : `chore` (config/technique), `feat` (ajout), `fix` (correction), `docs` (documentation), `exo` (exercice terminé).
Exemple : `chore: initialise l'environnement et la memoire du prof`.
Astuce Windows : éviter les accents dans les messages de commit (soucis d'encodage).

---

## 4. Questions de révision (auto-test)

1. Quelle commande affiche le contenu du dossier courant ?
2. Que signifie le `.` à la fin de `git clone <url> .` ?
3. Cite les 3 zones de git dans l'ordre et la commande qui fait passer de l'une à l'autre.
4. Pourquoi un dossier vide n'apparaît-il pas dans git, et comment y remédier ?
5. Dans la sortie de `ls`, comment distingues-tu un dossier d'un fichier ?
6. À quoi sert l'option `-u` dans `git push -u origin main`, et pourquoi n'en a-t-on plus besoin ensuite ?
7. Qu'est-ce qu'un commit, en une phrase ?
8. Donne un message de commit correct selon notre convention pour « ajout d'un exercice sur les boucles ».
9. Quel raccourci du terminal évite les fautes de frappe dans les chemins ?
10. Quelle est la différence entre un dépôt **local** et le **remote** ?

<details>
<summary>Réponses</summary>

1. `ls`.
2. « Cloner dans le dossier courant » (au lieu de créer un sous-dossier).
3. Working directory →(`git add`)→ staging →(`git commit`)→ repository (local) ; puis `git push` → remote.
4. Git ne suit que les fichiers, pas les dossiers vides ; on ajoute un fichier `.gitkeep` dedans.
5. La colonne **Mode** : `d…` = dossier, `-…` = fichier.
6. `-u` mémorise la destination (`origin main`) comme upstream par défaut ; ensuite `git push` seul suffit.
7. Un instantané daté du projet accompagné d'un message décrivant le changement.
8. Ex. : `exo: ajoute un exercice sur les boucles`.
9. La touche **Tab** (auto-complétion).
10. Le **local** est la copie sur ta machine ; le **remote** est la copie en ligne (GitHub), synchronisée via `push`/`pull`.

</details>
