from src.schemas.chapters import AddBookChapterRequestDTO, AddBookChapterDTO
from src.services.base import BaseService


class ChaptersService(BaseService):
    async def get_all_chapters(self, book_id: int):
        return await self.db.chapters.get_all(book_id=book_id)

    async def get_chapter(self, book_id: int, chapter_number: int):
        return await self.db.chapters.get_one(book_id=book_id, chapter_number=chapter_number)

    async def add_chapter(self, book_id: int, chapter_data: AddBookChapterRequestDTO):
        chapter_number = await self.db.chapters.get_next_chapter_number(book_id=book_id)
        new_chapter_data = AddBookChapterDTO(
            book_id=book_id, chapter_number=chapter_number, **chapter_data.model_dump()
        )
        new_chapter = await self.db.chapters.add(new_chapter_data)
        await self.db.commit()
        return new_chapter
