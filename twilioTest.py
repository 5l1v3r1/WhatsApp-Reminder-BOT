# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure

f = open("token.password", "r")
token = f.readline()
f.close()

account_sid = 'AC23891757669d832bdd5ad158c530548a'
auth_token = token
client = Client(account_sid, auth_token)

message = client.messages.create(
         from_='whatsapp:+15005550006',
         body='Hi, Joe! Thanks for placing an order with us. We’ll let you know once your order has been processed and delivered. Your order number is O12235234',
         to='whatsapp:+905395740062'
     )

print(message.sid)