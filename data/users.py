import sqlalchemy
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from sqlalchemy_serializer import SerializerMixin

class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    token = sqlalchemy.Column(sqlalchemy.String, nullable=True)