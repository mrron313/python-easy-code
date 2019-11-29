import smtplib
from email.mime.audio import MIMEAudio
from email.mime.multipart import MIMEMultipart

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login("yd.arif456@gmail.com", "4reosdkfksdjfiehriow4ir3wesac")

BODY = MIMEMultipart()
BODY['From'] = "yd.arif456@gmail.com"
BODY['To'] = "ez.boy763@gmail.com" 
BODY['Subject'] = "Youtube Mp3 Converter"

server.sendmail(
  "yd.arif456@gmail.com", 
  "ez.boy763@gmail.com", 
  BODY)
server.quit()