import datetime

là = datetime.datetime.now()

with open("hosts.txt", "r") as entree, open("rapport.txt", "w") as sortie:
    sortie.write("Rapport genere le " + là.strftime("%d/%m/%Y %Hh%M") + "\n")
    for ligne in entree:
        morceau = ligne.split(":")
        sortie.write("Machine : " + morceau[0] + " - IP : " + morceau[1].strip() + "\n")

