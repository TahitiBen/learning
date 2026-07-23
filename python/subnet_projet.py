def hotes_utilisables(prefixe):
    return (2 ** (32 - prefixe)-2)

while True: 
    try:
        prefixe = int(input("Ecris un nombre entre 0 et 32: "))
        if prefixe == int(prefixe) and prefixe >= 0 and prefixe <= 32:
            print (prefixe,"->",hotes_utilisables(prefixe))
            break
        else:
            print ("Ce nombre n'est pas entre 0 et 32")

    except ValueError:
        print("Ce nombre n'est pas un nombre")
        continue
        prefixe = int(input("Ecris un nombre entre 0 et 32: "))
   
if prefixe <= 24:
    print ("Grand réseau")

elif prefixe <= 28:
    print ("Reseaux moyen")

else:
    print ("Petit réseaux")