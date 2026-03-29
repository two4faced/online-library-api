from fastapi import APIRouter, Depends

from src.database.db_manager import DBManager
from src.dependencies.dependencies import get_db
from src.schemas.genres import AddGenreDTO
from src.services.genres import GenresService

router = APIRouter(prefix='/genres', tags=['genres'])


@router.get('')
async def get_all_genres(db: DBManager = Depends(get_db)):
    return await GenresService(db).get_all_genres()


@router.post('')
async def add_genre(genre_data: AddGenreDTO, db: DBManager = Depends(get_db)):
    new_genre = await GenresService(db).add_genre(genre_data)
    return new_genre