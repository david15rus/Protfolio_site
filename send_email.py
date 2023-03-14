import smtplib
import ssl

HOST = 'smtp.gmail.com'
PORT = 465
username = 'razzzial15@gmail.com'
password = 'gwrvrxsyskcjfage'
context = ssl.create_default_context()


def send_email(message):
    reciever = 'razzzial15@gmail.com'

    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(username, password)
        server.sendmail(username, reciever, message)

