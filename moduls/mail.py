import smtplib
from email.message import EmailMessage

import config


def send_mail(to_email, subject, message, from_email, server=config.server):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email
    msg.set_content(message)
    server = smtplib.SMTP(server, 587)
    server.set_debuglevel(1)
    server.login(to_email, config.password)  # user & password
    server.send_message(msg)
    server.quit()
