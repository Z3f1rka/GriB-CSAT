import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Criterion(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'criterions'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("categories.id"), nullable=False)
    
    category = orm.relationship('Category', back_populates='criterion')
    ratings = orm.relationship('Rating')