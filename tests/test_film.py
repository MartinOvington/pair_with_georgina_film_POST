from lib.film import *

def test_film_equality():
    film1 = Film("Test1", 1999, 1)
    film2 = Film("Test1", 1999, 1)
    assert film1 == film2

def test_film_str():
    film = Film("Test1", 1999, 1)
    assert str(film) == "Film(1, Test1, 1999)"