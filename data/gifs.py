import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Gif(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'gifs'

    id = sqlalchemy.Column(sqlalchemy.String, primary_key=True)
    en = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    ru = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
