from flask import Blueprint, jsonify, request, redirect, make_response
from blueprints.auth import get_jwt_payload

# db imports
from data import db_session
from data.sessions import Session
from data.users import User
from data.products import Product
from data.feedbacks import Feedback
from data.category import Category

crud = Blueprint("CRUD", "crud")

@crud.route("/upload_image", methods=["POST", "GET"])
def upload_image():
    """
    sess = db_session.create_session()
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)"""
    if request.method == "POST":
        file = request.files["file"]
        file.save(file.filename)
        return "saved"
    if request.method == "GET":
        return """<!doctype html>
<html>
  <head>
    <title>File Upload</title>
  </head>
  <body>
    <h1>File Upload</h1>
    <form method="POST" action="" enctype="multipart/form-data">
      <p><input type="file" name="file"></p>
      <p><input type="submit" value="Submit"></p>
    </form>
  </body>
</html>"""


@crud.route("/add_category", methods=["POST"])
def add_category():
    sess = db_session.create_session()
    data = request.json
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "admin":
        return make_response("You are not admin", 400)
    if sess.query(Category).filter(Category.title == data['title']).first():
        return make_response("This category is exists", 400)
    sess.add(Category(
        title=data['title'],
        characteristics=';'.join(list(map(lambda x: x.lower(), data["chars"])))
    ))
    sess.commit()
    return make_response("OK", 200)