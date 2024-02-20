import smtplib,ssl
from email.message import EmailMessage

def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "YOUR EMAIL"
    password = "YOUR PASSWORD" #This email must be generated in your google account

    receiver = "YOUR PASSWORD"

    subject = "New Article"
    body = message

    em = EmailMessage()
    em['From'] = username
    em['To'] = receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, em.as_string())