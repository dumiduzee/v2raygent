from pydantic import BaseModel

class ConfigCreate(BaseModel):
    token:str
    package:str

class RegisterToken(BaseModel):
    token:str