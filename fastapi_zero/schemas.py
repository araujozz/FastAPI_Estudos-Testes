from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserPublic(BaseModel):
    usuario: str
    email: EmailStr
    id: int


class UserSchemas(BaseModel):
    usuario: str
    email: EmailStr
    senha: str


class UserDB(UserSchemas):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
