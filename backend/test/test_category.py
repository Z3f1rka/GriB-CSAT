import requests
from auth import get_access_admin, get_access_user, get_access_vendor
BASEURL = "http://127.0.0.1:8080/api/category"

def test_category_add():
    res = requests.post(BASEURL + "/add", json={"title": "Компьютеры и ноутбуки",
                                                "criterions": ["Соотношение цены и качества", "Внешний вид", "Энергоемкость"]}, headers={"authorization": get_access_admin()})
    assert res.status_code == 200

def test_category_invalid_role():
    res = requests.post(BASEURL + "/add", json={"title": "Компьютеры и ноутбуки",
                                                "criterions": ["Соотношение цены и качества", "Внешний вид", "Энергоемкость"]}, headers={"authorization": get_access_user()})
    assert res.status_code == 403

def test_category_invalid_token():
    res = requests.post(BASEURL + "/add", json={"title": "Компьютеры и ноутбуки",
                                                "criterions": ["Соотношение цены и качества", "Внешний вид", "Энергоемкость"]})
    assert res.status_code == 401

def test_category_add_validation():
    res = requests.post(BASEURL + "/add", json={"title": "Компьютеры и ноутбуки",
                                                "criterions": ["Целосность", "Удобство", "Энергоемкость"]}, headers={"authorization": get_access_admin()})
    assert res.status_code == 400

def test_category_no_criterions():
    res = requests.post(BASEURL + "/add", json={"title": "Компьютеры и ноутбуки"}, headers={"authorization": get_access_admin()})
    assert res.status_code == 400

def test_category_all():
    res = requests.get(BASEURL + "/all", headers={"authorization": get_access_vendor()})
    assert res.status_code == 200
    assert res.json() == list()

def test_category_all_invalid_token():
    res = requests.get(BASEURL + "/all", headers={"authorization": get_access_user()})
    assert res.status_code == 403