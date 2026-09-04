compteur = 0
with open ("serveurs.txt", "w") as f:
    f.write("Serveur T385b\n")
    f.write("Serveur XA\n")
    f.write("Serveur XS\n")

with open ("serveurs.txt","r") as f:
    for ligne in f:
        print(ligne.strip())
        compteur += 1
print ('Total : ' + str (compteur) + ' serveurs')