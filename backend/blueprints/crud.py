from flask import Blueprint, jsonify, request, redirect, make_response
from blueprints.auth import get_jwt_payload, make_session
from werkzeug.utils import secure_filename
import os

# db imports
from data import db_session
from data.category import Category
from data.products import Product

ALLOWED_MEDIA = []
DESTINATION = ""


crud = Blueprint("CRUD", "crud")

@crud.route("/upload_images", methods=["POST", "GET"])
def upload_images():
    sess = db_session.create_session()
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)
    if payload["role"] != "vendor":
        return make_response("The requester is not vendor", 403)
    if request.method == "POST":
        if request.files:
            for i, file in enumerate(request.files):
                try:
                    image = request.files[f"images[{i}]"]
                    if image.content_type not in ALLOWED_MEDIA:
                        return make_response("Unsupported Media Type", 415)
                    image.save(os.path.join(DESTINATION), secure_filename(image.filename))
                except (KeyError, FileNotFoundError):
                    return jsonify("An error occurred while processing the file."), 500
            return "saved"
        return make_response("No files", 400)
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
        return make_response("The requester is not admin", 403)
    if sess.query(Category).filter(Category.title == data['title']).first():
        return make_response("This category exists", 400)
    sess.add(Category(
        title=data['title'],
        criterions=';'.join(list(map(lambda x: x.lower(), data["chars"])))
    ))
    sess.commit()
    return make_response("OK", 200)


@crud.route("/delete_card/<int:id>", methods=["DELETE"])
def delete_card(id: int):
    sess = db_session.create_session()
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "admin":
        return make_response("The requester is not admin", 403)
    elif payload['role'] == "vendor":
        if not sess.query(Product).filter(Product.id == id).first().vendor_id == payload['sub']:
            return make_response("The requester is not have this product", 403)
    card = sess.query(Product).filter(Product.id == id).first()
    sess.delete(card)
    sess.commit()
    return make_response("OK", 200)