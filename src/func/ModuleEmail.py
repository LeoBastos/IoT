import smtplib
from email.message import EmailMessage


def send_mail(to_email, subject, message, server='smtp.gmail.com', from_email='leonardobastos04@gmail.com'):

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = ', '.join(to_email)
    msg.set_content(message)

    server = smtplib.SMTP_SSL(server, 465)
    server.login(from_email, '-00388ut32Leo')
    server.send_message(msg)

