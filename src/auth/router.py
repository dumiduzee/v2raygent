from typing import Annotated
from fastapi import APIRouter, Depends,status
from fastapi.security import OAuth2PasswordRequestForm
from src.auth.schema import LoginSchema, Register, RegisterResponse, Token
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
    

#Login user endpoint
@auth_router.post("/login",summary="loginin endpoint",status_code=status.HTTP_200_OK,response_model=Token)
def login(db:db,form_data:Annotated[OAuth2PasswordRequestForm,Depends()]):
    token = services.login_service(username=form_data.username,token=form_data.password,db=db)
    return Token(
        token=token,
        token_type="bearer"
    )