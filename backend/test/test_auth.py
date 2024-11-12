import pytest
import requests
import os
from auth import get_access_user
BASEURL = "http://127.0.0.1:8080/api/auth/"


def test_pass_test():
    assert True

def test_register_user():
    res = requests.post(BASEURL + "register", json={"name": "testuser",
                                                    "email": "testuser@mail.com",
                                                    "pswd": "test",
                                                    "pswd_repeated": "test"})
    assert res.status_code == 200

def test_register_admin():
    res = requests.post(BASEURL + "register", json={"name": "testadmin",
                                                    "email": "testadmin@mail.com",
                                                    "pswd": "test",
                                                    "pswd_repeated": "test",
                                                    "role": "admin"})
    assert res.status_code == 200

def test_register_vendor():
    res = requests.post(BASEURL + "register", json={"name": "testvendor",
                                                    "email": "testvendor@mail.com",
                                                    "pswd": "test",
                                                    "pswd_repeated": "test",
                                                    "role": "vendor"})
    assert res.status_code == 200

def test_required_name():
    res = requests.post(BASEURL + "register", json={"name": "testuser",
                                                    "email": "t@mail.com",
                                                    "pswd": "test",
                                                    "pswd_repeated": "test"})
    assert res.status_code == 400

def test_required_email():
    res = requests.post(BASEURL + "register", json={"name": "testuser123",
                                                    "email": "testuser@mail.com",
                                                    "pswd": "test",
                                                    "pswd_repeated": "test"})
    assert res.status_code == 400

def test_login():
    res = requests.post(BASEURL + "login", json={"name": "testuser",
                                                 "pswd": "test"})
    assert res.status_code == 200

def test_wrong_password():
    res = requests.post(BASEURL + "login", json={"name": "testuser",
                                                 "pswd": "123"})
    assert res.status_code == 400

def test_wrong_user():
    res = requests.post(BASEURL + "login", json={"name": "aaaaa",
                                                 "pswd": "test"})
    assert res.status_code == 404

def test_getuser():
    res = requests.get(BASEURL + "get_user", headers={"authorization": get_access_user()})

    assert res.status_code == 200

def test_invalid_token():
    res = requests.get(BASEURL + "get_user", headers={"authorization": get_access_user() + 'ee'})

    assert res.status_code == 401