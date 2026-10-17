
from ...domain.entities import User, UserInDB, UserInfo, UserInfoInDB
from ...domain.repository import IUserRepository, IUserInfoRepository
from ...infrastructure.orm.models import UserModel, UserInfoModel


class MongoUserRepository(IUserRepository):
    async def create_user(self, user: User) -> UserInDB:
        db_user = UserModel(email=user.email)
        await db_user.insert()

        db_user_info = UserInfoModel(
            id=db_user.id,
            progress=[],
        )
        await db_user_info.insert()

        return UserInDB(
            id=db_user.id,
            email=db_user.email,
        )

    async def login_user(self, user: User) -> UserInDB:
        db_user = await UserModel.find_one(
            UserModel.email == user.email
        )

        if db_user is None:
            return await self.create_user(user)

        return UserInDB(
            id=db_user.id,
            email=db_user.email,
        )


class MongoUserInfoRepository(IUserInfoRepository):
    async def update_user_info(
        self, user_info: UserInfo
    ) -> UserInfoInDB:
        db_user_info = await UserInfoModel.find_one(
            UserInfoModel.id == user_info.id
        )

        if db_user_info is None:
            raise ValueError(
                f"Progress record not found for user {user_info.id}"
            )

        db_user_info.progress = user_info.progress
        await db_user_info.save()

        return UserInfoInDB(
            id=db_user_info.id,
            progress=[
                item.model_dump()
                for item in db_user_info.progress
            ],
        )

