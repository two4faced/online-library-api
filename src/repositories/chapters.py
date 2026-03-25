from src.models.books import BookChaptersORM
from src.repositories.base import BaseRepository
from src.schemas.chapters import BookChaptersDTO


class BookChaptersRepository(BaseRepository):
    model = BookChaptersORM
    schema = BookChaptersDTO
