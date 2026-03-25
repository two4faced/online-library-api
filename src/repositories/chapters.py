from sqlalchemy import select, func

from src.models.books import BookChaptersORM
from src.repositories.base import BaseRepository
from src.schemas.chapters import BookChaptersDTO


class BookChaptersRepository(BaseRepository):
    model = BookChaptersORM
    schema = BookChaptersDTO

    async def get_next_chapter_number(self, book_id: int):
        query = select(func.max(self.model.chapter_number)).filter_by(book_id=book_id)
        result = await self.session.execute(query)
        current_max_chapter_number = result.scalars().one_or_none()

        return (current_max_chapter_number or 0) + 1
