from datetime import timedelta
from datetime import datetime
import random
import jwt
import requests
from src.setting import setting
from src.auth.utils import TEXT_LK_API_KEY, TEXT_LK_SENDER_ID


JWT_SECRET_KEY = setting.JWT_SECRET_KEY 
JWT_ALGORITHM =  setting.JWT_ALGORITHM
TEXT_LK_API_KEY = setting.TEXT_LK_API_KEY
TEXT_LK_SENDER_ID = setting.TEXT_LK_SENDER_ID

#Genarate register token
def genarate_register_token():
    """for genarate register token for every user"""
    return str(random.randint(10_000_000, 99_999_999))


#SEND TOKEN TO THE USER
def send_register_token(token, phone_number):
    print(phone_number.lstrip("+"))
    url = "https://app.text.lk/api/v3/sms/send"

    headers = {
        "Authorization": f"Bearer {TEXT_LK_API_KEY}",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    data = {
        "recipient": phone_number.lstrip("+"),
        "sender_id": f"{TEXT_LK_SENDER_ID}",
        "type": "plain",
        "message": f"Your registration code is: {token}. please save this code somewhere. this code required for request configs."
    }

    response = requests.post(url, headers=headers, json=data)
    

    try:
        print(response.json())
        return True
    except Exception as e:
        print("Failed to parse response:", e)
        print("Raw response:", response.text)


#create jwt access token
def create_access_token(data:dict,expires_delta:timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta
    else:
        expire = datetime.now() + timedelta(minutes=10)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode,JWT_SECRET_KEY,algorithm=JWT_ALGORITHM)
    return encoded_jwt