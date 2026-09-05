import sqlite3
conn = sqlite3.connect("sql/machines.db")
curseur = conn.cursor()

nom = input("Nom de la machine : ")
curseur.execute("SELECT * FROM machines WHERE nom = ?", (nom,))
for ligne in curseur.fetchall():
    print(ligne)

conn.close()