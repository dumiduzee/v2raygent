from supabase import Client


class Crud():

    def get_username(self,token,db:Client):
        return db.table("users").select("username").eq("token",token).execute()
