import requests

API_URL = "https://si-presences-gbh.onrender.com/api/cours/"

def get_cours(date=None, enseignant=None, classe=None):
    params = {}

    if date:
        params["date"] = date

    if enseignant:
        params["enseignant"] = enseignant

    if classe:
        params["classe"] = classe

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()
