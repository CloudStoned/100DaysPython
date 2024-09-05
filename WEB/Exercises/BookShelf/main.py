from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    print(all_books)
    return render_template("index.html", books = all_books) # To pass a data from main.py to .html

@app.route("/add", methods = ["GET", "POST"])
def add():
    # Get data from the add.html using request.
    if request.method == "POST":
        new_book = {
            "author": request.form["author"],
            "title": request.form["title"],
            "rating": request.form["rating"]
        }
        all_books.append(new_book)
        print("Books Appended")
        return redirect(url_for('home'))

    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

