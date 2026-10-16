from ...domain.entities import UserInfo, UserInfoInDB
from ...domain.repository import IUserInfoRepository


class UpdateUserInfo:
    def __init__(self, repo: IUserInfoRepository):
        self.repo = repo

    async def execute(
        self, user_info: UserInfo
    ) -> UserInfoInDB:
        return await self.repo.update_user_info(user_info)
