from sqlalchemy import Column , String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase
import uuid
from datetime import datetime
from ...domain.entities import UserInDB

Base = DeclarativeBase()

class Base(DeclarativeBase):
    pass

class UserModel (Base):
    __tablename__ ="user"
    id = Column(UUID(as_uuid=True) , primary_key=True , default=uuid.uuid4)
    email = Column(String)
