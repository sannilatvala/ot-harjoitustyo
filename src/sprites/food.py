from random import randrange
import pygame


class Food:
    def __init__(self):
        pass

    def food(self, position):
        rect = pygame.Rect(position[0], position[1], 30, 30)
        return rect

    def new_food(self, screen_height, screen_width, block, wall_size):
        food_x = randrange(wall_size, screen_width - block - wall_size, 30)
        food_y = randrange(wall_size, screen_height - block - wall_size, 30)
        food_position = [food_x, food_y]
        return food_position
