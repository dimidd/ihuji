

from twilio.rest import TwilioRestClient

# creating an SMS
def createMessage(account_sid, auth_token, from_who ,to_who,message_txt):
    client = TwilioRestClient(account_sid, auth_token)
    client.messages.create(
	to=to_who,
	from_=from_who,
	body=message_txt,
    )
