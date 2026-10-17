
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field, field_validator


class User(BaseModel):
    email: EmailStr


class UserInDB(User):
    id: UUID

class UserLogin(User):
    pass


class MCQResult(BaseModel):
    qn: int = Field(ge=0)
    correct: bool


class DayProgress(BaseModel):
    day: int = Field(ge=0)
    completed: bool = False
    mcq: list[MCQResult] = Field(default_factory=list)
    completed_at: datetime | None = None

    @field_validator("mcq")
    @classmethod
    def unique_questions(cls, v: list[MCQResult]) -> list[MCQResult]:
        qns = [m.qn for m in v]
        if len(qns) != len(set(qns)):
            raise ValueError("Duplicate question numbers in a day")
        return v


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
