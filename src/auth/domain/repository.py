from abc import ABC , abstractmethod
from uuid import UUID
from .entities import User , UserInDB , UserInfo , UserInfoInDB

class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user:User) ->UserInDB:
        ...

    @abstractmethod
    async def login_user(self, user:User) -> UserInDB:
        ...

class IUserInfoRepository(ABC):
    @abstractmethod
    async def update_user_info(self, user_info:UserInfo) ->UserInfoInDB:
        ...



