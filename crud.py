from fastapi import APIRouter, Depends, FastAPI
from sqlmodel import Session

from models import Users as User

from database import get_session

# import models
app = FastAPI
users_router = APIRouter()


@users_router.post("/create_user", status_code=201, response_model=User)
def create_user(user: User, db: Session = Depends(get_session)):
    # hashed_password = user.password + 'hash'
    db.add(user)
    db.commit()
    db.refresh(user)

    return user


# 	with Session(engine) as sessiion:


# 	db.add(user)
# 	db.commit(user)
# 	db.refresh(user)

# 	return user

# # def read_users(db:Session):
# # 	db.
