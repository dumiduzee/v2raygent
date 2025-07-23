from src.setting import setting
import requests

TEXT_LK_API_KEY = setting.TEXT_LK_API_KEY
TEXT_LK_SENDER_ID = setting.TEXT_LK_SENDER_ID


def send_config(config, phone_number):
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
        "message": f"Your newly created config : {config}"
    }

    response = requests.post(url, headers=headers, json=data)
    

    try:
        print(response.json())
        return True
    except Exception as e:
        print("Failed to parse response:", e)
        print("Raw response:", response.text)

