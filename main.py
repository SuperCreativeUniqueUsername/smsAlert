import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
 
message = MIMEMultipart()
message["To"] = 'To line here.'
message["From"] = 'From line here.'
message["Subject"] = 'Subject line here.'

title = '<b> Title line here. </b>'
messageText = MIMEText('''Message body goes here.''','html')
message.attach(messageText)

email = 'Your Gmail address here.'
password = 'Your app password here.'

server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo('Gmail')
server.starttls()
server.login(email,password)
fromaddr = 'From line here.'
toaddrs  = 'Address you send to.'
server.sendmail(fromaddr,toaddrs,message.as_string())

server.quit()