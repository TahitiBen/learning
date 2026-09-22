import requests

reponse = requests.get("https://api.github.com/users/TahitiBen")
donnees = reponse.json()

print("Dépôts publics : ", donnees["public_repos"])
print("Compte créé le : ", donnees["created_at"])