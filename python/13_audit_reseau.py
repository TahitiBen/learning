import datetime

def est_sur_reseau (ligne, reseau):
    return reseau + "." in ligne

def formater_machine(morceau):
    return "Machine : " + morceau[0] + " - IP : " + morceau [1].strip()+ "\n"

maintenant = datetime.datetime.now()

reseau = input("Donner le nom d'un réseau à auditer (ex. 192.168.1): ")

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
    
    sortie.write ("Total : " + str(compteur) + " machine(s)" + "\n")