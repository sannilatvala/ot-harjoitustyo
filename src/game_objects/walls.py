from colors import Colors


class Walls:
    def __init__(self):
        self._colors = Colors()
        self._wall_size = 15
        self._screen_height = 570
        self._screen_width = 690

    def draw_walls(self, screen):
        for row in range(self._screen_width//self._wall_size):
            for column in range(self._screen_height//self._wall_size):
                if (row == 0 or column == 0 or row == self._screen_width//self._wall_size-1
                        or column == self._screen_height//self._wall_size-1):
                    square = (row * self._wall_size, column *
                              self._wall_size, self._wall_size, self._wall_size)
                    screen.fill(self._colors.grey(), square)
