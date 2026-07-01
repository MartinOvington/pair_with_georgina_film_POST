from lib.book import *

class BookRespository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        book_factory = self._connection.make_class_row(Book)
        return self._connection.execute(
            "SELECT * FROM books", 
            row_factory=book_factory)
    
    def create(self, book):
        self._connection.execute(
            "INSERT INTO books " \
            "(title, author) " \
            "VALUES(%s, %s)", [book.title, book.author]
        )
