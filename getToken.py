import requests
import dotenv
import os

dotenv.load_dotenv()
url = 'https://notify.eskiz.uz/api/auth/login'
data = {
    'email': os.getenv('GMAIL'),
    'password': os.getenv('PASSWORD'),
}

response = requests.post(url, data=data)

print(response.status_code)
print(response.json())
