import time
import uuid

import uvicorn
from fastapi import Depends, FastAPI

from project.db.challenge import ChallengeDao
from project.db.user import UserDao
from project.model import User, Token, Login, RegistrationUserDTO, UserDTO, Challenge, ChallengeDTO
from project.server.auth import LoginManager, create_password_hash

user_dao = UserDao()
challenge_dao = ChallengeDao()
loginManager = LoginManager(user_dao)
app = FastAPI()


#################
#     AUTH      #
#################

@app.post("/login", response_model=Token)
async def login(login_data: Login):
    return loginManager.login_for_token(login_data.username, login_data.password)


@app.post("/registration", response_model=Token)
async def registration(user: RegistrationUserDTO):
    user_dao.save(User(username=user.username, name=user.name, email=user.email, age=user.age,
                       token=create_password_hash(user.password)))
    return loginManager.create_token(user.username)


#################
#     USER      #
#################

@app.get("/user/me", response_model=UserDTO)
async def get_user_me(current_user: User = Depends(loginManager.get_current_user)):
    dto = UserDTO(username=current_user.username, name=current_user.name, email=current_user.email,
                  age=current_user.age)
    print(f"Return profile for user '{current_user.username}'")
    return dto


######################
#     CHALLENGE      #
######################

@app.post("/challenge", response_model=Challenge)
async def create_challenge(req: ChallengeDTO, current_user: User = Depends(loginManager.get_current_user)):
    challenge = Challenge(id=str(uuid.uuid4()), name=req.name, description=req.description, active_from=req.active_from,
                          active_until=req.active_until, frequency=req.frequency, price=req.price,
                          creator=current_user.username,
                          created=time.time())
    print(f"Created challenge: {challenge}")
    return challenge_dao.save(challenge)


@app.get("/challenge/{id}", response_model=Challenge)
async def get_challenge(id: str, current_user: User = Depends(loginManager.get_current_user)):
    challenge = challenge_dao.get(id)
    return challenge


if __name__ == '__main__':
    uvicorn.run(app, port=8080, host='0.0.0.0')
