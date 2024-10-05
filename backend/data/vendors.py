import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Vendor(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'vendors'

    uuid = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.uuid"), nullable=False, primary_key=True)
    products = sqlalchemy.Column(sqlalchemy.String, default=None)