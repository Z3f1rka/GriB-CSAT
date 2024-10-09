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
def product(id):
    """data = request.headers.get("bearer")
    jwt = get_jwt_payload(data)
    if type(jwt) != type(dict()):
        return make_response(jwt, 401)"""
    sess = db_session.create_session()
    product = sess.query(Product).filter(Product.id == id).first()
    if not product:
        return make_response('Товар не найден', 404)
    feedback_id = product.feedback.split(';')
    feedbacks = []

    for id in feedback_id:
        res = sess.query(Feedback).filter(id == Feedback.id).first()
        feedbacks.append(res)

    for_res = []
    for feedback in feedbacks:
        print(feedback)
        for_res.append({'name': feedback.user.name,
                        'text': feedback.text,
                        'rating': str(feedback.rating),
                        'data': feedback.public_date,
                        'user_id': feedback.user_id})
    for_res.sort(key=lambda x: len(x['text']), reverse=True)
    photos = product.photos.split(";")

    listimg = []
    for i in range(len(photos)):
        listimg.append({'id': i + 1, 'img': photos[i]})

    # user_characteristics = sess.query(Characteristic).all()
    # random_choice = sample(user_characteristics, 3)
    # user_characteristic = [i.title for i in random_choice]
    user_characteristic = []

    characteristics = sess.query(Product.characteristic_rating).all()
    characteristics.sort(key=lambda x: x['rating'])
    print(characteristics)

    res = {"ListImg": listimg,
           "title": product.title,
           'rating': product.rating,
           'maxrating': {'text': '', 'count': 5},
           'minrating': {'text': '', 'count': 1},
           'minrating': {},
           'characteristics': product.characteristics,
           "vendor": product.vendor.name,
           "description": product.description,
           "product_type": product.product_type,
           "feedback": for_res,
           'user_characteristic': user_characteristic
           }
    return res