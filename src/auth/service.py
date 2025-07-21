

#User registration service layer
from src.auth.Exceptions import PhoneNumberExsistsException, UsernameExsistsException
from src.auth.repo import Crud


class Service():
    """Base class for registraion related functions"""
    def __init__(self):
        """initialize crud repo"""
        self.crud = Crud()
    async def register_Service(self,user,db):
        """
        handle user registration
        check that username or phone number already exists
        create a record for the user
        genarate access token (8 digits) 
        send 8 digit code as sms
        """
        #check username existance
        isExsists = await self.crud.isUserExistByUsername(user["username"],db)
        if isExsists:
            raise UsernameExsistsException()
        # #check phone number exsistance
        isExsists = await self.crud.isUserExsitsByNumber(user["phone_number"],db)
        if isExsists:
            raise PhoneNumberExsistsException()
        

services = Service()
    
