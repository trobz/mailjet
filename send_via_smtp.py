#!/usr/bin/env python2
#
# Send an email via smtp, like Odoo does

import smtplib
from email.mime.text import MIMEText

##
# Configuration
##

from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS

# Catchall
CATCHALL = "nils+catchall@trobz.com"

# Sender header
VALIDATED = "gestion@superquinquin.fr"

# MAIL FROM:
BOUNCE = "nils+bounce-533192-memberspace.conversation-17@trobz.com"
SMTP_FROM = BOUNCE
#SMTP_FROM = "gestion@superquinquin.fr"

# "Unvalidated" From address:
UNVALIDATED = "nils+member@trobz.com"

# Recipients:
RECIPIENTS = [ "nils+coordinator@trobz.com" ]

TEXT = "This is a test from Trobz: From = UNVALIDATED"

##
# Build the mail
##

msg = MIMEText(TEXT)
msg['Sender'] = VALIDATED
msg['Return-Path'] = BOUNCE
msg['Subject'] = "please ignore this email"
msg['From'] = UNVALIDATED
msg['Reply-To'] = CATCHALL
msg['To'] = ",".join(RECIPIENTS)

##
# Send the mail
##

smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(SMTP_HOST, SMTP_PORT)
smtp.starttls()
smtp.login(SMTP_USER, SMTP_PASS)
smtp.sendmail(SMTP_FROM, RECIPIENTS, msg.as_string())
smtp.quit()
