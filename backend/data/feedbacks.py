import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Feedback(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'feedbacks'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False, autoincrement=True)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.id"), nullable=False)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))
    product_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("products.id"), nullable=False)
    deprecated = sqlalchemy.Column(sqlalchemy.Boolean, default=True)
    
    user = orm.relationship('User')
    product = orm.relationship('Product', back_populates='feedbacks')
    ratings = orm.relationship('Rating', cascade='all, delete')