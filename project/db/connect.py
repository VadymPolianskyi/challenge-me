import psycopg2

from project.config import reader as config_reader


def open_connection_cursor():
    """ Creates connection to the PostgreSQL database server """
    print('Connecting to the PostgreSQL database...')
    conn = psycopg2.connect(**config_reader.db)
    return conn.cursor()


def open_connection():
    """ Creates connection to the PostgreSQL database server """
    print('Connecting to the PostgreSQL database...')
    return psycopg2.connect(**config_reader.db)
