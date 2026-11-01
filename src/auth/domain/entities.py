
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class User(BaseModel):
    email: EmailStr


class UserInDB(User):
    id: UUID




class DayProgress(BaseModel):
    day: int = Field(ge=0)
    completed: bool = False
    total_question: int
    missed_question: int
    completed_at: datetime | None = None



class UserInfo(BaseModel):
    id: UUID
    progress: list[DayProgress] = Field(default_factory=list)

    @field_validator("progress")
    @classmethod
    def unique_days(cls, v: list[DayProgress]) -> list[DayProgress]:
        days = [d.day for d in v]
        if len(days) != len(set(days)):
            raise ValueError("Duplicate day entries in progress")
        return v


class UserInfoInDB(UserInfo):
    model_config = ConfigDict(from_attributes=True)


class UserLogin(UserInDB):
    progress: list[DayProgress] = Field(default_factory=list)
