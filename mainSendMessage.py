from twilio.rest import Client

def sendMessage(textMessage):
    f = open("token.password", "r")
    token = f.readline()
    f.close()

    account_sid = 'AC23891757669d832bdd5ad158c530548a'
    auth_token = token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=str(textMessage),
        to=f'whatsapp:+905395740062'
    )

    print(message.sid)