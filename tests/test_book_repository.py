from lib.book import *
from lib.book_repository import *

"""
Calling all on book repository
Returns all the books in the database
"""
def test_get_all_books(clean_db):
    repo = BookRespository(clean_db)

    books = repo.all()
    assert books == [
        Book('The Gruffalo', 'Julia Donaldson', 1),
        Book('Ada Twist, Scientist', 'Andrea Beaty', 2),
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3),
        Book('Dragons in a Bag', 'Zetta Elliott', 4)
    ]

"""
Calling create on book repository
Adds the book to the database
"""
def test_create_book(clean_db):
    repo = BookRespository(clean_db)

    book = Book('New book', 'New author')
    result = repo.create(book)
    assert result is None

    books = repo.all()
    assert books == [
        Book('The Gruffalo', 'Julia Donaldson', 1),
        Book('Ada Twist, Scientist', 'Andrea Beaty', 2),
        Book('The Girl Who Drank the Moon', 'Kelly Barnhill', 3),
        Book('Dragons in a Bag', 'Zetta Elliott', 4),
        Book('New book', 'New author', 5)
    ]