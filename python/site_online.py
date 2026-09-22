import requests

url = input("Entrer une URL: ")

try:    
    chr = requests.get(url)

    if chr.status_code == 200:
        print("Le site est EN LIGNE (200)")

    else:
        print("Le site repond, code: ", chr.status_code)

except requests.exceptions.RequestException:
    print("Site INJOINGNABLE")