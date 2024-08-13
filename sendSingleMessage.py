import requests


def send_sms(token, mobile_phone, message, from_number, callback_url):
    url = 'https://notify.eskiz.uz/api/message/sms/send'

    headers = {
        'Authorization': f'Bearer {token}',
    }

    data = {
        'mobile_phone': mobile_phone,
        'message': message,
        'from': from_number,
        'callback_url': callback_url
    }

    # print("Sending request with headers:", headers)
    # print("Sending request with data:", data)

    response = requests.post(url, headers=headers, data=data)

    return response.status_code

# dotenv.load_dotenv()
#
# # Replace with your actual token
# token = os.getenv('TOKEN')
#
# # Verify if the token is loaded correctly
# if not token:
#     print("Token is not set or loaded incorrectly.")
#     exit()
#
# # Define the parameters
# mobile_phone = "998914021601"
# message = "Bu Eskiz dan test"
# from_number = "4546"
# callback_url = "http://0000.uz/test.php"
#
# # Send the SMS
# response = send_sms(token, mobile_phone, message, from_number, callback_url)
#
# # Print the response
# print(response)
