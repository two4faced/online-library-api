from src.schemas.genres import AddGenreDTO
from src.services.base import BaseService


class GenresService(BaseService):
    async def get_all_genres(self):
        return await self.db.genres.get_all()

    async def add_genre(self, genre_data: AddGenreDTO):
        new_genre = await self.db.genres.add(genre_data)
        await self.db.commit()
        return new_genre