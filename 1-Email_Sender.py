import os
from email.message import EmailMessage
import ssl
import smtplib

email_sender = "moustafanaguib200@gmail.com"
email_password = os.environ.get("Email_Password")
email_receiver = "moustafanaguib200@outlook.com"

subject = "How to send an email by using python"
body ="""
if you want to learn how you can send an email by using python
you can watch this youtube video ===> "https://tinyurl.com/nj6nmpxp"
"""

email = EmailMessage()

email['From'] = email_sender
email['To'] = email_receiver
email['Subject'] = subject
email.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtb:
    smtb.login(email_sender, email_password)
    smtb.sendmail(email_sender, email_receiver, email.as_string())
