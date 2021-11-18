from datetime import datetime
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


class Challenge(BaseModel):
    id: str
    name: str = None
    description: Optional[str] = None
    active_from: datetime
    active_until: Optional[datetime] = None
    created: Optional[datetime] = None
    frequency: str
    price: float
    creator: str


class ChallengeDTO(BaseModel):
    name: str = None
    description: Optional[str] = None
    active_from: datetime
    active_until: Optional[datetime] = None
    frequency: str
    price: float
