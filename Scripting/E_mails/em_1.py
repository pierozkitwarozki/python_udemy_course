# Sending e-mails

import smtplib  # Simple Mail Transfer Protocol
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('./HTML_Mail/index.html').read_text())
email = EmailMessage()
email['from'] = 'Bartlomiej Pierog'
email['to'] = 'bartekhenry14@gmail.com'
email['subject'] = 'Hello from Python Script'
email.set_content(html.substitute(name='Bart'))

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("jordandan2323@gmail.com", "grazyna2017")
    smtp.send(email)

# Code is good, but it doesn't work beacuse of google security problems.