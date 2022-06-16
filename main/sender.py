from twilio.rest import Client
import requests

TOKEN = "4badc9da04df357025caa7845f562b0d"
DEVICE_ID = 315565
phone = '+19377876495'


# account_sid = 'AC4a4fcc14030a7e4ddd5b3e046e42bccc'
# auth_token = 'f62cc69374e53ac105e0465ea21da83b'
# client = Client(account_sid, auth_token)

# message = client.messages.create(
#     from_=phone,
#     to='+998916046210',
#     body="Hello !",
# )

# print(message.sid)


def sms_send(phone_number, msg):
    url = f"https://semysms.net/api/3/sms.php?token={TOKEN}&device={DEVICE_ID}&phone={phone_number}&msg={msg}"
    response = requests.get(url)
    print(response)  # if  200 >> OK
    print(url)
    return True


sms_send(998905317494, "qale ishla")
