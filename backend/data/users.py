import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class User(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    role = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, nullable=False)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    avatar = sqlalchemy.Column(sqlalchemy.String, nullable=True)  # way to file
    registration_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    phone_number = sqlalchemy.Column(sqlalchemy.String, nullable=True)