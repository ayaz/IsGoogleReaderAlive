#!/usr/bin/env python
from flask import Flask
app = Flask(__name__)

from urllib import urlopen
from BeautifulSoup import BeautifulSoup
GoogleReaderRootURL = 'http://www.google.com/reader'

@app.route("/")
def IsGoogleReaderAlive():
    try:
        html = urlopen(GoogleReaderRootURL).read()
    except:
        raise
        return None

    soup = BeautifulSoup(html)
    if soup.find('a', attrs={'id': 'tour-link'}):
        return 'It is stll ALIVE!'
    else:
        send_mail(message='It really is down!')
        return 'Bugger! It is really gone!'


def send_mail(message):
    import smtplib
    from email.MIMEMultipart import MIMEMultipart
    from email.MIMEText import MIMEText

    gmailUser = 'GMAIL_USER'
    gmailPassword = 'GMAIL_PASS'
    recipient = 'TO_ADDRESS'

    msg = MIMEMultipart()
    msg['From'] = gmailUser
    msg['To'] = recipient
    msg['Subject'] = "IsGoogleReaderAlive: It's down!"
    msg.attach(MIMEText(message))

    mailServer = smtplib.SMTP('smtp.gmail.com', 587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(gmailUser, gmailPassword)
    mailServer.sendmail(gmailUser, recipient, msg.as_string())
    mailServer.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
