from src.models import ReviewsORM
from src.repositories.base import BaseRepository
from src.schemas.reviews import ReviewDTO


class ReviewsRepository(BaseRepository):
    model = ReviewsORM
    schema = ReviewDTO
