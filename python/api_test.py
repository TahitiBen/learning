import requests
reponse = requests.get("https://api.ipify.org?format=json")
print(reponse.json())