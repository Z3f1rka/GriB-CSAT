import pytest
import requests
import os
from auth import get_access_user
from test.auth import get_access_vendor

BASEURL = "http://127.0.0.1:8080/api/feedback/"

def test_feedback_add():
    res = requests.post(BASEURL + "add", json={"feedback": {"text": "очень классный","product_id": 1},
                                               "ratings": [{"rating": 4, "criterion": 1}]}, headers={"authorization": get_access_user()})
    assert res.status_code == 200