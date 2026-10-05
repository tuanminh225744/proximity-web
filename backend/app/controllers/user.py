from fastapi import APIRouter, Depends, HTTPException, status

from app.schemas.user.request import CreateUserRequest
from app.schemas.user.response import UserResponse

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user: CreateUserRequest):
    # Implementation for creating a new user
    
