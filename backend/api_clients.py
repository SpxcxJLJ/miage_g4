import requests

BASE_URL = "http://10.3.17.208:5000"


def get_enseignants():

    r = requests.get(f"{BASE_URL}/enseignants")

    r.raise_for_status()

    return r.json()

def get_matieres():

    r = requests.get(f"{BASE_URL}/matieres")

    r.raise_for_status()

    return r.json()

def get_enseignements():
    r = requests.get(f"{BASE_URL}/enseigne")
    r.raise_for_status()
    return r.json()

