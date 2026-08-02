import datetime

maintenant = datetime.datetime.now()

reseau = input("Donner le nom d'un réseau à auditer (ex. 192.168.1): ")

compteur = 0
with open("hosts.txt", "r") as entree, open("audit.txt", "w") as sortie:
    sortie.write("Audit du reseau " + reseau + " - genere le " + maintenant.strftime("%d/%m/%Y %Hh%M") + "\n")

    for ligne in entree:
        morceau = ligne.split(":")
        if reseau + "." in ligne:
            sortie.write("Machine : " + morceau[0] + " - IP : " + morceau [1].strip()+ "\n")
            compteur += 1

    if compteur == 0: 
        print("Aucune machine sur ce reseau")
    
    sortie.write ("Total : " + str(compteur) + " machine(s)" + "\n")