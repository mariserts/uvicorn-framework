from .base import BaseModel


class SessionSerializer(BaseModel):
    id: str
    user_id: int
