import typing

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, String, Text

from src.database.db import Base

if typing.TYPE_CHECKING:
    from src.models import GenresORM


class BooksORM(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    title: Mapped[str] = mapped_column(String(90))
    description: Mapped[str] = mapped_column(Text)
    volume: Mapped[int]
    rating: Mapped[float] = mapped_column(default=0.0)

    genres: Mapped[list['GenresORM']] = relationship(
        back_populates='books', secondary='book_genres'
    )
