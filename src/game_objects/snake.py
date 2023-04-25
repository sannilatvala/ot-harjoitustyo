import pygame
from colors import Colors


class Snake:
    def __init__(self):
        self._colors = Colors()

    def snake(self, position, block_size):
        rect = pygame.Rect(position[0], position[1], block_size, block_size)
        return rect

    def move_snake(self, snake_body, change_x, change_y, collision):
        old_head = snake_body[0]
        new_x = old_head[0] + change_x
        new_y = old_head[1] + change_y
        new_head = [new_x, new_y]
        snake_body.insert(0, new_head)
        if not collision:
            snake_body.pop()

        return snake_body

    def draw_snake(self, screen, block_size, snake_body):
        for position in snake_body:
            snake = self.snake(position, block_size)
            pygame.draw.rect(
                screen, self._colors.medium_slate_blue(), snake)
