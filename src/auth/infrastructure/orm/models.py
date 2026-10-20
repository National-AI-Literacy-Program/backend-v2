
from datetime import datetime
from uuid import UUID, uuid4

from beanie import Document
from pydantic import BaseModel, Field, field_validator, EmailStr

from pymongo import ASCENDING, IndexModel




class DayProgress(BaseModel):
    day: int = Field(ge=0)
    completed: bool = False
    total_question: int
    missed_question: int
    completed_at: datetime | None = None


class UserModel(Document):
    id: UUID = Field(default_factory=uuid4)
    email: EmailStr

    class Settings:
        name = "user"
        indexes = [
            IndexModel(
                [("email", ASCENDING)],
                unique=True,
            ),
        ]

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
