import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Photo(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'photos'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    path = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True)
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("products.id"), nullable=False)
    
    product = orm.relationship('Product', back_populates='photos')