
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


# ---------- Registration ----------

class RegisterRequest(BaseModel):
    email: EmailStr


class UserOut(BaseModel):
    id: UUID
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


# ---------- Login ----------

class LoginRequest(BaseModel):
    email: EmailStr


class LoginResponse(BaseModel):
    id: UUID
    email: EmailStr
    progress: list["DayProgressSchema"] = Field(
        default_factory=list
    )

    model_config = ConfigDict(from_attributes=True)


# ---------- Progress data ----------

class DayProgressSchema(BaseModel):
    day: int = Field(ge=1)
    completed: bool = False
    total_question: int
    missed_question: int
    completed_at: datetime | None = None


# ---------- Progress update request ----------

class UserInfoUpdateRequest(BaseModel):
    progress: list[DayProgressSchema] = Field(
        default_factory=list
    )


# ---------- Progress response ----------

class UserInfoOut(BaseModel):
    id: UUID
    progress: list[DayProgressSchema] = Field(
        default_factory=list
    )

    model_config = ConfigDict(from_attributes=True)
