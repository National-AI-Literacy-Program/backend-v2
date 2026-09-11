from ...domain.entities import User, UserInDB
from ...domain.repository import IUserRepository
from ...infrastructure.orm.models import UserModel


class MongoUserRepository(IUserRepository):
    async def create_user(self, user: User) -> UserInDB:
        db_user = UserModel(email=user.email)
        await db_user.insert()
        return UserInDB(
            id=db_user.id,
            email=db_user.email,
        )
