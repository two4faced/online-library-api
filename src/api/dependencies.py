from typing import Any

from typing_extensions import AsyncGenerator
from fastapi import Request, Depends

from src.database.db import async_session_maker
from src.database.db_manager import DBManager
from src.services.auth import AuthService


async def get_db() -> AsyncGenerator[DBManager, Any]:
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


def get_access_token(request: Request) -> str:
    token = request.cookies.get('access_token', None)
    return token


def get_user_id(token: str = Depends(get_access_token)) -> int:
    token_data = AuthService().decode_token(token)
    return int(token_data.sub)


def get_auth_service() -> AuthService:
    return AuthService()
