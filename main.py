from fastapi import Depends, FastAPI

from project.db.user import MockDB
from project.model import User, UserDTOFull, Token, Login
from project.server.auth import LoginManager, create_password_hash

user_dao = MockDB()
loginManager = LoginManager(user_dao)
app = FastAPI()


@app.post("/login", response_model=Token)
async def login(login_data: Login):
    return loginManager.login_for_token(login_data.username, login_data.password)


@app.post("/registration/", response_model=Token)
async def create_item(user: UserDTOFull):
    user_dao.save(User(username=user.username, name=user.name, email=user.email, age=user.age,
                       token=create_password_hash(user.password)))
    token = loginManager.login_for_token(user.username, user.password)
    return token


@app.get("/user/me", response_model=User)
async def get_user_me(current_user: User = Depends(loginManager.get_current_user)):
    return current_user
