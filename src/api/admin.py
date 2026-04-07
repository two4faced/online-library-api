from typing import Annotated

from fastapi import APIRouter, Depends

from src.database.db_manager import DBManager
from src.dependencies.dependencies import get_db, PaginationParameters
from src.dependencies.role_checker import require_admin
from src.services.admin import AdminService

router = APIRouter(prefix='/admin', tags=['admin'])


@router.get('/users', dependencies=[require_admin], summary='get users')
async def get_all_users(
    pagination: Annotated[PaginationParameters, Depends()], db: DBManager = Depends(get_db)
):
    return await AdminService(db).get_all_users(page=pagination.page, page_size=pagination.page_size)


@router.delete('/users/{user_id}', dependencies=[require_admin], summary='delete user by id')
async def delete_user(user_id: int, db: DBManager = Depends(get_db)):
    await AdminService(db).delete_user(user_id=user_id)
    return {'status': 200}
