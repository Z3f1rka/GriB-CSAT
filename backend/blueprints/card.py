from flask import Blueprint, jsonify, request, redirect, make_response
from blueprints.auth import get_jwt_payload

# db imports
from data import db_session
from data.sessions import Session
from data.admins import Admin
from data.users import User
from data.products import Product
from data.feedbacks import Feedback

card = Blueprint("cards", "card")

@card.route("/products", methods=['GET'])
def products():
    sess = db_session.create_session()
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)
    products = sess.query(Product).all()
    res = []
    for product in products:
        photos = []
        for photo in product.photos.split(";"):
            photos.append(photo)
        el = {"id": product.id,
              "title": product.title,
              "img": photos}
        res.append(el)
    slice = tuple(map(int, data['photos'].split("-")))
    res = res[slice[0]:slice[1]]
    return res


@card.route("/product/<int:id>", methods=["GET"])
def product(id: int):
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)
    sess = db_session.create_session()
    product = sess.query(Product).filter(Product.uuid == id).first()
    feedbacks = sess.query(Feedback).filter(Feedback.uuid in product.feedback).all()
    for_res = []
    for feedback in feedbacks:
        for_res.append({'name': feedback.user.name,
                        'text': feedback.text,
                        'img': feedback.photos,
                        'rating': str(feedback.rating),
                        'date': feedback.public_date,
                        'user_id': feedback.user_id})
    res = {"ListImg": [],
           "title": product.title,
           "vendor": product.vendor.name,
           "characteristic": None,
           "description": product.description,
           "product_type": product.product_type,
           "feedback": for_res}
    return res