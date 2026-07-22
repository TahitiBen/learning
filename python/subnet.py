prefixe = input("écriver un chiffre :")
sufixe = int(prefixe)

if sufixe >= 0 and sufixe <= 32:
    print (2 ** (32 - sufixe)-2)

else:
    print ("Prefixe invalide (0 a 32)")
 