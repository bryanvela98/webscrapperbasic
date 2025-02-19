from twilio.rest import Client
import os

def send_notification(message, to_phone_number):
    account_sid = os.getenv('TWILIO_ACCOUNT_SID')
    auth_token = os.getenv('TWILIO_AUTH_TOKEN')
    from_phone_number = os.getenv('TWILIO_PHONE_NUMBER')

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=message,
        from_=from_phone_number,
        to=to_phone_number
    )

    return message.sid