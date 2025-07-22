from typing import Annotated
from fastapi import APIRouter, Depends
from src.auth.schema import User
from src.user.schemas import  RegisterToken, UsernameSchema
from src.database import db
from src.user.service import services

user_router = APIRouter(tags=["User"])



#Get username using token
@user_router.post("/username",summary="Get username using token",response_model=UsernameSchema)
def user_info(db:db,register_token:RegisterToken):
    user = services.get_username_Service(register_token.model_dump(),db)
    if user:
        return UsernameSchema(
            username=user.data[0]["username"],
            config_count=f"You have {3-int(user.data[0]["config_count"])} more credits"
        )

# @user_router.post("/create",summary="Create new config to the user")
# def createConfig(config:ConfigCreate,user:Annotated[User,Depends(services.get_current_user)],db:db):
#     services.create_config_service(userinfo=config)