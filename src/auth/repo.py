

class Crud():
    """Base class for all the database related tasks"""
    async def isUserExistByUsername(self,username,db):
        print(username,db)
        return True

    async def isUserExsitsByNumber(self,number,db):
        pass