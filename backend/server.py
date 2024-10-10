# TODO: Добавить валидацию запросов на все обработчики

# flask imports
from datetime import timedelta
from flask import Flask
from flask_cors import CORS

# Blueprints
from blueprints.auth import auth
from blueprints.card import card
from blueprints.crud import crud

# db imports
from data import db_session


app = Flask(__name__)
access_token_life_time = timedelta(minutes=10)
refresh_token_life_time = timedelta(days=30)
CORS(app)

app.register_blueprint(auth, url_prefix="/api/auth")
app.register_blueprint(card, url_prefix="/api")
app.register_blueprint(crud, url_prefix="/api")


if __name__ == "__main__":
    db_session.global_init('db/CSAT_db.db')
    app.run(port=8080, host="127.0.0.1")