

class Walls:
    """Pelin seiniä kuvaava luokka.
    """

    def __init__(self):
        """Luokan kosntruktori.
        """

        self._screen_width = 690
        self._screen_height = 570
        self._wall_size = 15
        self._walls = []

    def walls(self):
        """Muodostaa pelin seinät.

        Returns:
            Paluttaa listan, joka kuvaa pelin seiniä.
        """

        for row in range(self._screen_width//self._wall_size):
            for column in range(self._screen_height//self._wall_size):
                if (row == 0 or column == 0 or row == self._screen_width//self._wall_size-1
                        or column == self._screen_height//self._wall_size-1):
                    square = (row * self._wall_size, column *
                              self._wall_size, self._wall_size, self._wall_size)
                    self._walls.append(square)
        return self._walls
