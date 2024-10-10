
from datetime import datetime, timedelta, timezone
from flask import Blueprint, jsonify, request, redirect, make_response
import jwt
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename


# config imports
from server_conf import ENCRYPT_ALG, JWT_SECRET_KEY


# db imports
from data import db_session
from data.sessions import Session
from data.users import User

auth = Blueprint("authentification", "auth")

access_token_life_time = timedelta(hours=1)
refresh_token_life_time = timedelta(days=30)

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


def change_role(id: str, role: str) -> None:
    sess = db_session.create_session()
    user = sess.query(User).filter(User.id == id).first()
    user.role = role
    sess.commit()


@auth.route('/register', methods=['POST'])
def register():
    sess = db_session.create_session()
    data = request.json
    if not data["pswd"] or not (0 < len(data["name"]) <= 30) or not data["email"]:
        return make_response("Password required", 400)
    if sess.query(User).filter(User.name == data["name"]).first():
        return make_response("Пользователь с таким именем существует", 400)
    if sess.query(User).filter(User.email == data["email"]).first():
        return make_response("Пользователь с таким именем существует", 400)

    data['role'] = data.get('role') if data.get('role') else 'user'
    if data['pswd'] == data['pswd_repeated']:
        data['hashed_password'] = generate_password_hash(data['pswd'])
        data.pop('pswd')
        data.pop('pswd_repeated')
    sess.add(
        User(**data)
    )
    sess.commit()

    uid = sess.query(User).filter(User.name == data['name']).first().id
    access_token = create_jwt({
        'type': "jwt_access",
        'exp': datetime.now(timezone.utc) + access_token_life_time,
        'sub': uid,
        'role': data['role']
    })
    refresh_token = make_session(uid, data['role'])
    return {'refresh_token': refresh_token, 'access_token': access_token}


@auth.route('/login', methods=['POST'])
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
            'sub': user.id,
            'role': user.role
        })
        refresh_token = make_session(user.id, user.role)
        return {'refresh_token': refresh_token, 'access_token': access_token}


@auth.route('/refresh', methods=['POST'])
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
    return {'refresh_token': data, 'access_token': access_token}