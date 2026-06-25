import requests

BASE_URL = "http://10.3.0.145:5000"

def get_matieres():
    response = requests.get(f"{BASE_URL}/matieres")
    return response.json()
