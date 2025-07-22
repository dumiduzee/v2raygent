from fastapi import File
from pydantic import BaseModel, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
import phonenumbers

from src.auth.Exceptions import InvalidNumberException, LoginTokenInvalidException

class Register(BaseModel):
    username: str
    phone_number: PhoneNumber = Field(examples=["0767722791","+94767722791"])

    @field_validator('phone_number', mode='before')
    @classmethod
    def normalize_and_validate_phone(cls, v: str) -> str:
        try:
            parsed = phonenumbers.parse(v, "LK")
        except phonenumbers.NumberParseException:
            raise InvalidNumberException(detail="Invalid phone number format")

        if not phonenumbers.is_valid_number(parsed):
            raise InvalidNumberException(detail="Invalid phone number")


        if phonenumbers.region_code_for_number(parsed) != "LK":
            raise InvalidNumberException(detail="Phone number must be a Sri Lankan number (+94)")

        
        return phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)

class RegisterResponse(BaseModel):
    """Model schema for the returning register response"""
    succuss:bool=Field(default=True)
    message:str=Field(default="Account created succuss!!")

#schema for login
class LoginSchema(BaseModel):
    """
    Schema for the login endpoint
    required valid token recived from registration
    required valid username
    """
    username:str=Field(...,min_length=5,examples=["Valid username required"])
    token:str=Field(...,min_length=8,examples=["12345678"])

    @field_validator("token",mode="before")
    #token exactly have 8 digits
    @classmethod
    def token_validator(cls,v:str):
        if len(v) != 8:
            raise LoginTokenInvalidException()
        return v
    
    @field_validator("username",mode="before")
    #check username is provided or not
    @classmethod
    def username_validator(cls,v:str):
        if len(v)  == 0 or v is None:
            raise LoginTokenInvalidException(detail="Username required")
        return v