from pydantic import BaseModel, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber
import phonenumbers

from src.auth.Exceptions import InvalidNumberException

class Register(BaseModel):
    username: str
    phone_number: PhoneNumber

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
