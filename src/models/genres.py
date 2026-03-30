import typing

from sqlalchemy import String, ForeignKey, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.db import Base

if typing.TYPE_CHECKING:
    from src.models import BooksORM


class GenresORM(Base):
    __tablename__ = 'genres'

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(30))
    books: Mapped[list['BooksORM']] = relationship(back_populates='genres', secondary='book_genres')


class BookGenresORM(Base):
    __tablename__ = 'book_genres'

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    genre_id: Mapped[int] = mapped_column(ForeignKey('genres.id'))

    __table_args__ = (UniqueConstraint('book_id', 'genre_id', name='uq_book_genre'),)
