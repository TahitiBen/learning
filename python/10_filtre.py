compteur = 0
with open("hosts.txt", "r") as f:
    for ligne in f:
        if "192.168.1." in ligne:
            print(ligne.strip())
            compteur += 1
    print ("il y a", compteur, "machines")
