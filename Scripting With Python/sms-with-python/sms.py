from twilio.rest import Client

account_sid = 'ACefc806654e5d7ea8eb83ce3a1eecd9e2'
auth_token = '167b4f32c78a68d427769e93bebb232a'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+16209129204',
    body='I CANT BELIEVE THIS WORKS',
    to='+84395193759'
)

print(message.sid)
