import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class CategoryProduct(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'categoryproducts'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    category_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("category.id"), nullable=False)
    product_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("products.id"), nullable=False)
    
    category = orm.relationship('Category', back_populates='products')
    product = orm.relationship('Product', back_populates='categories')