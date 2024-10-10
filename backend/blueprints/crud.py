from flask import Blueprint, jsonify, request, redirect, make_response
from blueprints.auth import get_jwt_payload, make_session
from werkzeug.utils import secure_filename
import os

# db imports
from data import db_session
from data.feedbacks import Feedback
from data.rating import Rating
from data.users import User
from data.category import Category
from data.products import Product
from data.sessions import Session
from data.criterion import Criterion
from data.categoryproduct import CategoryProduct

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

# category crud

@crud.route("/category/add", methods=["POST"])
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
    cat = Category(title=data['title'])
    sess.add(cat)
    sess.commit()

    cat = sess.query(Category).filter(Category.title == data['title']).first()
    print(cat.id)
    criterions = data['criterions']
    # criterions = [title, ...]
    for criterion in criterions:
        if not criterion:
            return make_response("Title is required", 400)
        sess.add(Criterion(title=criterion, category_id=cat.id))
    sess.commit()
    return make_response("OK", 200)


@crud.route("/category/delete/<int:id>", methods=["POST"])
def delete_category(id):
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "admin":
        return make_response("The requester is not admin", 403)
    sess = db_session.create_session()
    if not sess.query(Category).filter(Category.id == id).first():
        return make_response("This category does not exist", 403)
    cat = sess.query(Category).filter(Category.id == id).first()
    sess.delete(cat)
    sess.commit()
    return make_response("OK", 200)


@crud.route("/category/edit/<int:id>", methods=["GET", "POST"])
def edit_category(id):
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "admin":
        return make_response("The requester is not admin", 403)
    sess = db_session.create_session()
    if not sess.query(Category).filter(Category.id == id).first():
        return make_response("This category does not exist", 403)
    cat = sess.query(Category).filter(Category.id == id).first()

    if request.method == 'GET':
        # {'title': , 'criterions': [{}]}
        res = {'title': cat.title, 'criterions': []}
        criterions = []
        for i in cat.criterion:
            criterions.append({'id': i.id, 'title': i.title})
        return res

    elif request.method == 'POST':
        data = request.json
        cat.title = data['title']
        # добавить, убрать критерии
        sess.commit()


@crud.route("/category/all", methods=['GET'])
def all():
    """{id:, title:, criterion: [{id, title}, ...]}"""
    sess = db_session.create_session()
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "vendor":
        return make_response("User is not vendor", 403)
    categories = sess.query(Category).all()
    responses = []
    for i in categories:
        element = {"id": i.id,
                    "title": i.title,
                    "criterion": None}
        criterions = []
        for j in i.criterion:
            criterions.append({"id": j.id,
                              "title": j.title})
        element["criterion"] = criterions
        responses.append(element)
    return responses


# TODO: дописать изменение

# CRUD card

@crud.route("/card/delete/<int:id>", methods=["DELETE"])
def delete_card(id: int):
    sess = db_session.create_session()
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "admin":
        return make_response("The requester is not admin", 403)
    elif payload['role'] == "vendor":
        if not sess.query(Product).filter(Product.id == id).first().vendor_id == payload['sub']:
            return make_response("The requester do not have this product", 403)
    card = sess.query(Product).filter(Product.id == id).first()
    sess.delete(card)
    sess.commit()
    return make_response("OK", 200)


@crud.route("/card/add", methods=["POST"])
def add_card():
    sess = db_session.create_session()
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "vendor":
        return make_response("The requester is not vendor", 403)
    
    vendor_id = payload['sub']
    data = request.json
    title = data['title']
    if title == '':
        return make_response("Title is required", 400)
    description = data['description']
    characteristics = data['characteristics']
    categories = data['categories'] # []
    sess.add(Product(vendor_id=vendor_id, title=title, description=description, characteristics=characteristics))
    sess.commit()
    product_id = len(sess.query(Product).all())
    for category in categories:
        cat = sess.query(Category).filter(Category.title == category).first()
        category_id = cat.id
        sess.add(CategoryProduct(product_id=product_id, category_id=category_id))
    sess.commit()
    return make_response("OK", 200)


@crud.route('/card/edit/<int:id>', methods=['GET', 'POST'])
def edit_card(id):
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "vendor":
        return make_response("The requester is not vendor", 403)
    vendor_id = payload['sub']

    sess = db_session.create_session()
    product = sess.query(Product).filter(Product.id == id).first()
    if product.vendor_id != vendor_id:
        make_response("The requester is not vendor of the product", 403)
        
    if request.method == 'GET':
        return jsonify({'id': product.id, 'title': product.title, 'description': product.description, 'characteristics': product.characteristics, 'categories': product.categories})
    
    elif request.method == 'POST':
        data = request.json
        if data['title'] == '':
            return make_response("Title is required", 400)
        product.title = data['title']       
        product.description = data['description']
        product.characteristics = data['characteristics']
        product.categories = data['categories'] # []


# user crud
@crud.route("/user/delete/<int:id>", methods=["DELETE"])
def delete(id: int):
    sess = db_session.create_session()
    payload = get_jwt_payload(request.headers.get("authorization"))
    allowed_role = "superuser"
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != allowed_role:
        return make_response(f"The requester is not {allowed_role}", 403)
    user = sess.query(User).filter(User.id == id).first()
    if user.role == "user":
        user.role = "deleted"
        session = sess.query(Session).filter(Session.user_id == user.id).first()
        sess.delete(session)
    elif user.role == "vendor":
        sess.delete(user)
        session = sess.query(Session).filter(Session.user_id == user.id).first()
        sess.delete(session)
    sess.commit()
    return make_response("OK", 200)


@crud.route("/user/update/<int:id>", methods=["PUT"])
def update(id: int):
    sess = db_session.create_session()
    payload = get_jwt_payload(request.headers.get("authorization"))
    data = request.json
    user = sess.query(User).filter(User.id == id).first()
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if not user.id == payload['sub']:
        return make_response("Users doesnt match", 403)

    if "email" in data.keys():
        if sess.query(User).filter(User.email == data["email"]).first():
            return make_response("This email is not unique", 400)
        user.email = data['email']
    if "name" in data.keys():
        if sess.query(User).filter(User.name == data["name"]).first():
            return make_response("This name is not unique", 400)
        user.name = data["name"]
    if "phone_number" in data.keys():
        if sess.query(User).filter(User.phone_number == data["phone_number"]).first():
            return make_response("This phone number is not unique", 400)
        user.phone_number = data["phone_number"]
    sess.commit()
    return make_response("OK", 200)


# feedbacks
# TODO: сделать изменение удаление отзывов
@crud.route("/feedback/add", methods=["POST"])
def add():
    """
    {feedback: {
        text:,
        product_id:
    },
    ratings: [{rating: , criterion:}]}
    """
    sess = db_session.create_session()
    data = request.json
    payload = get_jwt_payload(request.headers.get("authorization"))
    if type(payload) != type(dict()):
        return make_response("Unathorized", 401)
    if payload['role'] != "user":
        return make_response(f"The requester is not user", 403)

    # TODO: сделать валидацию входящих  данных

    feedback = Feedback(text=data['feedback']['text'],
                        product_id=data['feedback']['product_id'],
                        user_id=payload['sub'])
    sess.add(feedback)
    sess.commit()

    feedback_id = sess.query(Feedback).all()[-1]
    for i in data['ratings']:
        rating = Rating(rating=i['rating'],
                        feedback_id=feedback_id,
                        criterion_id=i["criterion"])
        sess.add(rating)
        sess.commit()
    return make_response("OK", 200)