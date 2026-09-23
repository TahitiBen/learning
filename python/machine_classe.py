class Machine: 
    def __init__(self, nom, ip):
        self.nom = nom
        self.ip = ip

PC = Machine("PCAdmin", "192.168.17.1")
imp = Machine("Imprimante3", "192.168.17.5")

print(PC.nom)
print(PC.ip)
print(imp.nom)
print(imp.ip)