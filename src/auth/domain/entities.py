from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class User(BaseModel):
    id : UUID
    fullname:str
    email:EmailStr
    age:Optional[int] = None
    address:Optional[str] = None

class UserInDB(User):
    id:UUID
