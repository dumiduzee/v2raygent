from fastapi import HTTPException,status


class AuthExceptions(HTTPException):
    """Base exception class for auth related exceptions"""
    pass

class InvalidNumberException(AuthExceptions):
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid phone number"):
        super().__init__(status_code, detail)

