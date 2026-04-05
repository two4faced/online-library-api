from typing import Any, Annotated

from pydantic import BaseModel
from typing_extensions import AsyncGenerator
from fastapi import Request, Depends, Query

from src.database.db import async_session_maker
from src.database.db_manager import DBManager
from src.exceptions import (
    InvalidTokenException,
    InvalidTokenHTTPException,
    NotAuthenticatedHTTPException,
)
from src.services.auth import AuthService, auth_service


class PaginationParameters(BaseModel):
    page: Annotated[int, Query(1, ge=1)] = 1
    page_size: Annotated[int | None, Query(None, ge=1, lt=100)] = 10


async def get_db() -> AsyncGenerator[DBManager, Any]:
    async with DBManager(session_factory=async_session_maker) as db:
        yield db


def get_access_token(request: Request) -> str:
    token = request.cookies.get('access_token', None)

    if not token:
        raise NotAuthenticatedHTTPException

    auth_service.decode_token(token)
    return token


def get_user_id(token: str = Depends(get_access_token)) -> int:
    try:
        payload = auth_service.decode_token(token)
        return int(payload['sub'])
    except InvalidTokenException:
        raise InvalidTokenHTTPException


async def get_current_user(user_id: int = Depends(get_user_id), db: DBManager = Depends(get_db)):
    return await db.users.get_one(id=user_id)


def get_auth_service() -> AuthService:
    return auth_service
