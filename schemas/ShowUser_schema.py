from pydantic import BaseModel

class ShowUser(BaseModel):
    username: str
    name: str
    email: str
    class Config():
        orm_mode = True
