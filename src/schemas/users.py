from pydantic import BaseModel, EmailStr, Field


class RegisterUserRequestDTO(BaseModel):
    name: str = Field(min_length=2, max_length=30)
    surname: str = Field(min_length=1, max_length=60)
    email: EmailStr = Field(max_length=100)
    password: str


class RegisterUserDTO(BaseModel):
    name: str
    surname: str
    email: EmailStr
    hashed_password: str


class LoginUserDTO(BaseModel):
    email: EmailStr
    password: str


class UserDTO(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr


class UserWithHashedPasswordDTO(UserDTO):
    hashed_password: str
