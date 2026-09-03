from ...domain.repository import IUserRepository
from ...domain.entities import User

class RegisterUser:
    def __init__(self , repo :IUserRepository):
        self.repo = repo

    async def execute(self, email:str):
        user = User(email=email )
        saved_user = await self.repo.create_user(user)
        return saved_user
