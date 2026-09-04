import sqlite3

link = sqlite3.connect("sql/machines.db")
ross = link.cursor()

ross.execute("INSERT INTO machines (nom,ip,reseau) VALUES ('Python-Test','192.168.1.99','192.168.1')")
link.commit()

ross.execute("SELECT * FROM machines")
for ligne in ross.fetchall():
    print(ligne[1], "->", ligne[2])

link.close()
