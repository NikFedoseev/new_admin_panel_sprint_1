from psycopg2.extensions import connection as _connection
from psycopg2.extras import execute_batch


class PostgresSaver():
    connection: _connection

    table_keys_map = {
        'film_work':  ['id', 'title', 'description', 'creation_date', 'rating', 'type', 'created', 'modified'],
        'genre': ['id', 'name', 'description', 'created', 'modified'],
        'person': ['id', 'full_name', 'created', 'modified'],
        'genre_film_work': ['id', 'genre_id', 'film_work_id', 'created'],
        'person_film_work': ['id', 'person_id', 'film_work_id', 'role', 'created'],
    }

    EXECUTE_PAGE_SIZE = 100

    def __init__(self, connection: _connection) -> None:
        self.connection = connection

    def execute_query(self, table_name, table_data, cur):
        table_keys = self.table_keys_map[table_name]
        keys = ', '.join(table_keys)
        placeholders = ', '.join(['%s' for _ in table_keys])

        data = [
            tuple(map(lambda key: item[key], table_keys))
            for item in table_data
        ]

        sql = f"INSERT INTO content.{table_name} ({keys}) VALUES ({placeholders}) ON CONFLICT DO NOTHING;"

        execute_batch(cur, sql, data, page_size=self.EXECUTE_PAGE_SIZE)

    def save_table_data(self, table_name: str, table_data: list[dict]):
        with self.connection.cursor() as cur:
            self.execute_query(table_name, table_data, cur)
            self.connection.commit()

    def save_all_data(self, data: dict):
        for table_name, table_data in data.items():
            self.save_table_data(table_name, table_data)
