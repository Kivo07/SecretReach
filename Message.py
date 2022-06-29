import os
from twilio.rest import Client
import socket
import Keys
user = socket.gethostname()
IP = socket.gethostbyname(user)

client = Client(Keys.ACCOUNT_SID, Keys.AUTH_TOKEN)

message = client.messages\
    .create(body="URGENT! HELP REQUESTED AT IP ADDRESS:" + str(IP),  from_=Keys.PHONE_NUMBER, to=Keys.TEST_NUMBER)

print(message.sid)
