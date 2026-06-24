import requests

BASE_URL = "http://10.3.17.208:5000"


def get_enseignants():
    response = requests.get(f"{BASE_URL}/enseignants")
    response.raise_for_status()
    return response.json()


def get_enseignant(id):
    response = requests.get(
        f"{BASE_URL}/enseignants/{id}"
    )
    response.raise_for_status()
    return response.json()


def get_matieres():
    response = requests.get(
        f"{BASE_URL}/matieres"
    )
    response.raise_for_status()
    return response.json()


def get_matieres_enseignant(id):
    response = requests.get(
        f"{BASE_URL}/enseignants/{id}/matieres"
    )
    response.raise_for_status()
    return response.json()