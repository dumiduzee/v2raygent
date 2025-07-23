from src.user.Exceptions import CreateConfigExceptions, GetUsernameExceptions
from src.user.repo import Crud
from src.user.marzban import create_config_marzban
from fastapi import status
from src.user.utils import send_config


class Service():
    """Base service class for user"""
    def __init__(self):
        self.crud = Crud()

    #get username and credit limits service
    def get_username_Service(self,token,db):
        # pass the token to the crud layer
        user = self.crud.get_username(token=token["token"],db=db)
        
        if user.data is None:
            raise GetUsernameExceptions(detail="User cannot find")
        return user
    
    def create_config_service(self,config_info,db):
        #first check is user really exists withing the database
        user = self.crud.get_username(config_info.token,db=db)
        if len(user.data) == 0:
            raise CreateConfigExceptions(detail="User not found")
        
        #check user config count
        if user.data[0]["config_count"] == 3:
            raise CreateConfigExceptions(detail="Credit limit reached")
        
        #create the config with unique id
        data = create_config_marzban(config_info.package,token=config_info.token)
        
        if data is None:
            raise CreateConfigExceptions(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong on our side")
        #save the config and subscription url to the config table
        db_save_data = data.copy()
        db_save_data["inbound"] = config_info.package
        db_save_data["userid"] = user.data[0]["id"]
        result = self.crud.insert_config(config=db_save_data,db=db)
        if result is None:
            raise CreateConfigExceptions(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong on our side")
        #increment the count
        config_count = int(user.data[0]["config_count"]) + 1
        result = self.crud.increment_config_count(user_id=user.data[0]["id"],count=config_count,db=db)
        #send created config to the user
        result_config_send = send_config(config=data["config"],phone_number=user.data[0]["phone_number"])
        if result is None:
            raise CreateConfigExceptions(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong on our side")
        return 3 - config_count



services = Service()