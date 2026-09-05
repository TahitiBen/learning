import sqlite3

def lister():
    bran = sqlite3.connect("sql/machines.db")
    ray = bran.cursor()

    ray.execute("SELECT * FROM machines")
    for ligne in ray.fetchall():
        print(ligne)

    bran.close()

def ajouter():
    recon = sqlite3.connect("sql/machines.db")
    charles = recon.cursor()

    nom = input("Entrez le nom de la machine: ")
    ip = input("Maintenant son adresse IP: ")
    reseau = input("Et enfin le réseau auquel elle appartient: ")
    charles.execute("INSERT INTO machines (nom, ip, reseau) VALUES (?, ?, ?)", (nom, ip, reseau))
    recon.commit()
    print ("Machine ajoutee !")

    recon.close()

def rechercher():
    ty = sqlite3.connect("sql/machines.db")
    ban = ty.cursor()

    text = input("Nom de la machine : ")
    ban.execute("SELECT * FROM machines WHERE nom = ?", (text,))
    for ligne in ban.fetchall():
        print(ligne)

    ty.close()

def modifier():
    jun = sqlite3.connect("sql/machines.db")
    tao = jun.cursor()

    modif = input("Nommez la machine à modifier: ")
    ip = input("Indiquez la nouvelle adresse IP: ")
    tao.execute("UPDATE machines SET ip = ? WHERE nom = ?", (ip,modif))
    jun.commit()

    jun.close()

def supprimer ():
    ye = sqlite3.connect("sql/machines.db")
    yo = ye.cursor()

    kan = input("Quel machine voulez-vous supprimer")
    yo.execute("DELETE FROM machines WHERE nom = ?", (kan,))
    ye.commit()

    ye.close()

while True: 
    print("1. Lister les machines")
    print("2. Ajouter une machine")
    print("3. Rechercher une machin")
    print("4. Modifier une machine")
    print("5. Supprimer une machine")
    print("6. Quitter")
    choix = input("Ton choix : ")

    if choix == "1":
        lister()
    elif choix == "2":
        ajouter()
    elif choix == "3":
        rechercher()
    elif choix == "4":
        modifier()
    elif choix == "5":
        supprimer()
    elif choix == "6":
        break
    else:
        print("Choix invalide")













