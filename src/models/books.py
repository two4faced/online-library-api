from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey, String, Text, UniqueConstraint

from src.database.db import Base


class BooksORM(Base):
    __tablename__ = 'books'

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'), nullable=True)
    title: Mapped[str] = mapped_column(String(90))
    description: Mapped[str] = mapped_column(Text)
    volume: Mapped[int]
    rating: Mapped[float] = mapped_column(default=0.0)


class BookChaptersORM(Base):
    __tablename__ = 'book_chapters'

    id: Mapped[int] = mapped_column(primary_key=True)
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    chapter_number: Mapped[int]
    chapter_name: Mapped[str] = mapped_column(String(150))
    content: Mapped[str] = mapped_column(Text)

    __table_args__ = (
        UniqueConstraint('book_id', 'chapter_number', name='uq_book_id_chapter_number'),
    )
