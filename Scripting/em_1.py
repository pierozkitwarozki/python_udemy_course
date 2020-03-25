# Sending e-mails

import smtplib  # Simple Mail Transfer Protocol
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Bartlomiej Pierog'
email['to'] = 'bartekhenry14@gmail.com'
email['subject'] = 'Hello from Python Script'

email.set_content('I\'m a Python master ')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jordandan2323@gmail.com", "grazyna2017")
    smtp.send(email)
