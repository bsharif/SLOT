from twilio.rest import TwilioRestClient
import config
import db

client = TwilioRestClient(config.twilio_sid, config.twilio_token)


def send_sms(sms_to, sms_body):
    try:
        print("Sending SMS to Twilio API")
        message = client.messages.create(to=sms_to, from_=config.twilio_number, body=sms_body)
        db.log_sms(config.twilio_number, sms_to, sms_body, "OUT")
        print("SMS sent to Twilio API")

    except Exception as e:
        print(e)
        pass

