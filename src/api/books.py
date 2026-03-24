from fastapi import APIRouter, Depends

from src.api.dependencies import get_db, get_user_id
from src.database.db_manager import DBManager
from src.schemas.books import AddBookRequestDTO, AddBookDTO, PatchBookDTO

router = APIRouter(prefix='/books', tags=['books'])


@router.get('', summary='get all books')
async def get_all_books(db: DBManager = Depends(get_db)):
    return await db.books.get_all()


@router.get('/{book_id}', summary='get one book by id')
async def get_one_book(book_id: int, db: DBManager = Depends(get_db)):
    return await db.books.get_one_or_none(id=book_id)


@router.post('', summary='add new book')
async def add_book(
    book_data: AddBookRequestDTO,
    db: DBManager = Depends(get_db),
    user_id: int = Depends(get_user_id),
):
    new_book_data = AddBookDTO(author_id=user_id, **book_data.model_dump())
    new_book = await db.books.add(new_book_data)

    await db.commit()
    return new_book


@router.delete('{book_id}', summary='delete book')
async def delete_book(book_id: int, db: DBManager = Depends(get_db)):
    await db.books.delete(id=book_id)
    await db.commit()
    return {'status': 200}


@router.patch('{book_id}', summary='partially change book')
async def change_book(book_data: PatchBookDTO, book_id: int, db: DBManager = Depends(get_db)):
    await db.books.change(book_data, exclude_unset=True, id=book_id)
    await db.commit()
    return {'status': 200}
