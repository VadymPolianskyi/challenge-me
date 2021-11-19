import psycopg2

from project.config import reader as config_reader


def open_connection():
    print('Connecting to the PostgreSQL database...')
    return psycopg2.connect(**config_reader.db)


def open_connection_cursor():
    print('Cursor from Connection to the PostgreSQL database...')
    return open_connection().cursor()
