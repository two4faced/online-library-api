from fastapi import APIRouter, Depends

from src.api.dependencies import get_db, get_user_id
from src.database.db_manager import DBManager
from src.schemas.books import AddBookRequestDTO, AddBookDTO

router = APIRouter(prefix='/books', tags=['books'])


@router.get('')
async def get_all_books(db: DBManager = Depends(get_db)):
    return await db.books.get_all()


@router.get('/{book_id}')
async def get_one_book(book_id: int, db: DBManager = Depends(get_db)):
    return await db.books.get_one_or_none(id=book_id)


@router.post('')
async def add_book(
    book_data: AddBookRequestDTO,
    db: DBManager = Depends(get_db),
    user_id: int = Depends(get_user_id),
):
    new_book_data = AddBookDTO(author_id=user_id, **book_data.model_dump())
    new_book = await db.books.add(new_book_data)

    await db.commit()
    return new_book
