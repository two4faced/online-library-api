from sqlalchemy import select, func

from src.models.chapters import BookChaptersORM
from src.repositories.base import BaseRepository
from src.schemas.chapters import BookChaptersDTO, BookChaptersContentDTO


class BookChaptersRepository(BaseRepository):
    model = BookChaptersORM
    schema = BookChaptersDTO

    async def get_one(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalars().one()

        return BookChaptersContentDTO.model_validate(model, from_attributes=True)

    async def get_next_chapter_number(self, book_id: int):
        query = select(func.max(self.model.chapter_number)).filter_by(book_id=book_id)
        result = await self.session.execute(query)
        current_max_chapter_number = result.scalars().one_or_none()

        return (current_max_chapter_number or 0) + 1
