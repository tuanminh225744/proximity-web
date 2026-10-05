from app.schemas.base import BaseSchema
from pydantic import Field, EmailStr
from typing import Optional

class CreateUserRequest(BaseSchema):
    email: EmailStr = Field(..., description="The email address of the user")   
    name: str = Field(..., min_length=2, max_length=100, description="The name of the user")
    age: Optional[int] = Field(None, ge=0, description="The age of the user")