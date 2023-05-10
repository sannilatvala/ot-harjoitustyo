from database.database_connection import get_database_connection


class HighScoreRepository:
    """Parhaisiin tuloksiin liityvistä tietokantaoperaatiosta vastaava luokka.
    """

    def __init__(self):
        """Luokan kosntruktori.
        """

        self._connection = get_database_connection()

    def find_by_username(self, username):
        """Palauttaa käyttäjänimen ja käyttäjän parhaan tuloksen käyttäjätunnuksen perusteella.

        Args: 
            username: muuttuja käyttäjänimelle.

        Returns:
            Palauttaa tuplen, joka sisältää käyttäjänimen ja parhaan tuloksen, jos käyttäjänimi on 
            olemassa. Muussa tapauksessa None.
        """
        cursor = self._connection.cursor()

        user_high_score = cursor.execute("""SELECT username,
                                    highscore FROM highscores
                                    WHERE username=?""", [username]).fetchone()

        return user_high_score[0], user_high_score[1] if user_high_score else None

    def create_user(self, username):
        """Tallentaa käyttäjän tietokantaan.

        Args:
            username: muuttuja käyttäjänimelle.
        """

        cursor = self._connection.cursor()

        user = cursor.execute(
            "select * from highscores where username=?", [username]).fetchone()

        if user is None:
            self._connection.execute("""insert into highscores
                            (username, highscore) values (?, ?)""",
                                     [username, 0])

            self._connection.commit()

            return username

        return None

    def update_highscore(self, points, username):
        """Päivittää käyttäjän parasta tulosta.

        Args:
            points: muuttuja pelissä kerätyille pisteille.
            username: muuttuja käyttäjänimelle.
        """

        cursor = self._connection.cursor()

        cursor.execute(
            "select highscore from highscores where username=?", [username])

        row = cursor.fetchone()

        current_highscore = row[0] if row else 0

        if points > current_highscore:

            cursor.execute("""update highscores set
                            highscore=? where username=?""",
                           [points, username])

            self._connection.commit()

            return points

        return current_highscore

    def find_highest_highscores(self):
        """Palauttaa 5 parhainta tulosta tietokannassa.
        """

        cursor = self._connection.cursor()

        highscores = cursor.execute(
            "select username, highscore from highscores order by highscore desc limit 5").fetchall()

        return highscores

    def check_if_username_exist(self, username):
        """Tarkistaa onko käyttäjänimi jo olemassa.

        Args:
            username: muuttuja käyttäjänimelle.
        """

        cursor = self._connection.cursor()

        user = cursor.execute(
            "select * from highscores where username=?", [username]).fetchone()

        if user is None:
            return True
        else:
            return False
        
    def delete_all(self):
        """Poistaa kaikki käyttäjät ja ennätykset
        """

        cursor = self._connection.cursor()

        cursor.execute("delete from highscores")

        self._connection.commit()
