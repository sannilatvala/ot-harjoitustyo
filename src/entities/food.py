from random import randrange
import pygame


class Food:
    """Ykisttäistä ruokaa kuvaava luokka.
    """

    def __init__(self):
        """Luokan kosntruktori.
        """

        self._screen_width = 690
        self._screen_height = 570
        self._block_size = 30
        self._wall_size = 15

    def food(self, position):
        """Palauttaa ruokaa vastaavan objektin.

        Args:
            position: lista, joka kuvaa ruoan sijaintia.

        Returns:
            Palauttaa 'pygame.Rect'-objektin
        """

        rect = pygame.Rect(position[0], position[1], 30, 30)
        return rect

    def new_food(self, snake_body):
        """Palauttaa uuden ruoan sijainnin.

        Returns:
            Palauttaa listan, joka kuvaa ruoan sijaintia.
        """

        food_x = randrange(self._wall_size, self._screen_width -
                           self._block_size - self._wall_size, self._block_size)
        food_y = randrange(self._wall_size, self._screen_height -
                           self._block_size - self._wall_size, self._block_size)
        food_position = [food_x, food_y]

        while food_position in snake_body:
            food_x = randrange(self._wall_size, self._screen_width -
                           self._block_size - self._wall_size, self._block_size)
            food_y = randrange(self._wall_size, self._screen_height -
                           self._block_size - self._wall_size, self._block_size)
            food_position = [food_x, food_y]

        return food_position
