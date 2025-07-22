from pydantic import BaseModel

class ConfigCreate(BaseModel):
    token:str
    package:str

class RegisterToken(BaseModel):
    token:str

class UsernameSchema(BaseModel):
    username:str
    config_count:str