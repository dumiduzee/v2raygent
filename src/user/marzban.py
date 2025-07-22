
from time import timezone
from yaml import Token
from src.setting import setting
import requests
from datetime import datetime,timedelta
from uuid import uuid4
from fastapi import status

from src.user.Exceptions import CreateConfigExceptions

MARZBAN_API_URL = setting.MARZBAN_API_URL
MARZBAN_USERNAME = setting.MARZBAN_USERNAME
MARZBAN_PASSWORD = setting.MARZBAN_PASSWORD
TOKEN = None

def login_to_marzban():
    """login tom the marzban pannel and save the token"""
    global TOKEN
    try:
        pass
        url_login = f"{MARZBAN_API_URL}api/admin/token"
        print(url_login)
        response = requests.post(url=url_login,data={
            "username":MARZBAN_USERNAME,
            "password":MARZBAN_PASSWORD
        })
        result = response.json()
        TOKEN =  result.get("access_token")
    except Exception as e:
        print(e)



def genarate_uuid():
    return str(uuid4())




def create_config_marzban(package,token):
    """create user in marzban pannel"""
    try:
        if TOKEN is None:
            login_to_marzban()
        id = genarate_uuid()
        expire_time = datetime.now() + timedelta(days=30)
        expires_in =  int(expire_time.timestamp())

        body = {
            "data_limit": 107374182400,
            "data_limit_reset_strategy": "no_reset",
            "expire": expires_in,
            "inbounds": {
                "vless": [
                f"{package}"
                ]
                
            },
            "next_plan": {
                "add_remaining_traffic": False,
                "data_limit": 0,
                "expire": 30,
                "fire_on_either": True
            },
            "note": f"{token}",
            "on_hold_expire_duration": 0,
            "on_hold_timeout": "2023-11-03T20:30:00",
            "proxies": {
                "vless": {
            "id": f"{id}"}
                
            },
            "status": "active",
            "username": f"{id}"
        }

        headers = {
            "Authorization": f"Bearer {TOKEN}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        url = f"{MARZBAN_API_URL}api/user"

        response = requests.post(url=url,headers=headers,json=body)
        result = response.json()
        config = result.get("links")[0]
        subscription_url:str = result.get("subscription_url").split("/sub/")[1]
        return {
            "config":config,
            "subscription_url":subscription_url
            }
    except Exception as e:
        print(e)
        raise CreateConfigExceptions(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail="Something went wrong went creating config")


    

    