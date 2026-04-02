from src.schemas.reviews import AddReviewRequestDTO, AddReviewDTO, PatchReviewDTO
from src.services.base import BaseService


class ReviewsService(BaseService):
    async def get_all_reviews(self, book_id: int):
        return await self.db.reviews.get_all(book_id=book_id)

    async def add_review(
        self,
        review_data: AddReviewRequestDTO,
        book_id: int,
        user_id: int,
    ):
        new_review_data = AddReviewDTO(
            book_id=book_id, author_id=user_id, **review_data.model_dump()
        )
        new_review = await self.db.reviews.add(new_review_data)
        await self.db.commit()
        return new_review

    async def delete_review(self, book_id: int, review_id: int, user_id: int):
        await self.db.reviews.delete(id=review_id, author_id=user_id, book_id=book_id)
        await self.db.commit()

    async def change_review(
        self, review_data: PatchReviewDTO, book_id: int, review_id: int, user_id: int
    ):
        await self.db.reviews.change(
            review_data, exclude_unset=True, book_id=book_id, author_id=user_id, id=review_id
        )
        await self.db.commit()
        return {'status': 200}
