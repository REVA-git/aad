from core.schemas import SignupRequest, UserResponse
from core import repository


def signup(request: SignupRequest):
    return repository.create_user(request)


def get_users() -> list[UserResponse]:
    return repository.get_users()
