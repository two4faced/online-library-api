from pydantic import BaseModel, Field, ConfigDict

from src.schemas.genres import GenreDTO


class AddBookRequestDTO(BaseModel):
    title: str = Field(max_length=90)
    description: str = Field(max_length=2000)
    volume: int = Field(le=1500)
    genres: list[int] | None = Field(None)


class AddBookDTO(BaseModel):
    author_id: int | None
    title: str = Field(max_length=90)
    description: str = Field(max_length=2000)
    volume: int = Field(le=1500)
    rating: float = Field(default=0.0, ge=0, le=10)


class BookDTO(BaseModel):
    id: int
    author_id: int | None
    title: str = Field(max_length=90)
    description: str = Field(max_length=2000)
    volume: int = Field(le=1500)
    rating: float = Field(default=0.0, ge=0, le=10)


class BookWithGenresDTO(BookDTO):
    genres: list[GenreDTO]


class RequestPatchBookDTO(BaseModel):
    title: str | None = Field(default=None, max_length=90)
    description: str | None = Field(default=None, max_length=2000)
    volume: int | None = Field(default=None, le=1500)
    genres: list[int] | None = Field(None)


class PatchBookDTO(BaseModel):
    title: str | None = Field(default=None, max_length=90)
    description: str | None = Field(default=None, max_length=2000)
    volume: int | None = Field(default=None, le=1500)

    model_config = ConfigDict(extra='ignore')
