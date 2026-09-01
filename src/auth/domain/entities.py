from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID

class User(BaseModel):
    email:EmailStr

class UserInDB(User):
    id:UUID
