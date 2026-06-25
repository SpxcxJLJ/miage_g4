import requests

BASE_URL = "http://10.3.17.208:5000"

def get_enseignants():
    response = requests.get(f"{BASE_URL}/enseignants")
    return response.json()
