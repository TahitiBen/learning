def niveau_alerte(pourcentage):
    if pourcentage >= 90:
        return ("CRITIQUE")

    elif pourcentage >= 70:
        return ("Attention")

    else:
        return ("OK")

while True:
    pour = input('indiquez un pourcentage: ')
    if pour == "stop":
        break
    else:
        pour = float(pour)
        print(niveau_alerte(pour))
