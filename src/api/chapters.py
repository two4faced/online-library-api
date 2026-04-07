from fastapi import APIRouter
from fastapi.params import Depends

from src.dependencies.dependencies import get_db, get_access_token
from src.database.db_manager import DBManager
from src.dependencies.role_checker import require_author_or_admin
from src.schemas.chapters import AddBookChapterRequestDTO
from src.services.chapters import ChaptersService

router = APIRouter(prefix='/books/chapters', tags=['chapters'])


@router.get('/{book_id}', summary='get all chapters for specific book by id')
async def get_all_chapters(book_id: int, db: DBManager = Depends(get_db)):
    return await ChaptersService(db).get_all_chapters(book_id=book_id)


@router.get(
    '/{book_id}/{chapter_number}',
    summary='get one chapter with content',
    dependencies=[Depends(get_access_token)],
)
async def get_chapter(book_id: int, chapter_number: int, db: DBManager = Depends(get_db)):
    return await ChaptersService(db).get_chapter(book_id=book_id, chapter_number=chapter_number)


@router.post('/{book_id}', summary='add new chapter', dependencies=[require_author_or_admin])
async def add_chapter(
    book_id: int, chapter_data: AddBookChapterRequestDTO, db: DBManager = Depends(get_db)
):
    return await ChaptersService(db).add_chapter(book_id=book_id, chapter_data=chapter_data)
