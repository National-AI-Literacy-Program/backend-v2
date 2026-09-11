from beanie import Document
from pydantic import Field
import uuid


class UserModel(Document):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)
    email: str

    class Settings:
        name = "user"  # collection name
