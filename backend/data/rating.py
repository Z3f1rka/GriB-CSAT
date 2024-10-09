import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Rating(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'rating'
    
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, nullable=False)
    rating = sqlalchemy.Column(sqlalchemy.Integer, nullable=False, primary_key=True)
    feedback_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("feedbacks.id"), nullable=False)
    criterion_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("criterions.id"), nullable=False)
    
    feedback = orm.relationship('Feedback', back_populates='ratings')
    criterion = orm.relationship('Criterion')