from fastapi import APIRouter , Depends , status
from .auth_schemas import RegisterRequest , UserOut
from .dependencies import get_register_use_case
from ..application.use_cases.register_user import RegisterUser

router = APIRouter(tags=['auth'], prefix='/auth')

@router.post("/register", response_model=UserOut)
async def register(
    request: RegisterRequest,
    use_case: RegisterUser = Depends(get_register_use_case)
):
    user = await use_case.execute(request.email, request.password)
    return UserOut.model_validate(user)
