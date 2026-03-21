from fastapi import APIRouter, Depends, Response

from src.api.dependencies import get_auth_service
from src.db import async_session_maker
from src.repositories.users import UsersRepository
from src.schemas.users import RegisterUserRequestDTO, RegisterUserDTO, LoginUserDTO
from src.services.auth import AuthService

router = APIRouter(prefix='/auth', tags=['authentication and authorization'])


@router.post('/register')
async def registration(
    credentials: RegisterUserRequestDTO, auth_service: AuthService = Depends(get_auth_service)
):
    new_user_data = RegisterUserDTO(
        name=credentials.name,
        surname=credentials.surname,
        email=credentials.email,
        hashed_password=auth_service.hash_password(credentials.password),
    )
    async with async_session_maker() as session:
        await UsersRepository(session).add(new_user_data)
        await session.commit()

    return {'status': 200}


@router.post('/login')
async def login(credentials: LoginUserDTO, response: Response, auth_service: AuthService = Depends(get_auth_service)):
    async with async_session_maker() as session:
        user = await UsersRepository(session).get_user_with_hashed_password(email=credentials.email)
        if auth_service.verify_password(credentials.password, user.hashed_password):
            token = auth_service.create_access_token(user_id=str(user.id))
            response.set_cookie('access_token', token)
            return {'access_token': token}
        return None


@router.post('/logout')
async def logout(response: Response):
    response.delete_cookie('access_token')

    return {'status': 200}