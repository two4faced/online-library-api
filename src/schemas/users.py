from pydantic import BaseModel, EmailStr, Field


class RegisterUserRequestDTO(BaseModel):
    name: str = Field(ge=2, le=30)
    surname: str = Field(ge=1, le=60)
    email: EmailStr = Field(le=100)
    password: str


class RegisterUserDTO(BaseModel):
    name: str
    surname: str
    email: EmailStr
    hashed_password: str


class UserDTO(BaseModel):
    id: int
    name: str
    surname: str
    email: EmailStr
