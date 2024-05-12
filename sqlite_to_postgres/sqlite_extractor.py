import sqlite3
from models import Filmwork, Genre, Person, GenreFilmwork, PersonFilmwork


class SQLiteExtractor():
    connection: sqlite3.Connection

    tables_class_map = {
        'film_work': Filmwork,
        'genre': Genre,
        'person': Person,
        'genre_film_work': GenreFilmwork,
        'person_film_work': PersonFilmwork
    }

    TABLE_ITER_SIZE = 100

    def __init__(self, connection: sqlite3.Connection) -> None:
        self.connection = connection
        self.connection.row_factory = sqlite3.Row

    def iter_table(self, table_name: str, size: int):
        curs = self.connection.cursor()
        curs.execute(f'SELECT * from {table_name};')

        while True:
            rows = curs.fetchmany(size=size)
            if not rows:
                break
            yield rows

    def extract_movies(self):
        res: dict[str, list[dict]] = {}
        for table_name, model in self.tables_class_map.items():
            res[table_name] = []
            for rows in self.iter_table(table_name, self.TABLE_ITER_SIZE):
                res[table_name].extend([
                    model(**dict(row)).transform()
                    for row in rows
                ])

        return res
