from pydantic import BaseModel, Field

class ConfigCreate(BaseModel):
    token:str=Field(examples=["token"])
    package:str=Field(examples=["Dialog 724"])

class RegisterToken(BaseModel):
    token:str

class UsernameSchema(BaseModel):
    username:str
    config_count:str

class ConfigCreateResponse(BaseModel):
    succuss:bool=Field(default=True)
    message:str=Field(default="Config created succuss")
    remainiting_credits:int