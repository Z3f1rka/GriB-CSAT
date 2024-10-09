from email.policy import default

import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    vendor_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"), nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, default=None)
    feedback = sqlalchemy.Column(sqlalchemy.String, default='') # id1;id2
    photos = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    statistics = sqlalchemy.Column(sqlalchemy.String, default=None) # path to file
    isaccepted = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))
    category = sqlalchemy.Column(sqlalchemy.ForeignKey("category.title"), default=None)
    rating = sqlalchemy.Column(sqlalchemy.Float, default=0)
    number_of_feedbacks = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    product_type = sqlalchemy.Column(sqlalchemy.Boolean, default=1) # 1 - товар, 0 - услуга
    vendor = orm.relationship('User')
    # characteristics = sqlalchemy.Column(sqlalchemy.String, nullable=False) # 'id1;id2;id3'
    characteristic_rating = sqlalchemy.Column(sqlalchemy.JSON) # [{'id': 1, 'rating': 5}, ...]
    characteristics = orm.relationship('Category')