import requests

API_URL = "https://si-presences-gbh.onrender.com/api/presences/"

def get_presences(cours=None, etudiant=None, statut=None):
    params = {}

    if cours:
        params["cours"] = cours

    if etudiant:
        params["etudiant_id"] = etudiant

    if statut:
        params["statut"] = statut

    response = requests.get(API_URL, params=params)
    response.raise_for_status()
    return response.json()
