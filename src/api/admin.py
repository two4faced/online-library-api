from typing import Annotated

from fastapi import APIRouter, Depends

from src.database.db_manager import DBManager
from src.dependencies.dependencies import get_db, PaginationParameters
from src.dependencies.role_checker import require_admin
from src.schemas.users import AdminPatchUserDTO
from src.services.admin import AdminService

router = APIRouter(prefix='/admin', tags=['admin'], dependencies=[require_admin])


@router.get('/users', summary='get users')
async def get_all_users(
    pagination: Annotated[PaginationParameters, Depends()], db: DBManager = Depends(get_db)
):
    return await AdminService(db).get_all_users(
        page=pagination.page, page_size=pagination.page_size
    )


@router.patch('/users/{user_id}')
async def change_user(user_data: AdminPatchUserDTO, user_id: int, db: DBManager = Depends(get_db)):
    await AdminService(db).change_user(user_data, user_id)
    return {'status': 200}


@router.delete('/users/{user_id}', summary='delete user by id')
async def delete_user(user_id: int, db: DBManager = Depends(get_db)):
    await AdminService(db).delete_user(user_id=user_id)
    return {'status': 200}


@router.delete('/reviews/{review_id}')
async def delete_review(review_id: int, db: DBManager = Depends(get_db)):
    await AdminService(db).delete_review(review_id)
    return {'status': 200}


@router.delete('/books/{book_id}')
async def delete_book(book_id: int, db: DBManager = Depends(get_db)):
    await AdminService(db).delete_book(book_id)
    return {'status': 200}
