from typing import Annotated
from fastapi import Depends
from supabase import Client,create_client
from src.setting import setting

url = setting.SUPABASE_URL
key = setting.SUPABASE_KEY

#Initiating supabase client
client : Client = create_client(url,key)

#getter function for supabase client
def getClient() -> Client :
    return client

#dpi
db = Annotated[Client,Depends(getClient)]




 