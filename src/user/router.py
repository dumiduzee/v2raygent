from typing import Annotated
from fastapi import APIRouter, Depends
from src.auth.schema import User
from src.user.schemas import  RegisterToken
from src.database import db
from src.user.service import services

user_router = APIRouter(tags=["User"])



#Get username using token
@user_router.post("/username",summary="Get username using token")
def user_info(db:db,register_token:RegisterToken):
    services.get_username_Service(register_token.model_dump(),db)


# @user_router.post("/create",summary="Create new config to the user")
# def createConfig(config:ConfigCreate,user:Annotated[User,Depends(services.get_current_user)],db:db):
#     services.create_config_service(userinfo=config)