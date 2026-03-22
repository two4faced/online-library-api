from fastapi import APIRouter, Depends

from src.api.dependencies import get_db
from src.database.db_manager import DBManager

router = APIRouter(prefix='/books', tags=['books'])


@router.get('')
async def get_all_books(db: DBManager = Depends(get_db)):
    return await db.books.get_all()


@router.get('/{book_id}')
async def get_one_book(book_id: int, db: DBManager = Depends(get_db)):
    return await db.books.get_one_or_none(id=book_id)
