import os
import pygame
from sprites.snake import Snake
from sprites.food import Food
from colors import Colors
from start_button import StartButton


class DrawObjects:
    def __init__(self):
        self._snake = Snake()
        self._food = Food()
        self._colors = Colors()
        self._start_button = StartButton()

    def draw_screen(self, screen):
        screen.fill(self._colors.black())

    def draw_start_button(self, screen):
        screen.blit(self._start_button.start_button(), (0, 0))

    def draw_game_instructions(self, screen):
        position_x = 0
        position_y = 90
        font = pygame.font.SysFont("Comic Sans MS", 20)
        instructions = []
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, "..", "data", "game_instructions.txt")
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                text = font.render(line.strip(), True, self._colors.white())
                instructions.append(text)
        for text in instructions:
            screen.blit(text, (position_x, position_y))
            position_y += 30

    def draw_walls(self, wall_size, screen, screen_height, screen_width):
        for row in range(screen_width//wall_size):
            for column in range(screen_height//wall_size):
                if (row == 0 or column == 0 or row == screen_width//wall_size-1
                        or column == screen_height//wall_size-1):
                    square = (row * wall_size, column *
                              wall_size, wall_size, wall_size)
                    screen.fill(self._colors.grey(), square)

    def draw_food(self, screen, food_position):
        food = self._food.food(food_position)
        pygame.draw.rect(screen, self._colors.white(), food)

    def draw_snake(self, screen, block, snake_body):
        for position in snake_body:
            snake = self._snake.snake(position, block)
            pygame.draw.rect(
                screen, self._colors.medium_slate_blue(), snake)

        pygame.display.flip()
