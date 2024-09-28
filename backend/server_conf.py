from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = str(os.environ.get("SECRET_KEY"))
ENCRYPT_ALG = str(os.environ.get("ENCRYPT_ALG"))
JWT_SECRET_KEY = str(os.environ.get("JWT_SECRET_KEY"))