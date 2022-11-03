from .base import BaseModel


class UserSerializer(BaseModel):
    id: int
    email: str
    password: str
    is_superuser: bool
