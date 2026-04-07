from pydantic import EmailStr
from sqlalchemy import select

from src.models.users import UsersORM
from src.repositories.base import BaseRepository
from src.schemas.users import UserDTO, UserWithHashedPasswordDTO


class UsersRepository(BaseRepository):
    model = UsersORM
    schema = UserDTO

    async def get_all(self, page: int = 1, page_size: int = 10):
        offset = (page - 1) * page_size

        query = select(self.model)
        query = query.offset(offset).limit(page_size)
        result = await self.session.execute(query)

        return [
            self.schema.model_validate(model, from_attributes=True)
            for model in result.scalars().all()
        ]

    async def get_user_with_hashed_password(self, email: EmailStr):
        query = select(self.model).filter_by(email=email)
        result = await self.session.execute(query)
        model = result.scalars().one()

        return UserWithHashedPasswordDTO.model_validate(model, from_attributes=True)
