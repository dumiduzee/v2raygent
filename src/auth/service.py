

#User registration service layer
from src.auth.Exceptions import PhoneNumberExsistsException, RegisterFailExsistsException, UsernameExsistsException
from src.auth.repo import Crud
from src.auth.utils import genarate_register_token, send_register_token


class Service():
    """Base class for registraion related functions"""
    def __init__(self):
        """initialize crud repo"""
        self.crud = Crud()
    def register_Service(self,user,db):
        """
        handle user registration
        check that username or phone number already exists
        create a record for the user
        genarate access token (8 digits) 
        send 8 digit code as sms
        """
        #check username existance
        isExsists = self.crud.isUserExistByUsername(user["username"],db)
        if isExsists:
            raise UsernameExsistsException()
        # #check phone number exsistance
        isExsists = self.crud.isUserExsitsByNumber(user["phone_number"].replace("tel:", "").replace("-", ""),db)
        if isExsists:
            raise PhoneNumberExsistsException()
        #check token 
        while True:
            token  = genarate_register_token()
            exsts = self.crud.isTokenExists(token=token,db=db)
            if exsts:
                continue
            break
        
        #register the user with newly created token
        user["phone_number"] = user["phone_number"].replace("tel:", "").replace("-", "")
        user["token"] = token
        inserted_user = self.crud.insertUser(user=user,db=db)
        if inserted_user:
            #send registration token to the phone number
            #return the user dsata to the handler
            if send_register_token(token=token,phone_number=user["phone_number"].replace("tel:", "").replace("-", "")):
                return inserted_user
            else:
                raise RegisterFailExsistsException()
        else:
            raise RegisterFailExsistsException()

        

services = Service()
    
