from pydantic import BaseModel


class SignupRequest(BaseModel):
    username: str
    name: str
    email: str
    password: str


class UserResponse(BaseModel):
    username: str
    name: str
    email: str
