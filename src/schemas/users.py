from pydantic import BaseModel


class UsersDTO(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    hashed_password: str
