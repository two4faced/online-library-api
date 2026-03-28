from src.schemas.books import AddBookRequestDTO, AddBookDTO, PatchBookDTO
from src.services.base import BaseService


class BooksService(BaseService):
    async def get_all_books(self):
        return await self.db.books.get_all()

    async def get_one_book(self, book_id: int):
        return await self.db.books.get_one_or_none(id=book_id)

    async def add_book(self, book_data: AddBookRequestDTO, user_id: int):
        new_book_data = AddBookDTO(author_id=user_id, **book_data.model_dump())
        new_book = await self.db.books.add(new_book_data)
        await self.db.commit()
        return new_book

    async def delete_book(self, book_id: int):
        await self.db.books.delete(id=book_id)
        await self.db.commit()

    async def change_book(self, book_data: PatchBookDTO, book_id: int):
        await self.db.books.change(book_data, exclude_unset=True, id=book_id)
        await self.db.commit()
