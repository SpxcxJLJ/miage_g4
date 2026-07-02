import requests

BASE_URL = "http://10.3.17.208:5000"

def get_enseignants():
    return requests.get(f"{BASE_URL}/enseignants").json()


