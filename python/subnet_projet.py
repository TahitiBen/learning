def hotes_utilisables(prefixe):
    return (2 ** (32 - prefixe)-2)

prefixe = int(input("Ecris un nombre entre 0 et 32: "))
while prefixe < 0 or prefixe > 32:
    print("Ce nombre n'est pas entre 0 et 32")
    prefixe = int(input("Ecris un nombre entre 0 et 32: "))

print (prefixe,"->",hotes_utilisables(prefixe))
   

if prefixe <= 24:
    print ("Grand réseau")

elif prefixe <= 28:
    print ("Reseaux moyen")

else:
    print ("Petit réseaux")