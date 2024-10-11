import pytest
import requests
import os
from auth import get_access_user
from test.auth import get_access_vendor

BASEURL = "http://127.0.0.1:8080/api/card/"

def test_add_card():
    res = requests.post(BASEURL + "add", json={"title": "Компьютер",
                                               "description": "черный",
                                               "characteristics": "Черный",
                                               "categories": ["Компьютеры и ноутбуки"]}, headers={"authorization": get_access_vendor()})
    assert res.status_code == 200


def test_add_card_invalid_token():
    res = requests.post(BASEURL + "add", json={"title": "Компьютер",
                                               "description": "черный",
                                               "characteristics": "Черный",
                                               "categories": 1}, headers={"authorization": get_access_user()})
    assert res.status_code == 403


def test_invalid_title():
    res = requests.post(BASEURL + "add", json={"title": "",
                                               "description": "черный",
                                               "characteristics": "Черный",
                                               "categories": 1}, headers={"authorization": get_access_vendor()})
    assert res.status_code == 400


def test_not_authorized():
    res = requests.post(BASEURL + "add", json={"title": "Компьютер",
                                               "description": "черный",
                                               "characteristics": "Черный",
                                               "categories": [1]})
    assert res.status_code == 401

def test_product():
    res = requests.get("http://127.0.0.1:8080/api/product/1")
    assert res.status_code == 200


def test_invalid_product():
    res = requests.get("http://127.0.0.1:8080/api/product/10", headers={"authorization": get_access_user()})
    assert res.status_code == 404