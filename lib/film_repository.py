from lib.film import *

class FilmRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        film_factory = self._connection.make_class_row(Film)
        return self._connection.execute(
            "SELECT * FROM films",
            row_factory=film_factory
        )
    
    def create(self, film):
        self._connection.execute(
            "INSERT INTO films " \
            "(title, release_year) " \
            "VALUES(%s, %s)",
            [film.title, film.release_year]
        )