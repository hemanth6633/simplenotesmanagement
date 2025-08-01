import smtplib
from email.message import EmailMessage
def send_mail(to, subject, body):
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login('atmuribhaskar2002@gmail.com','uhor ujmm vwry uflz')
    msg = EmailMessage()
    msg['From'] = 'atmuribhaskar2002@gmail.com'
    msg['To'] = to
    msg['Subject'] = subject
    msg.set_content(body)
    server.send_message(msg)
    server.close()
    