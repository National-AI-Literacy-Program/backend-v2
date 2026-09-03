from pydantic import BaseModel , EmailStr
from uuid import UUID

class RegisterRequest(BaseModel):
    email:EmailStr

class UserOut(BaseModel):
    id:UUID
    email:EmailStr

    model_config = {"from_attributes": True}
