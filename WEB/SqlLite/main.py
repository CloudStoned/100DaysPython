from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

##CREATE DATABASE
class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/Kraum/PROJECTS/100DaysPython/WEB/SqlLite/new-books-collection.db"


# Create the extension
db = SQLAlchemy(model_class=Base)

# Initialise the app with the extension
db.init_app(app)

# Create Table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

    def __rep__(self):
        return f"<Book {self.title}"

# Create table schema in the database. Requires application context.
with app.app_context():
    db.create_all()

# CREATE RECORD
with app.app_context():
    new_book = Book(id=1, title="Sana", author="Twice", rating=9.3)
    db.session.add(new_book)
    db.session.commit()
