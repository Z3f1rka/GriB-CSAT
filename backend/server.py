# flask imports

from flask import Flask, jsonify, request, redirect, make_response
from flask_cors import CORS
import jwt

# config imports
from server_conf import SECRET_KEY, ENCRYPT_ALG, JWT_SECRET_KEY

app = Flask(__name__)

CORS(app)


@app.route('/test', methods=["GET"])
def test():
    return {"message": "Hello, world"}


if __name__ == "__main__":
    app.run(port=8080, host="127.0.0.1")