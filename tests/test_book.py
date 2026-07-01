from lib.book import *
"""
Creating a book
Has the expected attributes
"""
def test_book_creation():
    book = Book("My title", "My author", 1)
    assert book.id == 1
    assert book.title == "My title"
    assert book.author == "My author"

"""
Two books are equal if they have the same attributes
"""
def test_book_equality():
    book1 = Book("My title", "My author", 1)
    book2 = Book("My title", "My author", 1)
    assert book1 == book2

"""
Calling str on a book
Returns a nice string
"""
def test_book_str():
    book = Book("My title", "My author", 1)
    assert str(book) == "Book(1, My title, My author)"