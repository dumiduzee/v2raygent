from fastapi import APIRouter,status
from src.auth.schema import Register, RegisterResponse
from src.database import db
from src.auth.service import services




auth_router = APIRouter(tags=["Auth"])





#Register user endpoint
@auth_router.post("/register",summary="registration endpoint",response_model=RegisterResponse,status_code=status.HTTP_201_CREATED)
def register(register_info:Register,db:db):
    """Register user via valid username and valid phone number"""
    result = services.register_Service(register_info.model_dump(),db)
    if result:
        return RegisterResponse()