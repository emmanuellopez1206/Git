from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class User (BaseModel):
    username: str
    password: str
    name: str
    last_name: str
    address: Optional[str]
    phone: int
    email: str
    user_creation: datetime = datetime.now()

