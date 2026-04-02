from datetime import date

from pydantic import BaseModel, Field


class AddReviewRequestDTO(BaseModel):
    rating: int = Field(gt=0, le=10)
    content: str = Field(min_length=1, max_length=1000)


class AddReviewDTO(AddReviewRequestDTO):
    author_id: int
    book_id: int
    posted: date = Field(default=date.today())


class ReviewDTO(AddReviewDTO):
    id: int


class PatchReviewDTO(BaseModel):
    rating: int | None = Field(default=None, gt=0, le=10)
    content: str | None = Field(default=None, min_length=1, max_length=1000)
