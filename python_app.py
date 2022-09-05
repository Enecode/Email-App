from email.message import EmailMessage
from email_app.app2 import  passwod
import ssl
import smtplib

email_sender = 'isahjacob0@gmail.com'
email_password = passwod

email_receiver = 'loxavo8010@rxcay.com'

subject = "The reason for your mail"

body = f"""
Dear Programmer, \n\tMy name is Isah Jacob, and I must say that you are a great coder, as well as a very smart one.
I'm writing to you today because I've noticed you are not paying attention to those minor syntax errors. 
Take note that this is what makes you a lifelong learner. In the world of programming, you cannot be perfect.
\n
I'm hoping to hear from you soon.\n
best wishes for your success Jacob\n
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
