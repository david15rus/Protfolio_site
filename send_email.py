import smtplib
import ssl

host = 'smtp.gmail.com'
port = 465

username = 'razzzial15@gmail.com'
password = 'gwrvrxsyskcjfage'

reciever = 'razzzial15@gmail.com'
context = ssl.create_default_context()

message = '''\
Subject: Test mail
Hi!
How are you?
Bye!
'''
with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, reciever, message)
