import requests
import dotenv
import os


def send_multiple_sms(token, dispatch_id, messages):
    url = 'https://notify.eskiz.uz/api/message/sms/send-batch'

    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
    }

    data = {
        "messages": messages,
        "from": "4546",
        "dispatch_id": dispatch_id
    }

    response = requests.post(url, headers=headers, json=data)

    return response.json()


dotenv.load_dotenv()
dispatch_id = 123
token = os.getenv("TOKEN")
text = "Bu Eskiz dan test"
message = [
    {"user_sms_id": "sms1", "to": 998914021601, "text": text},
    {"user_sms_id": "sms2", "to": 998339991601, "text": text}
]
print(send_multiple_sms(token, dispatch_id, message))
