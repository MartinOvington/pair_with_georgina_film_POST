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