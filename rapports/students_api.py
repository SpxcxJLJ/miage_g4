import requests

API_URL = "https://projet-mobile.onrender.com/api/students"

def get_students():
    response = requests.get(API_URL)
    response.raise_for_status()
    return response.json()
