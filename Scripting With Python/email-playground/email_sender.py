import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Vong Hoang Vinh'
email['to'] = 'vonghoangvinh1989@gmail.com'
email['subject'] = 'You won 1,000,000 dollars!'

email.set_content(html.substitute({'name': 'TinTin'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('vonghoangvinh1989business@gmail.com', 'bypxzzfnltygkdxg')
    smtp.send_message(email)
    print('all good boss!')
