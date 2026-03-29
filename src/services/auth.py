from datetime import timedelta

from jose import jwt, JWTError
from authx import AuthXConfig, AuthX
from passlib.context import CryptContext

from src.config import settings
from src.exceptions import InvalidTokenException


class AuthService:
    config = AuthXConfig(
        JWT_SECRET_KEY=settings.SECRET_KEY,
        JWT_ACCESS_COOKIE_NAME='access_token',
        JWT_ACCESS_TOKEN_EXPIRES=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        JWT_TOKEN_LOCATION=['cookies'],
        JWT_COOKIE_SAMESITE='lax',
        JWT_COOKIE_HTTP_ONLY=True,
        JWT_COOKIE_SECURE=True,
    )

    def __init__(self):
        self.pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
        self.security = AuthX(config=self.config)

    def hash_password(self, plain_password):
        return self.pwd_context.hash(plain_password)

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def create_access_token(self, user_id: str):
        token = self.security.create_access_token(uid=user_id)
        return token

    def decode_token(self, token: str):
        try:
            payload = jwt.decode(
                token,
                self.config.JWT_SECRET_KEY,
                algorithms=[self.config.JWT_ALGORITHM],
            )
            return payload
        except JWTError:
            raise InvalidTokenException


auth_service = AuthService()
