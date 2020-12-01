#!/usr/bin/env python3

import email.message
import mimetypes
import os.path
import smtplib
import os
def generate_withno_attachement(sender, recipient, subject, body):
  """Creates an email with no attachement."""
  # Basic Email formatting
  message = email.message.EmailMessage()
  message["From"] = sender
  message["To"] = recipient
  message["Subject"] = subject
  message.set_content(body)
  return message

def send(message):
  """Sends the message to the configured SMTP server."""
  mail_server = smtplib.SMTP('localhost')
  mail_server.send_message(message)
  mail_server.quit()
