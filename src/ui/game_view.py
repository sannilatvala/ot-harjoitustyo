import pygame
from colors import Colors
from entities.snake import Snake
from entities.food import Food
from entities.walls import Walls
from repositories.high_score_repository import HighScoreRepository


class GameView:
    """Pelin pelaamisesta vastaava näkymä.
    """

    def __init__(self):
        """Luokan konstruktori.
        """

        self._colors = Colors()
        self._snake = Snake()
        self._food = Food()
        self._walls = Walls()
        self._block_size = 30
        self._screen = None
        self._screen_height = 570
        self._screen_width = 690

    def draw_game_screen(self, screen, food_position, snake_body, points, username):
        """Alustaa pelinäkymän.

        Args:
            screen: Pygame-näyttöobjekti.
            food_position: lista joka kuvaa ruoan sijaintia näytöllä.
            snake_body: lista joka kuvaa matoa.
            points: muuttuja pelissä kerätyille pisteille.
            username: muuttuja käyttäjänimelle.
        """

        self._screen = screen

        self._draw_screen(self._screen)

        self._draw_walls()

        self._draw_food(food_position)

        self._draw_snake(snake_body)

        self._draw_points(points)

        self._draw_highscore(username)

        pygame.display.flip()

    def _draw_screen(self, screen):
        screen.fill(self._colors.black())

    def _draw_walls(self):
        walls = self._walls.walls()
        for wall in walls:
            self._screen.fill(self._colors.grey(), wall)

    def _draw_food(self, food_position):
        food = self._food.food(food_position)
        pygame.draw.rect(self._screen, self._colors.white(), food)

    def _draw_snake(self, snake_body):
        for position in snake_body:
            snake = self._snake.snake(position, self._block_size)
            pygame.draw.rect(
                self._screen, self._colors.medium_slate_blue(), snake)

    def _draw_points(self, points):
        font = pygame.font.SysFont("Comic Sans MS", 25)
        points = font.render(
            f"Points: {points}", True, self._colors.white())
        self._screen.blit(points, (525, 10))

    def _draw_highscore(self, username):
        font = pygame.font.SysFont("Comic Sans MS", 25)
        high_score = HighScoreRepository().find_by_username(username)[1]
        score = font.render(
            f"High score: {high_score}", True, self._colors.white())
        self._screen.blit(score, (50, 10))
