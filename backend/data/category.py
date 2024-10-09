import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'category'

    title = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    characteristics = sqlalchemy.Column(sqlalchemy.String)
    product = orm.relationship('Product', back_populates='characteristics')