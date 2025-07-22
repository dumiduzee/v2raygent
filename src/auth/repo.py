from supabase import Client



class Crud():
    """Base class for all the database related tasks"""

    def isUserExistByUsername(self,username,db:Client):
        return db.table("users").select("*").eq("username",username).maybe_single().execute()

    def isUserExsitsByNumber(self,number,db):
        return db.table("users").select("*").eq("phone_number",number).maybe_single().execute()
