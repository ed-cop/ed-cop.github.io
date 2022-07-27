from logging.handlers import SMTPHandler
import smtplib
from email.message import EmailMessage
#pesan = input("masukan pesan anda :")
#
#

#
#
msg = EmailMessage()
msg['Subject'] = 'Check out Bronx as a puppy!'
#msg['From'] = 'akunefgy@gmail.com'
msg['To'] = 'tumbaljembatan@gmail.com'
msg.set_content('This is a plain text email')
msg.add_alternative("""\
<!DOCTYPE html>
<html>
<body>
<h1 style="color:SlateGray;">This is an HTML Email!</h1>
</body>
</html>
""", subtype='html')
#
##server = smtplib.SMTP_SSL("smtp.gmail.com",465)
#server.login("akunefgy@gmail.com","ftkhdgrqbrqelido")
#server.sendmail("akunefgy@gmail.com","tumbaljembatan@gmail.com",
#               pesan)

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login("akunefgy@gmail.com","ftkhdgrqbrqelido")
    smtp.send_message(msg)
#server.quit()