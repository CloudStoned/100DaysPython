from flask import Flask, render_template, request
import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
my_email = os.environ["my_email"]
app_password = os.environ["app_password"]

if not my_email or not app_password:
    raise Exception("Email or App password not loaded from .env")

posts = requests.get("https://api.npoint.io/9992e2546e53c14862de").json()

app = Flask(__name__)

@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        try:
            data = request.form
            name = data["name"]
            user_email = data["email"]
            phone = data["phone"]
            message = data["message"]

            # Create the email headers and message
            email_message = f"Subject: New Message from {name}\n"
            email_message += f"From: {user_email}\n"
            email_message += f"Reply-To: {user_email}\n\n"
            email_message += f"Name: {name}\nPhone: {phone}\nMessage: {message}\nUser Email: {user_email}"
            
            # Authenticate with your service account
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(my_email, app_password)
            server.sendmail(my_email, my_email, email_message)

            return render_template("contact.html", msg_sent=True)
            
        except smtplib.SMTPAuthenticationError as e:
            print(f"Failed to send email due to authentication error: {e}")
            return render_template("contact.html", msg_sent=False, error="Authentication failed.")
        except Exception as e:
            print(f"Failed to send email: {e}")
            return render_template("contact.html", msg_sent=False, error=str(e))
    
    return render_template("contact.html", msg_sent=False)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
