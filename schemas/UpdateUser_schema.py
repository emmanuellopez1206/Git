from pydantic import BaseModel
from typing import Union

class UpdateUser (BaseModel):
    username: str = None
    password: str = None
    name: str = None
    last_name: str = None
    address: str = None
    phone: int = None
    email: str = None

