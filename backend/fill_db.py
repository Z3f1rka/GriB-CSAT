from data import db_session
from data.sessions import Session
from data.admins import Admin
from data.users import User
from data.vendors import Vendor
from data.products import Product
from uuid import uuid4
from data.feedbacks import Feedback

def fill_product():
    sess = db_session.create_session()
    product = Product(
        uuid=str(uuid4()),
        vendor_id='2da54a9d-e52b-47df-9d9a-c25483bfd138',
        title="Tea",
        photos="photka"
    )
    sess.add(product)
    sess.commit()
    print("OK")

if __name__ == "__main__":
    db_session.global_init("db/CSAT_db.db")
    fill_product()