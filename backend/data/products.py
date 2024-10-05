import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'products'

    uuid = sqlalchemy.Column(sqlalchemy.String, primary_key=True, nullable=False)
    vendor_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("vendors.uuid"), nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text, default=None)
    characteristics = sqlalchemy.Column(sqlalchemy.String, default=None)
    feedback = sqlalchemy.Column(sqlalchemy.String, default=None)
    photos = sqlalchemy.Column(sqlalchemy.String, default=None)
    statistics = sqlalchemy.Column(sqlalchemy.String, default=None) # path to file
    isaccepted = sqlalchemy.Column(sqlalchemy.Boolean, default=False)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))