from sqlalchemy import ForeignKey, String, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from src.database.db import Base


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
