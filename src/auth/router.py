from fastapi import APIRouter, Request
from src.auth import service
from src.auth.schema import Register
from src.database import db
from src.auth.service import services

auth_router = APIRouter(tags=["Auth"])





#Register user endpoint
@auth_router.post("/register",summary="registration endpoint")
def register(register_info:Register,db:db):
    """Register user via valid username and valid phone number"""
    result = services.register_Service(register_info.model_dump(),db)