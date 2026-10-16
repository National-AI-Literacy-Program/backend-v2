
from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document
from pydantic import BaseModel, Field, field_validator


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


class UserModel(Document):
    id: UUID = Field(default_factory=uuid4)
    email: str

    class Settings:
        name = "user"


class UserInfoModel(Document):
    id: UUID
    progress: list[DayProgress] = Field(default_factory=list)

    @field_validator("progress")
    @classmethod
    def unique_days(cls, v: list[DayProgress]) -> list[DayProgress]:
        days = [d.day for d in v]
        if len(days) != len(set(days)):
            raise ValueError("Duplicate day entries in progress")
        return v

    class Settings:
        name = "user_info"
