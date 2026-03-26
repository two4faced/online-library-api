from fastapi import APIRouter
from fastapi.params import Depends

from src.api.dependencies import get_db
from src.database.db_manager import DBManager
from src.schemas.chapters import AddBookChapterRequestDTO, AddBookChapterDTO

router = APIRouter(prefix='/books/chapters', tags=['chapters'])


@router.get('/{book_id}', summary='get all chapters for specific book by id')
async def get_all_chapters(book_id: int, db: DBManager = Depends(get_db)):
    return await db.chapters.get_all(book_id=book_id)


@router.get('/{book_id}/{chapter_number}', summary='get one chapter with content')
async def get_chapter(book_id: int, chapter_number: int, db: DBManager = Depends(get_db)):
    return await db.chapters.get_one(book_id=book_id, chapter_number=chapter_number)


@router.post('/{book_id}', summary='add new chapter')
async def add_chapter(
    book_id: int, chapter_data: AddBookChapterRequestDTO, db: DBManager = Depends(get_db)
):
    chapter_number = await db.chapters.get_next_chapter_number(book_id=book_id)

    new_chapter_data = AddBookChapterDTO(
        book_id=book_id, chapter_number=chapter_number, **chapter_data.model_dump()
    )
    new_chapter = await db.chapters.add(new_chapter_data)

    await db.commit()
    return new_chapter
