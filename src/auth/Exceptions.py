from fastapi import HTTPException,status


class AuthExceptions(HTTPException):
    """Base exception class for auth related exceptions"""
    pass

class InvalidNumberException(AuthExceptions):
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid phone number"):
        super().__init__(status_code, detail)

class UsernameExsistsException(AuthExceptions):
    """Raise when username already esists in the database"""
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = "This username already exists in the system"):
        super().__init__(status_code, detail)

class PhoneNumberExsistsException(AuthExceptions):
    """Raise when  phone number already exists in the database"""
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = "This phone number already exists in the system"):
        super().__init__(status_code, detail)
