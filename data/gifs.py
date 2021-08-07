import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy_serializer import SerializerMixin


class Gif(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'gifs'

    id = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    link = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    words_en = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    words_ru = sqlalchemy.Column(sqlalchemy.String, nullable=True)
