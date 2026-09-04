import sqlite3

link = sqlite3.connect("sql/machines.db")
ross = link.cursor()

ross.execute("SELECT * FROM machines")
for ligne in ross.fetchall():
    print(ligne)

link.close()
