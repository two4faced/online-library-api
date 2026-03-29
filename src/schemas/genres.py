from pydantic import BaseModel, Field


class AddGenreDTO(BaseModel):
    title: str = Field(max_length=30)


class GenreDTO(AddGenreDTO):
    id: int