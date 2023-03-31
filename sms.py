import datetime
from twilio.rest import Client
from threading import Timer

class sms:
    def send_sms(self, number):
        # Put your Twilio account SID here
        account_sid = "AC81ef07b91f720edc67595f8046ee4c7e"
        auth_token = "c3fca40194ac2759ee0980a1eea728f2"  # Put your auth token here

        client = Client(account_sid, auth_token)

        message = client.api.account.messages.create(
            to=number,  # Put your cellphone number here
            from_="+14346036240",  # Put your Twilio number here
            body="You received this notification because you have not responded on your monitoring device. Please contact the nurse as soon as possible.")