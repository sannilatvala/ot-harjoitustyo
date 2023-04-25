from random import randrange
import pygame
from colors import Colors


class Food:
    def __init__(self):
        self._colors = Colors()
        self._screen_width = 690
        self._screen_height = 570
        self._block_size = 30
        self._wall_size = 15

    def food(self, position):
        rect = pygame.Rect(position[0], position[1], 30, 30)
        return rect

    def new_food(self):
        food_x = randrange(self._wall_size, self._screen_width -
                           self._block_size - self._wall_size, self._block_size)
        food_y = randrange(self._wall_size, self._screen_height -
                           self._block_size - self._wall_size, self._block_size)
        food_position = [food_x, food_y]
        return food_position

    def draw_food(self, screen, food_position):
        food = self.food(food_position)
        pygame.draw.rect(screen, self._colors.white(), food)
