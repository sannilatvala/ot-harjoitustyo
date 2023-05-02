import os
import sqlite3

dirname = os.path.dirname(__file__)
filepath = os.path.join(dirname, "highscores.db")
connection = sqlite3.connect(filepath)


def get_database_connection():
    return connection
