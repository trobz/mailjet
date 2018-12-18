#!/usr/bin/env python2
#
# Send an email via the Mailjet API:
# - https://github.com/mailjet/mailjet-apiv3-python
# - https://dev.mailjet.com/guides/#sending-a-basic-email-v3
# - https://dev.mailjet.com/guides/#send-api-json-properties-v3

from mailjet_rest import Client

from config import SMTP_USER, SMTP_PASS

api_key = SMTP_USER
api_secret = SMTP_PASS
mailjet = Client(auth=(api_key, api_secret))

data = {
    'FromEmail': 'nils+member@trobz.com',
    #'FromEmail': 'gestion@superquinquin.fr',
    'FromName': 'Member',
    'Subject': 'please ignore this email',
    'Sender': True, # also tried with True, 'True', 1
    'Text-part': 'This is a test from Trobz: using the API',
    'Recipients': [{'Email':'nils+coordinator@trobz.com', 'Name':'Coordinator'}]
}
result = mailjet.send.create(data=data)
print result.status_code
print result.json()
