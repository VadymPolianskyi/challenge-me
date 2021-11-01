from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.context import CryptContext

from project.db.user import UserDaoInterface
from project.model import TokenData
from project.server.config import AuthConfig

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


class Authenticator:
    """
    Basic authentication class.
    Contains methods for the following operations:
        - create token
        - get current user from token
    """

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    def __init__(self, auth_config: AuthConfig, user_dao: UserDaoInterface):
        self.secret_key = auth_config.SECRET_KEY
        self.algorithm = auth_config.ALGORITHM
        self.access_token_expire_minutes = auth_config.ACCESS_TOKEN_EXPIRE_MINUTES
        self.user_dao = user_dao

    def create_token(self, username: str):
        access_token_expires = timedelta(minutes=self.access_token_expire_minutes)
        access_token = self.__create_access_token(
            data={"username": username}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    async def get_current_user(self, token: str = Depends(oauth2_scheme)):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username: str = payload.get("username")
            if username is None:
                raise credentials_exception
            token_data = TokenData(username=username)
        except JWTError:
            raise credentials_exception
        user = self.user_dao.get(username=token_data.username)
        if user is None:
            raise credentials_exception
        # todo: map user to UserDTO
        return user

    def __create_access_token(self, data: dict, expires_delta: Optional[timedelta] = None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt


class LoginManager(Authenticator):
    """
    Class for managing login operation.
    Allows to:
        - verify and authenticate user
    """

    def __init__(self, auth_config: AuthConfig, user_dao: UserDaoInterface):
        super(LoginManager, self).__init__(auth_config, user_dao)
        self.user_dao = user_dao

    async def login_for_token(self, username: str, password: str):
        user = self.__authenticate_user(username, password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        return super().create_token(user.username)

    def __authenticate_user(self, username: str, password: str):
        user = self.user_dao.get(username)
        if not user:
            return False
        if not verify_password(password, user.token):
            return False
        return user
