from typing import Annotated, Any

from fastapi import Depends
from typing_extensions import AsyncGenerator

from src.database.db import async_session_maker
from src.database.db_manager import DBManager
from src.services.auth import AuthService


def get_auth_service() -> AuthService:
    return AuthService()


async def get_db() -> AsyncGenerator[DBManager, Any]:
    async with DBManager(session_factory=async_session_maker) as db:
        yield db
