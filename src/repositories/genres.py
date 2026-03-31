from sqlalchemy import delete, and_
from sqlalchemy.dialects.postgresql import insert

from src.models import GenresORM
from src.models.genres import BookGenresORM
from src.repositories.base import BaseRepository
from src.schemas.books import PatchBookDTO
from src.schemas.genres import GenreDTO, BookGenreDTO


class GenresRepository(BaseRepository):
    model = GenresORM
    schema = GenreDTO


class BookGenresRepository(BaseRepository):
    model = BookGenresORM
    schema = BookGenreDTO

    async def change_book_genres(
        self,
        book_id: int,
        genres_data: PatchBookDTO,
    ):
        data_to_insert = [
            {'book_id': book_id, 'genre_id': genre_id} for genre_id in genres_data.genres
        ]

        insert_stmt = insert(self.model).values(data_to_insert)
        insert_stmt = insert_stmt.on_conflict_do_nothing(index_elements=['book_id', 'genre_id'])
        await self.session.execute(insert_stmt)

        condition = and_(
            self.model.book_id == book_id,
            self.model.genre_id.not_in(genres_data.genres),
        )

        delete_stmt = delete(self.model).where(condition)

        await self.session.execute(delete_stmt)
