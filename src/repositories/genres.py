from src.models import GenresORM
from src.models.genres import BookGenresORM
from src.repositories.base import BaseRepository
from src.schemas.genres import GenreDTO, BookGenreDTO


class GenresRepository(BaseRepository):
    model = GenresORM
    schema = GenreDTO


class BookGenresRepository(BaseRepository):
    model = BookGenresORM
    schema = BookGenreDTO
