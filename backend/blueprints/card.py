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
    """[{id:, title:, img}]"""
    sess = db_session.create_session()
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)
    products = sess.query(Product).all()
    res = []
    for product in products:
        el = {"id": product.id,
              "title": product.title,
              "img": product.photos[0].path}
        res.append(el)
    return res


@card.route("/product/<int:id>", methods=["GET"])
def product(id):
    sess = db_session.create_session()
    product = sess.query(Product).filter(Product.id == id).first()
    if not product:
        return make_response('Товар не найден', 404)
    if sess.query(Feedback).filter(Feedback.product_id == product.id).first():
        total_med = 0 # конечный результат
        feedbacks = product.feedbacks # список фидбеков
        total_sum = 0
        maxrating = -1
        minrating = 6
        for i in feedbacks: # перебор списка фидбеков
            a = i.ratings # список рейтингов
            rating_sum = 0 # среднее арифметическое рейтингов
            for j in a: # перебор рейтингов
                rating_sum += j.rating
                if j > maxrating:
                    maxrating = j.rating
                    maxtext = j.title
                if j < minrating:
                    minrating = j.rating
                    mintext = j.title
            rating_med = rating_sum / len(a)
            total_sum += rating_med
        total_med = total_sum / len(feedbacks)

        rating = total_med

        for_res = []
        for feedback in feedbacks:
            a = feedback.ratings  # список рейтингов
            rating_sum = 0  # среднее арифметическое рейтингов
            for j in a:  # перебор рейтингов
                rating_sum += j.rating
            rating_med = rating_sum / len(a)
            for_res.append({'name': feedback.user.name,
                            'text': feedback.text,
                            'rating': rating_med,
                            'data': feedback.public_date,
                            'user_id': feedback.user_id})
        for_res.sort(key=lambda x: len(x['text']), reverse=True)

        s = []
        for j in [i.category for i in product.categories]:
            for n in j.criterion:
                s.append(n)
            print("SSSSSSSSSSSSSSSSS", s)

        random_choice = sample(s, 3)
        user_characteristic = [i.title for i in random_choice]

        characteristic = product.characteristics

        res = {"title": product.title,
               'rating': rating,
               'maxrating': {'text': maxtext, 'count': maxrating},
               'minrating': {'text': mintext, 'count': minrating},
               "vendor": product.vendor.name,
               "description": product.description,
               "feedback": for_res,
               'user_characteristic': user_characteristic,
               'characteristic': characteristic,
               "ListImg": [i.path for i in product.photos]
               }
    else:
        s = []
        for j in [i.category for i in list(product.categories)]:
            for n in j.criterion:
                print(n)
                s.append(n.title)
            print(j)
        print("SSSSSSSSSSSSSSSSS", s)
        try:
            random_choice = sample(s, 3)
        except Exception:
            random_choice = s
        user_characteristic = [i for i in random_choice]

        characteristic = product.characteristics
        res = {"title": product.title,
               'rating': 0,
               'maxrating': {'text': '', 'count': 0},
               'minrating': {'text': '', 'count': 0},
               "vendor": product.vendor.name,
               "description": product.description,
               "feedback": [],
               'user_characteristic': user_characteristic,
               'characteristic': characteristic,
               "ListImg": [i.path for i in product.photos]
               }
    return res