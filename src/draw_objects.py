import pygame
from sprites.snake import Snake
from colors import Colors

class DrawObjects:
    def __init__(self, screen):
        self._screen  = screen
        self._snake = Snake()
        self._colors = Colors()

    def draw_snake(self, block, snake_body):
        self._screen.fill(self._colors.black())
        for position in snake_body:
            snake = self._snake.snake(position, block)
            pygame.draw.rect(self._screen, self._colors.blue(), snake)
        
        pygame.display.flip()