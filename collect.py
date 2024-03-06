from twilio.rest import Client
import auth.py


account_sid = 'AC28d031667feaac6108f812d5af5a2709'
auth_token = auth.token
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+18443373805',
  body='Hello from Mania',
  to='+18777804236'
)

print(message.sid)
