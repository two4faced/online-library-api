import enum

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Enum

from src.database.db import Base


class UserRole(str, enum.Enum):
    READER = 'reader'
    AUTHOR = 'author'
    ADMIN = 'admin'


class UsersORM(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(60))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    role: Mapped[UserRole] = mapped_column(Enum(UserRole), default=UserRole.READER)
    hashed_password: Mapped[str]
