from fastapi import APIRouter, Depends, Response

from src.api.dependencies import get_db, get_user_id
from src.database.db_manager import DBManager
from src.exceptions import InvalidCredentialsException, InvalidCredentialsHTTPException
from src.schemas.users import RegisterUserRequestDTO, LoginUserDTO
from src.services.users import UsersService

router = APIRouter(prefix='/auth', tags=['authentication and authorization'])


@router.post('/register')
async def registration(
    credentials: RegisterUserRequestDTO,
    db: DBManager = Depends(get_db),
):
    await UsersService(db).registration(credentials)
    return {'status': 200}


@router.post('/login')
async def login(credentials: LoginUserDTO, response: Response, db: DBManager = Depends(get_db)):
    try:
        token = await UsersService(db).login(credentials)
    except InvalidCredentialsException:
        raise InvalidCredentialsHTTPException

    response.set_cookie('access_token', token)
    return {'access_token': token}


@router.get('/me')
async def get_me(
    user_id=Depends(get_user_id),
    db: DBManager = Depends(get_db),
):
    return await UsersService(db).get_me(user_id)


@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('access_token')
    return {'status': 200}
