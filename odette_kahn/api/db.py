import os

from flask import g
import sqlite3

DB_PATH = os.environ['DB_PATH']


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DB_PATH)

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def get_wine_properties_and_quality(wine_name, properties_names):
    conn = get_db()
    query = f"select {','.join(properties_names)} from WINE where name = '{wine_name}'"
    cursor = conn.execute(query)
    resp = list(cursor.fetchone())
    close_db()
    properties = resp[:-1]
    quality = resp[-1]
    return properties, quality
