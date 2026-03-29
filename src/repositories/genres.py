from src.models import GenresORM
from src.repositories.base import BaseRepository
from src.schemas.genres import GenreDTO


class GenresRepository(BaseRepository):
    model = GenresORM
    schema = GenreDTO