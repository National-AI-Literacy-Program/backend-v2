from abc import ABC , abstractmethod
from uuid import UUID
from .entities import User , UserInDB

class IUserRepository(ABC):
    @abstractmethod
    async def create_user(self, user:User) ->UserInDB:
        ...


    






