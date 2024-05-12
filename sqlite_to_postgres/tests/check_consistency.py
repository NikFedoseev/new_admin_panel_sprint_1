import sqlite3
import psycopg2
from contextlib import closing
import collections
import os
from dotenv import load_dotenv

load_dotenv()

pg_dsl = {
    'dbname': os.environ.get('DB_NAME'),
    'user':  os.environ.get('DB_USER'),
    'password': os.environ.get('DB_PASSWORD'),
    'host': os.environ.get('DB_HOST'),
    'port': os.environ.get('DB_PORT')
}

sqlite_db_path = './db.sqlite'


def test__film_work_count():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute('SELECT count(*) FROM film_work;')
            sqlite_res = sqlite_curs.fetchone()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute('SELECT count(*) FROM content.film_work;')
        pg_res = pg_cur.fetchone()

    assert sqlite_res[0] == pg_res[0]


def test__genre_count():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute('SELECT count(*) FROM genre;')
            sqlite_res = sqlite_curs.fetchone()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute('SELECT count(*) FROM content.genre;')
        pg_res = pg_cur.fetchone()

    assert sqlite_res[0] == pg_res[0]


def test__person_count():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute('SELECT count(*) FROM person;')
            sqlite_res = sqlite_curs.fetchone()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute('SELECT count(*) FROM content.person;')
        pg_res = pg_cur.fetchone()

    assert sqlite_res[0] == pg_res[0]


def test__genre_film_work_count():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute('SELECT count(*) FROM genre_film_work;')
            sqlite_res = sqlite_curs.fetchone()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute('SELECT count(*) FROM content.genre_film_work;')
        pg_res = pg_cur.fetchone()

    assert sqlite_res[0] == pg_res[0]


def test__person_film_work_count():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute('SELECT count(*) FROM person_film_work;')
            sqlite_res = sqlite_curs.fetchone()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute('SELECT count(*) FROM content.person_film_work;')
        pg_res = pg_cur.fetchone()

    assert sqlite_res[0] == pg_res[0]


def test__film_work_data():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute(
                'SELECT id, title, description, creation_date, rating, type FROM film_work;')
            sqlite_res = sqlite_curs.fetchall()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute(
            'SELECT id, title, description, creation_date, rating, type FROM content.film_work;')
        pg_res = pg_cur.fetchall()

    assert collections.Counter(sqlite_res) == collections.Counter(pg_res)


def test__genre_data():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute(
                'SELECT id, name, description FROM genre;')
            sqlite_res = sqlite_curs.fetchall()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute(
            'SELECT id, name, description FROM content.genre;')
        pg_res = pg_cur.fetchall()

    assert collections.Counter(sqlite_res) == collections.Counter(pg_res)


def test__person_data():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute(
                'SELECT id, full_name FROM person;')
            sqlite_res = sqlite_curs.fetchall()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute(
            'SELECT id, full_name FROM content.person;')
        pg_res = pg_cur.fetchall()

    assert collections.Counter(sqlite_res) == collections.Counter(pg_res)


def test__genre_film_work_data():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute(
                'SELECT id, genre_id, film_work_id FROM genre_film_work;')
            sqlite_res = sqlite_curs.fetchall()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute(
            'SELECT id, genre_id, film_work_id FROM content.genre_film_work;')
        pg_res = pg_cur.fetchall()

    assert collections.Counter(sqlite_res) == collections.Counter(pg_res)


def test__person_film_work_data():
    with sqlite3.connect(sqlite_db_path) as sqlite_conn:
        with closing(sqlite_conn.cursor()) as sqlite_curs:
            sqlite_curs.execute(
                'SELECT id, person_id, film_work_id, role type FROM person_film_work;')
            sqlite_res = sqlite_curs.fetchall()
    with psycopg2.connect(**pg_dsl) as pg_conn, pg_conn.cursor() as pg_cur:
        pg_cur.execute(
            'SELECT id, person_id, film_work_id, role FROM content.person_film_work;')
        pg_res = pg_cur.fetchall()

    assert collections.Counter(sqlite_res) == collections.Counter(pg_res)


if __name__ == '__main__':
    test__film_work_count()
    test__genre_count()
    test__person_count()
    test__genre_film_work_count()
    test__person_film_work_count()
    test__film_work_data()
    test__genre_data()
    test__person_data()
    test__genre_film_work_data()
    test__person_film_work_data()
