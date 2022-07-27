
import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("akunefgy@gmail.com","ftkhdgrqbrqelido")
server.sendmail("akunefgy@gmail.com",
"tumbaljembatan@gmail.com",
"kon")
server.quit()
