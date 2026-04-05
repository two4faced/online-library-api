from sqlalchemy import select, desc, func
from sqlalchemy.orm import selectinload

from src.models import BooksORM
from src.repositories.base import BaseRepository
from src.repositories.utils import get_author_ids_for_books
from src.schemas.books import BookDTO, BookWithGenresDTO


class BooksRepository(BaseRepository):
    model = BooksORM
    schema = BookDTO

    async def get_books_with_genres(
        self,
        title: str | None,
        author: str | None,
        page: int = 1,
        page_size: int = 10,
    ):
        offset = (page - 1) * page_size

        query = select(self.model).options(selectinload(self.model.genres))
        count_query = select(func.count()).select_from(self.model)

        if title:
            query = query.filter(self.model.title.icontains(title.strip()))
            count_query = count_query.filter(self.model.title.icontains(title.strip()))

        if author:
            author_subquery = get_author_ids_for_books(author.strip())
            query = query.filter(self.model.author_id.in_(author_subquery))
            count_query = count_query.filter(self.model.author_id.in_(author_subquery))

        query = query.order_by(desc(self.model.rating))
        query = query.offset(offset).limit(page_size)

        result = await self.session.execute(query)
        total = (await self.session.execute(count_query)).scalar()

        return {
            'total': total,
            'page': page,
            'page_size': page_size,
            'items': [
                BookWithGenresDTO.model_validate(model, from_attributes=True)
                for model in result.scalars().all()
            ],
        }

    async def get_one_book_with_genres(self, **filter_by):
        query = select(self.model).options(selectinload(self.model.genres)).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalar_one()
        return BookWithGenresDTO.model_validate(model, from_attributes=True)
