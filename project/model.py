from typing import Optional

from pydantic import BaseModel


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


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


class UserDTOFull(UserDTO):
    password: str
