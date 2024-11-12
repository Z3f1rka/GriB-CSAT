import requests
BASEURL = "http://127.0.0.1:8080/api/auth/"


def get_access_user():
    tokens = requests.post(BASEURL + "login", json={"name": "testuser",
                                                    "pswd": "test"})

    return tokens.json()["access_token"]

def get_access_admin():
    tokens = requests.post(BASEURL + "login", json={"name": "testadmin",
                                                    "pswd": "test"})

    return tokens.json()["access_token"]

def get_access_vendor():
    tokens = requests.post(BASEURL + "login", json={"name": "testvendor",
                                                    "pswd": "test"})

    return tokens.json()["access_token"]