nb = input("Indiquez un nombre: ")

try:
    int (nb)
    print ("nombre valide: ",nb)

except ValueError:
    print ("Ce n'est pas un nombre !")
