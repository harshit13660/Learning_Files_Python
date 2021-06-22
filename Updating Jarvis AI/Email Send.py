import smtplib

sender_email = "johnwick13660@gmail.com"
rec_email = "tomarharsh8@gmail.com"
password = "johnyzindabad"
message = f"Subject: Confirm Your Mail\n\nThis is my text"
print(message)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
print(server.login(sender_email, password))
print("Login success")
server.sendmail(sender_email, rec_email, message)
print("Email has been sent to ", rec_email)