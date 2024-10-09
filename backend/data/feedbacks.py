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
    form = sqlalchemy.Column(sqlalchemy.String, default=None)
    photos = sqlalchemy.Column(sqlalchemy.String, default=None)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))
    rating = sqlalchemy.Column(sqlalchemy.Float, default=0)
    user = orm.relationship('User')