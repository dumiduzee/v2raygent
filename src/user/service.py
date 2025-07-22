


from src.user.Exceptions import GetUsernameExceptions
from src.user.repo import Crud


class Service():
    """BAse service class for user"""
    def __init__(self):
        self.crud = Crud()

    #get username and credit limits service
    def get_username_Service(self,token,db):
        # pass the token to the crud layer
        username = self.crud.get_username(token=token["token"],db=db)
        if username.count is None:
            raise GetUsernameExceptions(detail="User cannot find")
        print(username)



services = Service()