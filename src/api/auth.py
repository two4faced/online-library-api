from fastapi import APIRouter, Depends, Response

from src.api.dependencies import get_auth_service, get_db, get_user_id
from src.database.db_manager import DBManager
from src.schemas.users import RegisterUserRequestDTO, RegisterUserDTO, LoginUserDTO
from src.services.auth import AuthService

router = APIRouter(prefix='/auth', tags=['authentication and authorization'])


@router.post('/register')
async def registration(
    credentials: RegisterUserRequestDTO,
    db: DBManager = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
):
    new_user_data = RegisterUserDTO(
        name=credentials.name,
        surname=credentials.surname,
        email=credentials.email,
        hashed_password=auth_service.hash_password(credentials.password),
    )
    await db.users.add(new_user_data)
    await db.commit()

    return {'status': 200}


@router.post('/login')
async def login(
    credentials: LoginUserDTO,
    response: Response,
    db: DBManager = Depends(get_db),
    auth_service: AuthService = Depends(get_auth_service),
):
    user = await db.users.get_user_with_hashed_password(email=credentials.email)
    if auth_service.verify_password(credentials.password, user.hashed_password):
        token = auth_service.create_access_token(user_id=str(user.id))
        response.set_cookie('access_token', token)
        return {'access_token': token}
    return None


@router.get('/me')
async def get_me(
    user_id=Depends(get_user_id),
    db: DBManager = Depends(get_db),
):
    return await db.users.get_one(id=user_id)


@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('access_token')

    return {'status': 200}
