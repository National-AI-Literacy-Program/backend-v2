from ..infrastructure.repositories.sqlalchemy_user_repo import SQLAlchemyUserRepository
from ..application.use_cases.register_user import RegisterUser
from sqlalchemy.ext.asyncio import AsyncSession
from ..infrastructure.database import get_db
from fastapi import Depends

async def get_register_use_case(session:AsyncSession = Depends(get_db)):
    repo =SQLAlchemyUserRepository(session = session)
    return RegisterUser(repo=repo )
