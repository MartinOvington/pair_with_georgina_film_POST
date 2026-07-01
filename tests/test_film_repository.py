from lib.film_repository import *

"""
Gets all films
"""
def test_get_all_films(clean_db):
    film_repo = FilmRepository(clean_db)
    films = film_repo.all()
    assert films == [Film('Jaws', 1987, 1),
                    Film('Scream', 1999, 2),
                    Film('Project Hail Mary', 2026, 3)]
    

"""
Creating a new films
Adds it to the database
"""
def test_create_film(clean_db):
    film_repo = FilmRepository(clean_db)
    film = Film("Harold and Maude", 1971)
    result = film_repo.create(film)
    assert result is None

    films = film_repo.all()
    assert films == [Film('Jaws', 1987, 1),
                    Film('Scream', 1999, 2),
                    Film('Project Hail Mary', 2026, 3),
                    Film("Harold and Maude", 1971, 4)]