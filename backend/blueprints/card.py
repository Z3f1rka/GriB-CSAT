from flask import Blueprint, jsonify, request, redirect, make_response
from blueprints.auth import get_jwt_payload

# db imports
from data import db_session
from data.sessions import Session
from data.users import User
from data.products import Product
from data.feedbacks import Feedback
from data.criterion import Criterion
from data.categoryproduct import CategoryProduct
from data.rating import Rating

# random
from random import sample

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
        el = {"id": product.id,
              "title": product.title}
        res.append(el)
    return res


@card.route("/products/vendor/<int:id>", methods=['GET'])
def vendor_products(id):
    sess = db_session.create_session()
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)
    if payload['role'] != "vendor":
        return make_response("User is not vendor", 403)
    if not sess.query(Product).filter(Product.vendor_id == id).all():
        return make_response("This vendor does not exist", 403)
    products = sess.query(Product).filter(Product.vendor_id == id).all()
    res = []
    for product in products:
        el = {"id": product.id,
              "title": product.title}
        res.append(el)
    return res


@card.route("/product/<int:id>", methods=["GET"])
def product(id):
    data = request.headers.get("bearer")
    jwt = get_jwt_payload(data)
    if type(jwt) != type(dict()):
        return make_response(jwt, 401)
    sess = db_session.create_session()
    product = sess.query(Product).filter(Product.id == id).first()
    if not product:
        return make_response('Товар не найден', 404)
    feedbacks = product.feedbacks
    rating = sum([i.rating for i in product.ratings]) / len(product.ratings)
    
    for_res = []
    for feedback in feedbacks:
        for_res.append({'name': feedback.user.name,
                        'text': feedback.text,
                        'rating': rating,
                        'data': feedback.public_date,
                        'user_id': feedback.user_id})
    for_res.sort(key=lambda x: len(x['text']), reverse=True)

    s = []
    for j in [i.category for i in product.categories]:
        for n in j.criterion:
            s.append(n)
    
    random_choice = sample(n, 3)
    user_characteristic = [i.title for i in random_choice]

    characteristic = product.characteristics
    
    minrating = min([i.rating for i in product.ratings])
    maxrating = max([i.rating for i in product.ratings])
    
    mintext = sess.query(Criterion).filter(minrating == Criterion.ratings).first().title
    maxtext = sess.query(Criterion).filter(maxrating == Criterion.ratings).first().title

    res = {"title": product.title,
           'rating': rating,
           'maxrating': {'text': maxtext, 'count': maxrating},
           'minrating': {'text': mintext, 'count': minrating},
           "vendor": product.vendor.name,
           "description": product.description,
           "feedback": for_res,
           'user_characteristic': user_characteristic,
           'characteristic': characteristic
           }
    
    return res