
from uuid import UUID

from fastapi import APIRouter, Depends, status

from .auth_schemas import (
    RegisterRequest,
    UserOut,
    UserInfoUpdateRequest,
    UserInfoOut,
    LoginRequest,
    LoginResponse
    )
from .dependencies import (
    get_register_use_case,
    get_update_use_case,
    get_login_use_case
)
from ..application.use_cases.register_user import RegisterUser
from ..application.use_cases.update_user_info import UpdateUserInfo
from ..application.use_cases.login import LoginUser
from ..domain.entities import UserInfo , User

router = APIRouter(tags=["auth"], prefix="/auth")


@router.post(
    "/register",
    response_model=UserOut,
    status_code=status.HTTP_201_CREATED,
)
async def register(
    request: RegisterRequest,
    use_case: RegisterUser = Depends(get_register_use_case),
):
    user = await use_case.execute(request.email)
    return UserOut.model_validate(user)



@router.put(
    "/progress/{user_id}",
    response_model=UserInfoOut,
    status_code=status.HTTP_200_OK,
)
async def update_progress(
    user_id: UUID,
    request: UserInfoUpdateRequest,
    use_case: UpdateUserInfo = Depends(get_update_use_case),
):
    user_info = UserInfo(
        id=user_id,
        progress=[
            item.model_dump()
            for item in request.progress
        ],
    )

    saved_info = await use_case.execute(user_info)

    return UserInfoOut.model_validate(
        {
            "id": saved_info.id,
            "progress": [
            item.model_dump()
                for item in saved_info.progress
            ],
        }
    )
from fastapi import APIRouter, Depends, status


@router.post(
    "/login",
    response_model=LoginResponse,
    status_code=status.HTTP_200_OK,
)
async def login(
    request: LoginRequest,
    use_case: LoginUser = Depends(get_login_use_case),
):
    user = User(email=request.email)
    logged_in_user = await use_case.execute(user)

    return LoginResponse.model_validate(logged_in_user)
