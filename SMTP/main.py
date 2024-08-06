import smtplib
from dotenv import load_dotenv
import os
import spotipy

load_dotenv()


load_dotenv()

email_sender = os.environ["email_sender"]
app_password =  os.environ["app_password"]
email_reciever = os.environ["email_reciever"]

try:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_sender, app_password)
    server.sendmail(email_sender, email_reciever, "TEST MAIL")
    print('Mail Sent')

except smtplib.SMTPAuthenticationError as e:
    print(f"Failed to send email: {e}")
finally:
    server.quit()
