import requests
from requests import Response

login_url = "https://api.escuelajs.co/api/v1/auth/login"
profile_url = "https://api.escuelajs.co/api/v1/auth/profile"


def login(username, password):
    return requests.post(login_url, data={"email": username, "password": password})


def get_token_validation(token):
    return requests.get(profile_url, headers={"Authorization": f"Bearer {token}"})


def validate_token(username: str, token_validation: Response):
    if token_validation.status_code != 200:
        return False
    return username == token_validation.json()["email"]
