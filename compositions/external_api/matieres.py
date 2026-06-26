import requests

BASE_URL = "http://10.3.17.208:5000"

def get_matieres():
    return requests.get(f"{BASE_URL}/matieres").json()

def get_matieres_by_enseignant(id):
    return requests.get(f"{BASE_URL}/enseignants/{id}/matieres").json()
