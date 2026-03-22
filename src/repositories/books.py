from src.models import BooksORM
from src.repositories.base import BaseRepository
from src.schemas.books import BookDTO


class BooksRepository(BaseRepository):
    model = BooksORM
    schema = BookDTO
