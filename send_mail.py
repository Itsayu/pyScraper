# import smtplib
#
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login('2027195ayush@gmail.com', 'rbhrvbotytxtdiwy')
#
# message = "Hey there, Sending mail through Python!"
# server.sendmail('2027195ayush@gmail.com', 'surajten00@gmail.com', message)
#
# server.quit()

# ------------------------OR------------------------
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.mime.base import MIMEBase
# from email import encoders
#
# from_add = '2027195ayush@gmail.com'
# to_add = 'ayushkr9976@gmail.com'
# subject = "Mail from Python Script - 1"
#
# msg = MIMEMultipart()
# msg['From'] = from_add
# msg['To'] = to_add
# msg['Subject'] = subject
#
# # --------------<b> TAG OR BOLD TAG------AND <br> FOR NEW LINE----------
# body1 = "<b>Hey there! Sending mail through Python!</b><br>Good Morning"
# # body2 = "Good morning"
# msg.attach(MIMEText(body1, 'html'))
# # msg.attach(MIMEText(body2, 'html'))
#
# my_file = open("scrape.csv", 'rb')
#
# part = MIMEBase('application', 'octet-stream')
# part.set_payload((my_file).read())
# encoders.encode_base64(part)
# part.add_header('content-Disposition', 'attachment; filename= ' + 'scrape.csv')
# msg.attach(part)
#
#
# message = msg.as_string()
#
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login('2027195ayush@gmail.com', 'rbhrvbotytxtdiwy')
#
# # message = "Hey there, Sending mail through Python!"
# server.sendmail(from_add, to_add, message)
#
# server.quit()

# ------------------------------------------------------THE SEND_MAIL.PY IS INTEGRATED BY OUR SCRAPE.PY----------------------------------------------------------------------------------

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add = '2027195ayush@gmail.com'
    to_add = 'neelampanjwani72@gmail.com'
    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject

# --------------<b> TAG OR BOLD TAG------AND <br> FOR NEW LINE----------
    body1 = "<b>Today's Finance Report Attached</b><br>Good Morning"
# body2 = "Good morning"
    msg.attach(MIMEText(body1, 'html'))
# msg.attach(MIMEText(body2, 'html'))

    my_file = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)


    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('2027195ayush@gmail.com', 'rbhrvbotytxtdiwy')

    server.sendmail(from_add, to_add, message)

    server.quit()