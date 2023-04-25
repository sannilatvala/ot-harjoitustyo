import pygame
from colors import Colors
from game_objects.snake import Snake
from game_objects.food import Food
from game_objects.walls import Walls
from views.create_screen import CreateScreen


class GameView:
    def __init__(self):
        self._colors = Colors()
        self._snake = Snake()
        self._food = Food()
        self._walls = Walls()
        self._create_screen = CreateScreen()
        self._block_size = 30
        self._screen = None

    def draw_game_screen(self, screen, food_position, snake_body, points):

        self._screen = screen

        self._draw_screen(self._screen)

        self._draw_walls()

        self._draw_food(food_position)

        self._draw_snake(snake_body)

        self._draw_points(points)

        pygame.display.flip()

    def _draw_screen(self, screen):
        screen.fill(self._colors.black())

    def _draw_walls(self):
        self._walls.draw_walls(self._screen)

    def _draw_food(self, food_position):
        self._food.draw_food(self._screen, food_position)

    def _draw_snake(self, snake_body):
        self._snake.draw_snake(self._screen, self._block_size, snake_body)

    def _draw_points(self, points):
        font = pygame.font.SysFont("Comic Sans MS", 25)
        points = font.render(
            f"POINTS {points}", True, self._colors.white())
        self._screen.blit(points, (525, 10))
