from fastapi import APIRouter
from core.schemas import SignupRequest, UserResponse
from core import service

router = APIRouter(tags=["auth"], prefix="/auth")


@router.post("/signup")
async def signup(request: SignupRequest) -> UserResponse:
    return service.signup(request)


@router.get("/users")
async def get_users() -> list[UserResponse]:
    return service.get_users()
