import requests

BASE_URL = "https://subpanel-versus-ebook.ngrok-free.dev"



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


def get_enseignant(id):
    r = requests.get(f"{BASE_URL}/enseignants/{id}")
    r.raise_for_status()
    return r.json()