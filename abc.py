from importlib.resources import contents

print('STARTING')
import smtplib
from email.message import EmailMessage

def send_mail(to,subject,content):
    message = EmailMessage()
    message['from'] = 'demirbahadir0601@gmail.com'
    message['To'] = to
    message['Subject'] = subject
    message.set_content(content)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login('demirbahadir0601@gmail.com','wweh uqym fqkd tonr')
            smtp.send_message(message)
            print('succesfull')
    except Exception as e:
        print('failed')

send_mail(
    to= 'sinembabadagli@icloud.com',
       subject='Hello, this e-mail is the first test e-mail of the e-mail system written by Bahadir.',
    content = 'This is a test email'
)