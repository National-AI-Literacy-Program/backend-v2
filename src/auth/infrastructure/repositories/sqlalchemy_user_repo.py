from sqlalchemy.ext.asyncio import AsyncSession
from ...domain.entities import User, UserInDB
from ...domain.repository import IUserRepository
from ...infrastructure.orm.models import UserModel

class SQLAlchemyUserRepository(IUserRepository):
    def __int__(self , session:AsyncSession):
        self.session = session

    async def create_user(self, user:User) ->UserInDB:
        db_user = UserModel(
            email = user.email
        )
        self.session.add(db_user)
        await self.session.commit()
        return UserInDB(
            id = db_user.id,
            email= db_user.email
        )
