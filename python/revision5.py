val = input('Entrez un nombre: ')

try:
    int(val)
    print ('Nombre valide : ' + str (val))

except ValueError:
    print ("Ce n'est pas un nombre !")
    