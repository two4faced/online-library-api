from datetime import date

from sqlalchemy import ForeignKey, CheckConstraint, Text, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import SMALLINT

from src.database.db import Base


class ReviewsORM(Base):
    __tablename__ = 'reviews'

    id: Mapped[int] = mapped_column(primary_key=True)
    author_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    book_id: Mapped[int] = mapped_column(ForeignKey('books.id'))
    rating: Mapped[int] = mapped_column(SMALLINT(), CheckConstraint('rating > 0 AND rating <= 10'))
    content: Mapped[str] = mapped_column(Text())
    posted: Mapped[date]

    __table_args__ = (UniqueConstraint('author_id', 'book_id', name='uq_author_book'),)
