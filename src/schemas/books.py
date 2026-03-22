from pydantic import BaseModel, Field


class AddBookRequestDTO(BaseModel):
    title: str = Field(max_length=90)
    description: str = Field(max_length=2000)
    volume: int = Field(le=1500)
    rating: float = Field(default=0.0, ge=0, le=10)


class AddBookDTO(AddBookRequestDTO):
    author_id: int | None


class BookDTO(BaseModel):
    id: int
    author_id: int | None
    title: str = Field(max_length=90)
    description: str = Field(max_length=2000)
    volume: int = Field(le=1500)
    rating: float = Field(default=0.0, ge=0, le=10)
