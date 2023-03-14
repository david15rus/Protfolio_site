import smtplib
import ssl
import os

HOST = 'smtp.gmail.com'
PORT = 465
username = 'razzzial15@gmail.com'
password = os.getenv("PASSWORD")
context = ssl.create_default_context()
reciever = 'razzzial15@gmail.com'


def send_email(message):
    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

