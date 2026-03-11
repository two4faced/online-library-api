from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Text

from src.db import Base


class BooksORM(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    title: Mapped[str] = mapped_column(String(90))
    description: Mapped[str] = mapped_column(Text)
    volume: Mapped[int]
    rating: Mapped[float] = mapped_column(default=0.0)
