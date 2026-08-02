compteur = 0 
with open("hosts.txt", "r") as f:
    for ligne in f:
        print(ligne.strip())
        compteur += 1

print ("Total:",compteur, "machines")