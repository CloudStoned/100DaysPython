from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

app = Flask(__name__)

class Base(DeclarativeBase):
    pass

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///C:/Users/Kraum/PROJECTS/100DaysPython/WEB/SqlLite/crud.db"

db = SQLAlchemy(model_class=Base)

db.init_app(app)

class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()

def insert_data():
    with app.app_context():
        new_book = Book(title="Atomic Habits", author="Sana", rating=9.9)
        db.session.add(new_book)
        db.session.commit()

def read_data():
    with app.app_context():
        result = db.session.execute(db.select(Book).order_by(Book.title))
        all_books = result.scalars().all()  
        for book in all_books:
            print(f"Title: {book.title}, Author: {book.author}, Rating: {book.rating}")

def read_particular_data():
    with app.app_context():
        book = db.session.execute(db.select(Book).where(Book.title == "Harry Potter and the Goblet of Fire")).scalar()
        print(book)

def update_data():
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.title == "Harry Potter")).scalar()
        book_to_update.title = "Harry Potter and the Chamber of Secrets"
        db.session.commit() 

def update_particualar_data():
    book_id = 1
    with app.app_context():
        book_to_update = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        book_to_update.title = "Harry Potter and the Goblet of Fire"
        db.session.commit()  

def delete_data():
    book_id = 1
    with app.app_context():
        book_to_delete = db.session.execute(db.select(Book).where(Book.id == book_id)).scalar()
        db.session.delete(book_to_delete)
        db.session.commit()


