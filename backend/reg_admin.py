import requests

resp = requests.post("http://127.0.0.1:8080/api/auth/register", json={"name": "main admin",
                                                                      "email": "mainadmin@mail.sru",
                                                                      "pswd": "123",
                                                                      "pswd_repeated": "123",
                                                                      "role": "admin"})