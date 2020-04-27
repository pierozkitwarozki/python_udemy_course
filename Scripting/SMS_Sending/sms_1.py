from twilio.rest import Client

account_sid = 'AC02f52799703bdd2241230398c73fc8bd'
auth_token = 'eec12fb213b177c4637ed3d9d1ede42b'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+16626440158',
    body='Boro to gej',
    to='+48697584302'
)

print(message.sid)