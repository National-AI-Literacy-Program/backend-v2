from ...domain.entities import User
from ...domain.repository import IUserRepository


class LoginUser:
    def __init__(self, user_repository: IUserRepository):
        self.user_repository = user_repository

    async def execute(self, user: User):
        return await self.user_repository.login_user(user)
