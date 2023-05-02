

class GameOver:
    """Pelin päättymisestä vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori.
        """

        self._screen_width = 690
        self._screen_height = 570
        self._wall_size = 15
        self._block_size = 30

    def is_touching_wall(self, snake_body):
        """Palauttaa tiedon seinään törmäämisestä.

        Args:
            snake_body: lista joka kuvaa matoa.

        Returns:
            Palautta Boolean-arvon True tai False.
        """

        if (snake_body[0][0] < self._wall_size or snake_body[0][0] > self._screen_width -
                self._block_size - self._wall_size):
            return True
        if (snake_body[0][1] < self._wall_size or snake_body[0][1] > self._screen_height -
                self._block_size - self._wall_size):
            return True
        return False

    def is_touching_snake_body(self, snake_body):
        """Palauttaa tiedon matoon törmäämisestä.

        Args:
            snake_body: lista joka kuvaa matoa.

        Returns:
            Palautta Boolean-arvon True tai False.
        """

        for snake_body_part in snake_body[2:]:
            if (snake_body[0][0] == snake_body_part[0] and
                    snake_body[0][1] == snake_body_part[1]):
                return True
        return False
