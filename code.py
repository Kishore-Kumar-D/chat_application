from twilio.rest import Client 
from keys import TWILIO_ACCOUNT_SID, TWILIO_API_KEY, twilio_no, mobile

client = Client(TWILIO_ACCOUNT_SID, TWILIO_API_KEY)

messages = "Your message goes here..."

message = client.messages.create(to=mobile, from_=twilio_no,body=messages)

print(message)
