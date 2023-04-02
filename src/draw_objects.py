import pygame
from sprites.snake import Snake
from colors import Colors

class DrawObjects:
    def __init__(self, screen):
        self._screen  = screen
        self._snake = Snake()
        self._colors = Colors()

    def draw_screen(self, block, screen_height, screen_width):
        self._screen.fill(self._colors.black())
            
    def draw_walls(self, block, wall_size, screen_height, screen_width):
        for row in range(screen_width//wall_size):
            for column in range(screen_height//wall_size):
                if row == 0 or column == 0 or row == screen_width//wall_size-1 or column == screen_height//wall_size-1:
                    square = (row * wall_size, column * wall_size, wall_size, wall_size)
                    self._screen.fill(self._colors.grey(), square)

    def draw_snake(self, block, snake_body):
        for position in snake_body:
            snake = self._snake.snake(position, block)
            pygame.draw.rect(self._screen, self._colors.medium_slate_blue(), snake)
        
        pygame.display.flip()