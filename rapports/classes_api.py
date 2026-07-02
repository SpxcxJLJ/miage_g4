import requests

API_URL = "https://projet-mobile.onrender.com/api/classes"

def get_classes():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
