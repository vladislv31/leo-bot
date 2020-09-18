import config
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def send_mail(to_mail, from_mail, from_pass, sub, text, host='smtp.ukr.net', port=465):
    s = smtplib.SMTP(host=host, port=port)

    s.starttls()
    s.login(from_mail, from_pass)

    msg = MIMEMultipart()

    message = text

    msg['From'] = from_mail
    msg['To'] = to_mail
    msg['Subject'] = sub

    msg.attach(MIMEText(message, 'plain'))

    s.send_message(msg)


    del msg

    s.quit()


def send_command(command):
    print('start')
    send_mail(config.to_mail, config.from_mail, config.from_pass, 'Trading Bot Command', command,)
    print('end')
