from ..infrastructure.repositories.mongo_user_repo import MongoUserRepository
from ..application.use_cases.register_user import RegisterUser

async def get_register_use_case():
    repo = MongoUserRepository()
    return RegisterUser(repo=repo)
