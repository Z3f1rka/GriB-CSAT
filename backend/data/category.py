import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Category(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'categories'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False, primary_key=True)
    
    products = orm.relationship('CategoryProduct', back_populates='category')
    criterion = orm.relationship('Criterion', back_populates='category')