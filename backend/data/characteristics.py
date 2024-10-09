import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Characteristic(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'characteristics'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)