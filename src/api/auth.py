from fastapi import APIRouter
from passlib.context import CryptContext

from src.db import async_session_maker
from src.repositories.users import UsersRepository
from src.schemas.users import RegisterUserRequestDTO, RegisterUserDTO

router = APIRouter(prefix='/auth', tags=['authentication and authorization'])

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


@router.post('/register')
async def registration(
        user_data: RegisterUserRequestDTO
):
    new_user_data = RegisterUserDTO(
        name=user_data.name,
        surname=user_data.surname,
        email=user_data.email,
        hashed_password=pwd_context.hash(user_data.password)
    )
    async with async_session_maker() as session:
        await UsersRepository(session).add(new_user_data)
        await session.commit()

    return {'status': 200}