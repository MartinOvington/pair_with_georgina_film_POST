from flask import Flask, request, render_template, redirect
from fixed_data import FIXED_BOOKS, FIXED_AUTHORS
from lib.book_repository import *
from lib.database_connection import *

app = Flask(__name__)
connection = DatabaseConnection()
connection.connect()
connection.seed("./seeds/book_store.sql")
book_repo = BookRespository(connection)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/hello', methods=['GET'])
def hello():
    return "Hello to you too"

@app.route('/books', methods=['GET'])
def get_books():
    books = book_repo.all()
    return render_template("books.html", books=books)

@app.route('/books', methods=['POST'])
def create_book():
    connection = DatabaseConnection()
    connection.connect()
    book_details = request.form
    book = Book(title=book_details["title"], author=book_details["author"])
    book_repo.create(book)
    return redirect("/books")


    
@app.route('/authors', methods=['GET'])
def get_authors():
    return FIXED_AUTHORS

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)