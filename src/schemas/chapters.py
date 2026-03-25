from pydantic import BaseModel, Field


class AddBookChapterRequestDTO(BaseModel):
    chapter_number: int
    chapter_name: str = Field(min_length=1, max_length=150)
    content: str


class AddBookChapterDTO(AddBookChapterRequestDTO):
    book_id: int


class BookChaptersDTO(BaseModel):
    id: int
    book_id: int
    chapter_number: int
    chapter_name: str = Field(min_length=1, max_length=150)


class BookChaptersContentDTO(BookChaptersDTO):
    content: str
