from fastapi import APIRouter, Depends

from src.api.dependencies import get_db, get_user_id
from src.database.db_manager import DBManager
from src.schemas.books import AddBookRequestDTO, AddBookDTO, PatchBookDTO
from src.services.books import BooksService

router = APIRouter(prefix='/books', tags=['books'])


@router.get('', summary='get all books')
async def get_all_books(db: DBManager = Depends(get_db)):
    return await BooksService(db).get_all_books()


@router.get('/{book_id}', summary='get one book by id')
async def get_one_book(book_id: int, db: DBManager = Depends(get_db)):
    return await BooksService(db).get_one_book(book_id=book_id)


@router.post('', summary='add new book')
async def add_book(
    book_data: AddBookRequestDTO,
    db: DBManager = Depends(get_db),
    user_id: int = Depends(get_user_id),
):
    new_book = await BooksService(db).add_book(book_data=book_data, user_id=user_id)
    return new_book


@router.delete('{book_id}', summary='delete book')
async def delete_book(book_id: int, db: DBManager = Depends(get_db)):
    await BooksService(db).delete_book(book_id=book_id)
    return {'status': 200}


@router.patch('{book_id}', summary='partially change book')
async def change_book(book_data: PatchBookDTO, book_id: int, db: DBManager = Depends(get_db)):
    await BooksService(db).change_book(book_data=book_data, book_id=book_id)
    return {'status': 200}
