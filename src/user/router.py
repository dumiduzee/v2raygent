from typing import Annotated
from fastapi import APIRouter, Depends,status
from src.auth.schema import User
from src.user.Exceptions import CreateConfigExceptions
from src.user.schemas import  ConfigCreate, ConfigCreateResponse, RegisterToken, UsernameSchema
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
            config_count=f"You have {3-int(user.data[0]['config_count'])} more credits"
        )
    

#Create new config to the user
@user_router.post("/create",summary="Create new config to the user",response_model=ConfigCreateResponse)
def createConfig(config:ConfigCreate,db:db):
    result = services.create_config_service(config_info=config,db=db)
    if result is None:
        raise CreateConfigExceptions(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong on our side")
    return ConfigCreateResponse(
        remainiting_credits= result
    )