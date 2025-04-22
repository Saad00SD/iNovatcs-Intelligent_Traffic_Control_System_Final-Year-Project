from twilio.rest import Client

# Twilio credentials
TWILIO_ACCOUNT_SID = 'ACe12bb94b2516a6f03f6077a24bf4d061'
TWILIO_AUTH_TOKEN = '2b47b428c4f09d1b4ba3622883c1ac39'
TWILIO_PHONE_NUMBER = '+12623813640'

# Create Twilio client
client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

def send_sms(to_phone_number, message):
    """ Function to send SMS using Twilio """
    message = client.messages.create(
        body=message,
        from_=TWILIO_PHONE_NUMBER,
        to=to_phone_number,
    )
    return message.sid
