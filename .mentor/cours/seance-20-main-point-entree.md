# Fiche de cours — Séance 20 : fonction principale & `if __name__ == "__main__"`

> Support de révision (séance du 2026-08-02). Prêt pour relecture ou import dans un outil de quiz (NotebookLM, Anki…).
> Module « Python pour l'infra » — structuration (3, finale).

---

## 1. Emballer le code principal dans une fonction

Au lieu de laisser le gros bloc « en vrac » à la fin, on l'enveloppe dans une fonction (ex. `auditer(reseau)`). Bénéfices :
- **Réutilisation** : on peut l'appeler plusieurs fois → `auditer("192.168.1")`, `auditer("10.0.0")`…
- **Importabilité** : un autre script peut réutiliser la fonction (`from monfichier import auditer`).
- **Lisibilité** : le fichier se lit comme « voici mes outils, voici comment ça se lance ».

*(Sur un mini-script le gain est modeste, mais c'est l'habitude qui passe à l'échelle.)*

## 2. Le point d'entrée : `if __name__ == "__main__":`

`__name__` est une variable cachée que Python remplit automatiquement :
- fichier **lancé directement** (`python fichier.py`) → `__name__ == "__main__"` → la condition est **vraie**, le code de lancement s'exécute ;
- fichier **importé** par un autre → `__name__` = le nom du module → condition **fausse**, le code de lancement **ne s'exécute pas** (seules les fonctions sont chargées).

But : **séparer les outils réutilisables du code de lancement**. Sans ce garde-fou, importer le fichier pour réutiliser une fonction déclencherait aussi l'`input()` et tout le programme.

## 3. La structure complète (référence)

```python
import datetime

def est_sur_reseau(ligne, reseau):
    return reseau + "." in ligne

def formater_machine(morceau):
    return "Machine : " + morceau[0] + " - IP : " + morceau[1].strip() + "\n"

def auditer(reseau):
    maintenant = datetime.datetime.now()
    compteur = 0
    with open("hosts.txt", "r") as entree, open("audit.txt", "w") as sortie:
        sortie.write("Audit du reseau " + reseau + " - genere le " + maintenant.strftime("%d/%m/%Y %Hh%M") + "\n")
        for ligne in entree:
            morceau = ligne.split(":")
            if est_sur_reseau(ligne, reseau):
                sortie.write(formater_machine(morceau))
                compteur += 1
        if compteur == 0:
            print("Aucune machine sur ce reseau")
        sortie.write("Total : " + str(compteur) + " machine(s)\n")

if __name__ == "__main__":
    reseau = input("Donner le reseau a auditer (ex. 192.168.1) : ")
    auditer(reseau)
```
Ordre : imports → fonctions utilitaires → fonction principale → point d'entrée.

---

## 4. Questions de révision (auto-test)

1. Cite deux bénéfices d'emballer le code principal dans une fonction.
2. Que vaut `__name__` quand on lance le fichier directement ?
3. Que vaut `__name__` quand le fichier est importé par un autre ?
4. Que se passerait-il, sans le garde-fou, si on importait le fichier pour réutiliser `auditer` ?
5. Où placer le code de lancement (input + appel) ?
6. Comment appeler `auditer` sur trois réseaux différents ?
7. Dans quel ordre organise-t-on le fichier ?
8. `if __name__ == "__main__":` s'exécute-t-il quand le fichier est importé ?
9. Pourquoi dit-on que la fonction rend le code « réutilisable » ?
10. En une phrase : à quoi sert `if __name__ == "__main__":` ?

<details>
<summary>Réponses</summary>

1. Réutilisation (l'appeler plusieurs fois), importabilité, lisibilité (deux au choix).
2. `"__main__"`.
3. Le nom du module (le nom du fichier).
4. L'import déclencherait l'`input()` et lancerait tout le programme, au lieu de juste charger la fonction.
5. Sous `if __name__ == "__main__":`.
6. `auditer("192.168.1")`, `auditer("10.0.0")`, `auditer("172.16.0")`.
7. Imports → fonctions utilitaires → fonction principale → point d'entrée.
8. Non (la condition est fausse quand le fichier est importé).
9. Parce qu'on peut l'appeler autant de fois qu'on veut, avec des arguments différents, ici et ailleurs.
10. À séparer les outils réutilisables du code qui ne doit s'exécuter que lorsqu'on lance ce fichier directement.

</details>
