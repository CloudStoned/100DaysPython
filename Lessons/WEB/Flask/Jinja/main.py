from flask import Flask, render_template, url_for
import random
import datetime
import requests

app = Flask(__name__, 
            template_folder='templates', 
            static_folder='static')

agify_api = "https://api.agify.io/?name="
genderize_api = "https://api.genderize.io/?name="

@app.route('/')
def home():
    rand_number = random.randint(0,9)
    year_today = datetime.datetime.now().year
    return render_template("index.html", num=rand_number, year=year_today)

@app.route('/guess/<name>')
def guess(name):
    age_response = requests.get(f"{agify_api}{name}")
    gender_response = requests.get(f"{genderize_api}{name}")

    age_json = age_response.json()
    gender_json = gender_response.json()

    age = age_json['age']
    gender = gender_json['gender']

    return render_template("index.html", name=name, age=age, gender=gender)

@app.route('/blog/<num>')
def blog(num):
    # print(num)
    blog_url = "https://api.npoint.io/d9177d1696f108b98c22"
    response = requests.get(blog_url)
    all_posts = response.json()
    
    return render_template("blog.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)