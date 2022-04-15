from decouple import config
from twilio.rest import Client


def run():
    account_sid = config("TWILIO_ACCOUNT_SID")
    auth_token = config("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="Essentials has processed your order and will be delivered to you by 16.04.2022 9 P.M.",
        from_="+12702897753",
        to="+919009042226",
    )

    print(message.sid)
