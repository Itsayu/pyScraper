import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add = 'ENTER YOUR E-MAIL ADDRESS'
    to_add = 'TO E-MAIL ADDRESS'
    subject = "Finance Stock Report"

    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['Subject'] = subject
    
    body1 = "<b>Today's Finance Report Attached</b><br>Good Morning"
    msg.attach(MIMEText(body1, 'html'))

    my_file = open(filename, 'rb')

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((my_file).read())
    encoders.encode_base64(part)
    part.add_header('content-Disposition', 'attachment; filename= ' + filename)
    msg.attach(part)


    message = msg.as_string()

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login('YOUR E-MAIL ID', 'E-MAIL PASSWORD/ GOOGLE TEMP. PASWSORD')

    server.sendmail(from_add, to_add, message)

    server.quit()
