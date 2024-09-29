import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase
import datetime
from datetime import timezone
from sqlalchemy_serializer import SerializerMixin


class Product(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'products'

    uuid = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    vendor_id = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("vendors.uuid"), nullable=False)
    title = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    description = sqlalchemy.Column(sqlalchemy.Text)
    characteristics = sqlalchemy.Column(sqlalchemy.String)
    feedback = sqlalchemy.Column(sqlalchemy.String)
    photos = sqlalchemy.Column(sqlalchemy.String)
    statistics = sqlalchemy.Column(sqlalchemy.String) # path to file
    isaccepted = sqlalchemy.Column(sqlalchemy.Boolean)
    public_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now(timezone.utc))