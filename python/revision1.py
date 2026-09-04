capacite = 500
utilise = 350

libre = capacite - utilise
pourcentage = utilise / capacite * 100

print ("Disque : " + str(capacite) + " Go | Utilise : " + str(utilise) + " Go | Libre : " + str(libre) + " Go | " + str(pourcentage) + "% utilisé")