from app.schemas.base import BaseSchema
from typing import Optional

class UserResponse(BaseSchema):
    id: int
    email: str
    name: str
    age: Optional[int] = None