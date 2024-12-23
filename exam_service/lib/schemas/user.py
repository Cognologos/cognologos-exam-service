from datetime import datetime

from .abc import BaseSchema


class UserSchema(BaseSchema):
    username: str
    email: str
    id: int
    hashed_password: str
    is_active: bool
    created_at: datetime
