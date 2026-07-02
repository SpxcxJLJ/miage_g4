import requests

BASE_URL = "http://10.3.17.208:5000"

def get_matieres():
    return requests.get(f"{BASE_URL}/matieres").json()

