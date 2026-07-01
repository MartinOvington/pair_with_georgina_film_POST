import sys
import os
from fixed_data import FIXED_BOOKS, FIXED_AUTHORS
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

"""
Doing a get request to /books endpoint
Gives status code 200
"""
def test_get_books_returns_a_200():
    client = app.test_client()

    response = client.get("/books")

    assert response.status_code == 200

"""
Doing a get request to /books endpoint
Returns the list of books in the response body
"""
@pytest.mark.skip(reason="Books page changed already to have fixed books")
def test_get_books_returns_all_books():
    client = app.test_client()
    response = client.get("/books")

    assert response.json == FIXED_BOOKS

"""
Doing a get request to /authors endpoint
Gives status code 200
"""
def test_get_authors_gives_code_200():
    client = app.test_client()
    response = client.get("/authors")

    assert response.status_code == 200

"""
Doing a get request to /authors endpoint
Returns the list of authors
"""
def test_get_authors_gives_all_authors():
    client = app.test_client()
    response = client.get("/authors")

    assert response.json == FIXED_AUTHORS