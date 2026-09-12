import smtplib
from email.mime.text import MIMEText

sender_email = ""
receiver_email =""
app_password = ""

message = """
Good Morning NIYA!

This email was sent automatically by your Pulse Bot.

Have a great day!
"""

msg = MIMEText(message)
msg["Subject"] = "Pulse Daily Report"
msg["From"] = sender_email
msg["To"] = receiver_email

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()

server.login(sender_email, app_password)
server.send_message(msg)

server.quit()

print("Email Sent Successfully!")
