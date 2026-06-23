import requests

BASE_G2 = "http://10.3.17.208:5000/api"

def get_enseignants():
    url = f"{BASE_G2}/enseignants"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()

def get_enseignant(enseignant_id):
    url = f"{BASE_G2}/enseignants/{enseignant_id}"
    response = requests.get(url, timeout=5)
    response.raise_for_status()
    return response.json()
