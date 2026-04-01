from pydantic import BaseModel, Field


class AddReviewRequestDTO(BaseModel):
    rating: int = Field(gt=0, le=10)
    content: str = Field(min_length=1, max_length=1000)


class AddReviewDTO(AddReviewRequestDTO):
    author_id: int
    book_id: int


class ReviewDTO(AddReviewDTO):
    id: int
