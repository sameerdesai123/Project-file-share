# pip install twilio
from twilio.rest import Client

# Your Account Sid and Auth Token from twilio.com/console
account_sid = ''
auth_token = ''
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="ALERT. Your car is under threat!!",
                     from_='',
                     to=''
                 )

# print(message.sid)
