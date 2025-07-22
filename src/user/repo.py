from supabase import Client


class Crud():

    def get_username(self,token,db:Client):
        return db.table("users").select("*").eq("token",token).execute()
    
    def insert_config(self,config,db:Client):
        return db.table("configs").insert({
            "inbound":config["inbound"],
            "config":config["config"],
            "subscription":config["subscription_url"],
            "userid":config["userid"]
        }).execute()
    
    def increment_config_count(self,user_id,count,db:Client):
        return db.table("users").update({"config_count":count}).eq("id",user_id).execute()
    