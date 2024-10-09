import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Session(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'sessions'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, nullable=False, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer,
                                sqlalchemy.ForeignKey("users.id"), nullable=False)
    refresh_token = sqlalchemy.Column(sqlalchemy.String, nullable=False)