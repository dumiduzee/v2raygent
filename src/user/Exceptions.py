from fastapi import HTTPException,status


class UserExceptions(HTTPException):
    """Base exception class for auth related exceptions"""
    pass

class GetUsernameExceptions(UserExceptions):
    """Raise when something happened on get username services"""
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = ""):
        super().__init__(status_code, detail)

