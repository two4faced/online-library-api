from sqlalchemy import select
from sqlalchemy.orm import selectinload

from src.models import BooksORM
from src.repositories.base import BaseRepository
from src.schemas.books import BookDTO, BookWithGenresDTO


class BooksRepository(BaseRepository):
    model = BooksORM
    schema = BookDTO

    async def get_books_with_genres(self, *filters, **filter_by):
        query = select(self.model).options(selectinload(self.model.genres))
        result = await self.session.execute(query)
        return [
            BookWithGenresDTO.model_validate(model, from_attributes=True)
            for model in result.scalars().all()
        ]

    async def get_one_book_with_genres(self, **filter_by):
        query = select(self.model).options(selectinload(self.model.genres)).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalar_one()
        return BookWithGenresDTO.model_validate(model, from_attributes=True)
