from sqlalchemy.orm import Session
from app.db import models
from schemas.UpdateUser_schema import UpdateUser


def create_user(user_one, db:Session):
    user_dict = user_one.model_dump()
    new_user = models.User(
        username = user_dict["username"],
        password = user_dict["password"],
        name = user_dict["name"],
        last_name = user_dict["last_name"],
        address = user_dict["address"],
        phone = user_dict["phone"],
        email = user_dict["email"],
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

def get_user(user_id, db:Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
            return {"Response":"User not found"}
    return user
    
def delete_user(user_id, db:Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"Response":"User not found"}
    user.delete(synchronize_session=False)
    db.commit()
    return {"Response": "User deleted satisfactorily"}

def get_all_users(db:Session):
    data = db.query(models.User).all()
    return data

def update_user(user_id, updateUser: UpdateUser, db:Session):
    user = db.query(models.User).filter(models.User.id == user_id)
    if not user.first():
        return {"Response":"User not found"}
    user.update(updateUser.model_dump(exclude_unset=True))
    db.commit()
    return {"Response": "User updated satisfactorily"}