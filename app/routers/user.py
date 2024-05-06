from fastapi import APIRouter, Depends
from app.db.database import get_db
from sqlalchemy.orm import Session
from schemas.User_schema import User
from schemas.ShowUser_schema import ShowUser
from schemas.UpdateUser_schema import UpdateUser
from app.repository import user
from typing import Union

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)
users = []
#endpoint to get all users
@router.get("/")
def get_user(db:Session = Depends(get_db)):
    res = user.get_all_users(db)
    return res

#endpoint to create user
@router.post("/")
def create_user(user_one: User, db:Session = Depends(get_db)):
    user.create_user(user_one, db)
    return {"Response":"User created satisfactorily"}

#endpoint to get user by id with path parameter
@router.post("/{user_id}", response_model=Union[ShowUser, dict])
def get_user_by_id_with_path(user_id: int, db:Session = Depends(get_db)):
    user_one = user.get_user(user_id, db)
    return user_one

#endpoint to delete user by id with path parameter
@router.delete("/{user_id}")
def delete_user(user_id: int, db:Session = Depends(get_db)):
    res = user.delete_user(user_id, db)
    return res

#endpoint to update user by id with path parameter
@router.patch("/{user_id}")
def update_user(user_id: int, updateUser: UpdateUser, db:Session = Depends(get_db)):
    res = user.update_user(user_id, updateUser, db)
    return res
    