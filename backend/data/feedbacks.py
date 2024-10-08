import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Feedback(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'feedbacks'

    uuid = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=False)
    user_id = sqlalchemy.Column(sqlalchemy.String, sqlalchemy.ForeignKey("users.uuid"), nullable=False)
    text = sqlalchemy.Column(sqlalchemy.Text, nullable=False)
    form = sqlalchemy.Column(sqlalchemy.String, default=None)
    photos = sqlalchemy.Column(sqlalchemy.String, default=None)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))
    rating = sqlalchemy.Column(sqlalchemy.Float, default=0)
    # только для товаров
    rating_criteria = sqlalchemy.Column(sqlalchemy.Float, default=0)
    packaging_quality_criteria = sqlalchemy.Column(sqlalchemy.Float, default=0)
    delivery_criteria = sqlalchemy.Column(sqlalchemy.Float, default=0)
    interaction_criteria = sqlalchemy.Column(sqlalchemy.Float, default=0)
    # только для услуг
    impression_criteria = sqlalchemy.Column(sqlalchemy.Float, default=0)
    quality_criteria = sqlalchemy.Column(sqlalchemy.Float, default=0)
    impression_of_vendor_criteria =  sqlalchemy.Column(sqlalchemy.Float, default=0)
    speed_criteria = sqlalchemy.Column(sqlalchemy.Float, default=0)