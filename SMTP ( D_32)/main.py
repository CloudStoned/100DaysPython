import smtplib

my_email = "cloudbagtas@gmail.com"
password = "+Pandora100104"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="cloudneo0719@gmail.com", msg="Hello from cloudbagtas@gmail.com")
connection.close()