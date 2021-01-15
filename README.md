### This is a basic webhook application for processing shipment notifications with EasyPost and Twilio.

### Tutorial Featured on the Twilio Python Blog
https://www.twilio.com/blog/build-shipment-notification-service-python-flask-twilio-easypost

To set up the app, start by running the following commands in the same directory as your copy of the app to set up your environment.
```
python3 -m shipment-notifications-venv venv
source shipment-notifications-venv/bin/activate
pip install -r requirements.txt
```

Once you have the environment set up you'll need an EasyPost and Twilio Account, as well as a couple phone numbers (one send SMS from Twilio and one to receive SMS from Twilio) that you save in your environment file.
```
export EASYPOST_API_KEY=<YOUR EASYPOST API KEY>
export TWILIO_ACCOUNT_SID=<YOUR TWILIO ACCOUNT SID>
export TWILIO_AUTH_TOKEN=<YOUR TWILIO AUTH TOKEN>
export TWILIO_PHONE=<YOUR TWILIO PHONE>
export NOTIFICATION_PHONE=<YOUR PHONE NUMBER>
````


