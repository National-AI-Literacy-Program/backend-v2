from ..infrastructure.repositories.mongo_user_repo import MongoUserRepository , MongoUserInfoRepository
from ..application.use_cases.register_user import RegisterUser
from ..application.use_cases.update_user_info import UpdateUserInfo

async def get_register_use_case():
    repo = MongoUserRepository()
    return RegisterUser(repo=repo)

async def get_update_use_case():
    repo = MongoUserInfoRepository()
    return UpdateUserInfo(repo=repo)
