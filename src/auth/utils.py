from datetime import timedelta
from datetime import datetime
import random
import jwt
import requests
from src.setting import setting


JWT_SECRET_KEY = setting.JWT_SECRET_KEY 
JWT_ALGORITHM =  setting.JWT_ALGORITHM

#Genarate register token
def genarate_register_token():
    """for genarate register token for every user"""
    return str(random.randint(10_000_000, 99_999_999))


#SEND TOKEN TO THE USER
def send_register_token(token, phone_number):
    print(phone_number.lstrip("+"))
    url = "https://app.text.lk/api/v3/sms/send"

    headers = {
        "Authorization": "Bearer 959|EEvDeFe6Ysac62kqIvCWlT2owSqxq06ms1g8z9MJ1918a24b",
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    data = {
        "recipient": phone_number.lstrip("+"),
        "sender_id": "TextLKDemo",
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