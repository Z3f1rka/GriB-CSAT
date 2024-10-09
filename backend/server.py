# flask imports
from datetime import datetime, timedelta, timezone
from flask import Flask, jsonify, request, redirect, make_response
from flask_cors import CORS
import jwt
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename


# config imports
from server_conf import SECRET_KEY, ENCRYPT_ALG, JWT_SECRET_KEY


# db imports
from data import db_session
from data.sessions import Session
from data.admins import Admin
from data.users import User
from data.products import Product
from data.feedbacks import Feedback
from data.characteristics import Characteristic

app = Flask(__name__)
access_token_life_time = timedelta(hours=1)
refresh_token_life_time = timedelta(days=30)
CORS(app)

# Authentification
def create_jwt(payload: dict) -> str:
    """
    This function generates a jwt

    REQUIRED FIELDS:
    iss — (issuer) издатель токена,
    sub — (subject) "тема", назначение токена,описываемый объект,
    aud — (audience) аудитория, получатели токена,
    exp — (expire time) срок действия токена,
    nbf — (not before) срок, до которого токен не действителен,
    iat — (issued at) время создания токена,
    jti — (JWT id) идентификатор токена
    """
    for param in payload.copy().keys():
        if not payload[param]:
            payload.pop(param)
    return jwt.encode(payload, JWT_SECRET_KEY, algorithm=ENCRYPT_ALG)


def get_jwt_payload(token: str) -> dict | str:
    """
    This function decodes token
    if token invalid :return: name of error
    else :return: payload(json)
    :param token: str
    """
    try:
        decoded = jwt.decode(token, JWT_SECRET_KEY, algorithms=ENCRYPT_ALG)
        return decoded
    except jwt.InvalidTokenError as invalid_token:
        return type(invalid_token).__name__


def make_session(user_id, role) -> str:
    db_sess = db_session.create_session()
    users_sessions = db_sess.query(Session).filter(Session.user_id == user_id).all()
    refresh_token = None

    if any(True for i in users_sessions if i.user_id == user_id):
        refresh_token = db_sess.query(Session).filter(Session.user_id == user_id).first().refresh_token
        jti = get_jwt_payload(refresh_token)['jti']
        db_sess.delete(db_sess.query(Session).filter(Session.user_id == user_id).first())
    if not refresh_token:
        jti = str(uuid4())
        refresh_token = create_jwt({
            'type': "jwt_refresh",
            'exp': datetime.now(timezone.utc) + refresh_token_life_time,
            'jti': jti,
            'role': role
        })
    refresh_session = Session(
        uuid=jti,
        user_id=user_id,
        refresh_token=refresh_token
    )
    db_sess.add(refresh_session)
    db_sess.commit()
    return refresh_token


def change_role(uuid: str, role: str) -> None:
    sess = db_session.create_session()
    user = sess.query(User).filter(User.uuid == uuid).first()
    user.role = role
    adm = sess.query(Admin).filter(Admin.uuid == uuid).first()
    if adm:
        sess.delete(adm)

    if role == "admin":
        sess.add(
            Admin(uuid=uuid)
        )
    sess.commit()


@app.route('/api/auth/register', methods=['POST'])
def register():
    sess = db_session.create_session()
    uuid = str(uuid4())
    data = request.json
    if sess.query(User).filter(User.name == data["name"]).first():
        return make_response("Пользователь с таким именем существует")
    if sess.query(User).filter(User.email == data["email"]).first():
        return make_response("Пользователь с таким именем существует")

    data['role'] = data.get('role') if data.get('role') else 'user'
    if data['pswd'] == data['pswd_repeated']:
        data['hashed_password'] = generate_password_hash(data['pswd'])
        data.pop('pswd')
        data.pop('pswd_repeated')
    sess.add(
        User(uuid=uuid, **data)
    )

    if data['role'] == "admin":
        sess.add(
            Admin(uuid=uuid)
        )
    sess.commit()

    access_token = create_jwt({
        'type': "jwt_access",
        'exp': datetime.now(timezone.utc) + access_token_life_time,
        'sub': uuid,
        'role': data['role']
    })
    refresh_token = make_session(uuid, data['role'])
    return {'refresh_token': refresh_token, 'access_token': access_token}


@app.route('/api/auth/login', methods=['POST'])
def login():
    sess = db_session.create_session()
    data = request.json
    user = sess.query(User).filter(User.name == data['name']).first()
    if not user:
        return make_response("User not found", 404)
    elif not check_password_hash(user.hashed_password, data['pswd']):
        return make_response("Wrong password", 400)
    else:
        access_token = create_jwt({
            'type': "jwt_access",
            'exp': datetime.now(timezone.utc) + access_token_life_time,
            'sub': user.uuid,
            'role': user.role
        })
        refresh_token = make_session(user.uuid, user.role)
        return {'refresh_token': refresh_token, 'access_token': access_token}


@app.route('/api/auth/refresh', methods=['POST'])
def refresh():
    sess = db_session.create_session()
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)
    session = sess.query(Session).filter(Session.uuid == payload['jti']).first()
    access_token = create_jwt({
        'type': "jwt_access",
        'exp': datetime.now(timezone.utc) + access_token_life_time,
        'sub': session.user_id,
        'role': payload['role']
    })
    return {'refresh_token': data['refresh_token'], 'access_token': access_token}


@app.route("/api/products", methods=['GET'])
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


@app.route("/api/product/<int:id>", methods=["GET"])
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


@app.route("/api/upload_image", methods=["POST", "GET"])
def upload_image():
    sess = db_session.create_session()
    data = request.headers.get("authorization")
    payload = get_jwt_payload(data)
    if type(payload) != type(dict()):
        return make_response(payload, 401)
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



if __name__ == "__main__":
    db_session.global_init('db/CSAT_db.db')
    db_sess = db_session.create_session()
    res = db_sess.query(Product).filter(Product.id == 1).first().characteristics
    res2 = db_sess.query(Characteristic).filter(Characteristic.id == int(res)).first().title
    print(res2)
    app.run(port=8080, host="127.0.0.1")