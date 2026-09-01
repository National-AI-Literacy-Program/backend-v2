from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, delete, update
from ...domain.entities import User , UserInDB
from ...domain.repository import IUserRepository
from ..orm.models import UserModel
from uuid import UUID

class SQLAlchemyUserRepository(IUserRepository):
    def __init__(self , session:AsyncSession):
        self.session = session

    async def create_user(self, user:User) ->UserInDB:
        db_user = UserModel(
            email = user.email,
        )
        self.session.add(User)
        await self.session.commit()
        await self.session.refresh(db_user)
        return UserInDB(
            id  = db_user.id ,
            email=db_user.email
        )
