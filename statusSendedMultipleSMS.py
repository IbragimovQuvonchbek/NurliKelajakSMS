import dotenv
import os
import requests


def status_sms(token, dispatch_id):
    url = 'https://notify.eskiz.uz/api/message/sms/get-dispatch-status'

    headers = {
        'Authorization': f'Bearer {token}'
    }

    data = {
        'dispatch_id': dispatch_id,
        'is_global': '0'
    }

    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    return response.json()


dotenv.load_dotenv()
dispatch_id = 123
token = os.getenv("TOKEN")
sms = status_sms(token, dispatch_id)
print(sms)
