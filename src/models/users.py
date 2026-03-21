from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String

from src.database.db import Base


class UsersORM(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    surname: Mapped[str] = mapped_column(String(60))
    email: Mapped[str] = mapped_column(String(100), unique=True)
    hashed_password: Mapped[str]
