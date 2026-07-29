with open("hosts.txt", "r") as entree, open("rapport.txt", "w") as sortie:
    for ligne in entree:
        morceau = ligne.split(":")
        sortie.write("Machine : " + morceau[0] + " - IP : " + morceau[1].strip() + "\n")
    