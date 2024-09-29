import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Feedback(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'feedbacks'

    uuid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    user_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.uuid"), nullable=False)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    form = sqlalchemy.Column(sqlalchemy.String)
    photos = sqlalchemy.Column(sqlalchemy.String)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))