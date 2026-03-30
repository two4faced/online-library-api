from pydantic import BaseModel, Field


class AddGenreDTO(BaseModel):
    title: str = Field(max_length=30)


class GenreDTO(AddGenreDTO):
    id: int


class AddBookGenreDTO(BaseModel):
    book_id: int
    genre_id: int


class BookGenreDTO(AddBookGenreDTO):
    id: int
