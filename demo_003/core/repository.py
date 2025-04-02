from core.schemas import SignupRequest, UserResponse


users = []


def create_user(request: SignupRequest):
    users.append(request)
    return request


def get_users() -> list[UserResponse]:
    return users
