with open("hosts.txt", "w") as f:
    f.write("Server-Web: 192.168.1.0\n")
    f.write("PC de Caroline: 192.168.10.0\n")
    f.write("Imprimante du bureau: 192.168.5.0\n")

with open("hosts.txt", "r") as f:
    contenu = f.read()
print(contenu)
