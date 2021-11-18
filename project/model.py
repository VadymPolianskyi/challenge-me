from typing import Optional

from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class User(BaseModel):
    username: str
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    token: Optional[str] = None


class UserDTO(BaseModel):
    username: str
    name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None


class RegistrationUserDTO(UserDTO):
    password: str
