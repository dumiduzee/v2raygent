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

class RegisterFailExsistsException(AuthExceptions):
    """Raise when  registration fail due to some situation"""
    def __init__(self, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail = "Something went wrong in our side"):
        super().__init__(status_code, detail)

class LoginTokenInvalidException(AuthExceptions):
    """Raise when token dosen't meets his requirements"""
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid token"):
        super().__init__(status_code, detail)

class UsernameNotValidException(AuthExceptions):
    """Raise when username not in database"""
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid username! please check your username again"):
        super().__init__(status_code, detail)

class TokenNotValidException(AuthExceptions):
    """Raise when token not in database"""
    def __init__(self, status_code=status.HTTP_400_BAD_REQUEST, detail = "Invalid token! please check your token again"):
        super().__init__(status_code, detail)