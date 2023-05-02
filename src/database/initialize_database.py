from database.database_connection import get_database_connection


def drop_tables(connection):
    """Poistaa tietokantataulut.

    Args: 
        connection: Tietokantayhteyden Connection-olio.
    """

    cursor = connection.cursor()

    cursor.execute("drop table if exists highscores")

    connection.commit()


def create_tables(connection):
    """Luo tietokantataulut.

    Args: 
        connection: Tietokantayhteyden Connection-olio.
    """

    cursor = connection.cursor()

    cursor.execute("""create table if not exists highscores (
                    id integer primary key, 
                    username text,
                    highscore integer)""")

    connection.commit()


def initialize_database():
    """Alustaa tietokantataulut.
    """

    connection = get_database_connection()

    create_tables(connection)
