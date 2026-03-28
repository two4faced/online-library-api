from src.exceptions import InvalidCredentialsException
from src.schemas.users import RegisterUserRequestDTO, RegisterUserDTO, LoginUserDTO
from src.services.auth import auth_service
from src.services.base import BaseService


class UserService(BaseService):
    async def registration(self, credentials: RegisterUserRequestDTO):
        new_user_data = RegisterUserDTO(
            name=credentials.name,
            surname=credentials.surname,
            email=credentials.email,
            hashed_password=auth_service.hash_password(credentials.password),
        )
        await self.db.users.add(new_user_data)
        await self.db.commit()

    async def login(self, credentials: LoginUserDTO):
        user = await self.db.users.get_user_with_hashed_password(email=credentials.email)
        if auth_service.verify_password(credentials.password, user.hashed_password):
            token = auth_service.create_access_token(user_id=str(user.id))
            return token
        raise InvalidCredentialsException

    async def get_me(self, user_id: int):
        return await self.db.users.get_one(id=user_id)
