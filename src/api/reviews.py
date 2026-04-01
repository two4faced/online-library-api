from fastapi import APIRouter, Depends

from src.database.db_manager import DBManager
from src.dependencies.dependencies import get_db, get_user_id
from src.schemas.reviews import AddReviewRequestDTO, AddReviewDTO
from src.services.reviews import ReviewsService

router = APIRouter(prefix='/books', tags=['reviews'])


@router.get('/{book_id}/reviews', summary='get reviews for book')
async def get_all_reviews(
    book_id: int,
    db: DBManager = Depends(get_db),
):
    return await ReviewsService(db).get_all_reviews(book_id)


@router.post('/{book_id}/reviews', summary='write a new review for book')
async def add_review(
    review_data: AddReviewRequestDTO,
    book_id: int,
    user_id: int = Depends(get_user_id),
    db: DBManager = Depends(get_db),
):
    new_review = await ReviewsService(db).add_review(
        review_data=review_data, book_id=book_id, user_id=user_id
    )
    return new_review
