from data import db_session
from data.users import User
from data.products import Product
from data.admins import Admin
from data.vendors import Vendor
from data.feedbacks import Feedback
from uuid import uuid4

db_session.global_init("db/CSAT_db.db")


def test1():
    sess = db_session.create_session()
    uuid = str(uuid4())
    user = User(
        uuid=uuid,
        role="admin",
        email="735@email",
        name="adm",
        hashed_password="pswd"
    )
    sess.add(user)

    adm = Admin(
    uuid=uuid
    )
    sess.add(adm)
    sess.commit()
    print("test1 OK")


def test2():
    sess = db_session.create_session()
    uuid = str(uuid4())
    user = User(
        uuid=uuid,
        role="vendor",
        email="735cvv@email",
        name="ven",
        hashed_password="pswd"
    )
    sess.add(user)
    vendor = Vendor(
        uuid=uuid
    )
    sess.add(vendor)
    sess.commit()
    print("test2 OK")


def test3():
    feedback = str(uuid4())
    sess = db_session.create_session()
    product = Product(
        uuid=str(uuid4()),
        vendor_id=sess.query(User).filter(User.name == "ven").first().uuid,
        title="kubiki kubiki kubiki",
        description="kuubicheskie",
        characteristics="krasnie zelenie zheltie",
        feedback=feedback,
        isaccepted=True,
        photos='/img'
    )
    sess.add(product)
    feedback = Feedback(
        uuid=feedback,
        user_id=sess.query(User).filter(User.name == "adm").first().uuid,
        text="zheltie krasnie zelenie"
    )
    sess.add(feedback)
    sess.commit()
    print("test3 OK")


if __name__ == "__main__":
    test1()
    test2()
    test3()