from src.models.users import UsersORM
from src.repositories.base import BaseRepository
from src.schemas.users import UsersDTO


class UsersRepository(BaseRepository):
    model = UsersORM
    schema = UsersDTO
