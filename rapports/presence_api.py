import requests

BASE_URL = "https://si-presences-gbh.onrender.com/api"

def get_cours(date=None, classe=None, enseignant=None):
    params = {}

    if date:
        params["date"] = date
    if classe:
        params["classe_id"] = classe
    if enseignant:
        params["enseignant_id"] = enseignant

    response = requests.get(f"{BASE_URL}/cours/", params=params)
    return response.json()
