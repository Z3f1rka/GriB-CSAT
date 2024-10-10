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
    description = sqlalchemy.Column(sqlalchemy.Text, default='Описание отсутсвует')
    characteristics = sqlalchemy.Column(sqlalchemy.String, default=None) #'id1;id2;id3'
    accepted = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))

    vendor = orm.relationship('User')
    categories = orm.relationship('CategoryProduct', back_populates='product')
    feedbacks = orm.relationship('Feedback')