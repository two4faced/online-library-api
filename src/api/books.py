from fastapi import APIRouter, Depends

from src.dependencies.dependencies import get_db, get_user_id
from src.database.db_manager import DBManager
from src.dependencies.role_checker import author_or_admin_depends
from src.schemas.books import AddBookRequestDTO, PatchBookDTO
from src.services.books import BooksService

router = APIRouter(prefix='/books', tags=['books'])


@router.get('', summary='get all books')
async def get_all_books(db: DBManager = Depends(get_db)):
    return await BooksService(db).get_all_books()


@router.get('/{book_id}', summary='get one book by id')
async def get_one_book(book_id: int, db: DBManager = Depends(get_db)):
    return await BooksService(db).get_one_book(book_id=book_id)


@router.post('', summary='add new book', dependencies=[author_or_admin_depends])
async def add_book(
    book_data: AddBookRequestDTO,
    db: DBManager = Depends(get_db),
    user_id: int = Depends(get_user_id),
):
    new_book = await BooksService(db).add_book(book_data=book_data, user_id=user_id)
    return new_book


@router.delete('{book_id}', summary='delete book', dependencies=[author_or_admin_depends])
async def delete_book(book_id: int, db: DBManager = Depends(get_db)):
    await BooksService(db).delete_book(book_id=book_id)
    return {'status': 200}


@router.patch('{book_id}', summary='partially change book', dependencies=[author_or_admin_depends])
async def change_book(book_data: PatchBookDTO, book_id: int, db: DBManager = Depends(get_db)):
    await BooksService(db).change_book(book_data=book_data, book_id=book_id)
    return {'status': 200}
