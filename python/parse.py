with open("hosts.txt", "r") as f:
    for ligne in f:
        morceau = ligne.split(":")
        print("Nom:",morceau[0], "| IP:", morceau[1].strip())

    

