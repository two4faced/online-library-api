from src.schemas.books import AddBookRequestDTO, AddBookDTO, PatchBookDTO, RequestPatchBookDTO
from src.schemas.genres import AddBookGenreDTO
from src.services.base import BaseService


class BooksService(BaseService):
    async def get_all_books(self, page, page_size, title: str | None, author: str | None):
        return await self.db.books.get_books_with_genres(
            page=page, page_size=page_size, title=title, author=author
        )

    async def get_one_book(self, book_id: int):
        return await self.db.books.get_one_book_with_genres(id=book_id)

    async def add_book(self, book_data: AddBookRequestDTO, user_id: int):
        new_book_data = AddBookDTO(author_id=user_id, **book_data.model_dump())
        new_book = await self.db.books.add(new_book_data)

        book_genres_data = [
            AddBookGenreDTO(book_id=new_book.id, genre_id=gen_id) for gen_id in book_data.genres
        ]
        await self.db.book_genres.add_bulk(book_genres_data)

        await self.db.commit()
        return new_book

    async def delete_book(self, book_id: int):
        await self.db.books.delete(id=book_id)
        await self.db.commit()

    async def change_book(self, book_data: RequestPatchBookDTO, book_id: int):
        changed_book_data = PatchBookDTO(**book_data.model_dump(exclude_unset=True))

        if book_data.genres:
            await self.db.book_genres.change_book_genres(book_id=book_id, genres_data=book_data)

        await self.db.books.change(changed_book_data, exclude_unset=True, id=book_id)
        await self.db.commit()
