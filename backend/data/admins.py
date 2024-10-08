import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Admin(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'admins'

    uuid = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.uuid"), nullable=False, primary_key=True)
    requests = sqlalchemy.Column(sqlalchemy.String, default=None)