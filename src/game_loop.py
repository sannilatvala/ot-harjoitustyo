import pygame
from game_over import GameOver
from entities.snake import Snake
from entities.food import Food
from ui.game_view import GameView
from ui.create_screen import CreateScreen
from ui.game_over_view import GameOverView


class GameLoop:
    """Pelin toiminnasta vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori.
        """

        self._snake_body = [[105, 255], [75, 255], [45, 255]]
        self._dx = 0
        self._dy = 0
        self._start_move_snake = False
        self._change_direction_to = None
        self._direction = None
        self._food_position = Food().new_food()
        self._points = 0

    def start(self, username):
        """Aloittaa pelin.

        Args:
            username: muuttuja käyttäjänimelle.
        """

        screen = CreateScreen().create_screen()

        running = True

        while running:

            if self._game_events() is False:
                break

            self._change_direction()

            self._set_new_snake_position()

            collision = self._check_food_collision(
                self._snake_body, self._food_position)

            if self._start_move_snake:
                self._snake_body = Snake().move_snake(
                    self._snake_body, self._dx, self._dy, collision)

            if self._game_over_conditions(self._snake_body):
                if GameOverView().draw_game_over_screen(self._points, username):
                    GameLoop().start(username)
                break

            GameView().draw_game_screen(
                screen, self._food_position, self._snake_body, self._points, username)

            clock = pygame.time.Clock()
            clock.tick(10)

    def _game_events(self):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self._start_move_snake = True
                    self._change_direction_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    self._change_direction_to = "LEFT"
                elif event.key == pygame.K_UP:
                    self._change_direction_to = "UP"
                elif event.key == pygame.K_DOWN:
                    self._change_direction_to = "DOWN"
            elif event.type == pygame.QUIT:
                return False

    def _change_direction(self):
        if self._change_direction_to == "RIGHT" and self._direction != "LEFT":
            self._direction = "RIGHT"
        elif (self._change_direction_to == "LEFT" and self._direction != "RIGHT"
                and self._direction is not None):
            self._direction = "LEFT"
        elif (self._change_direction_to == "UP" and self._direction != "DOWN"
                and self._direction is not None):
            self._direction = "UP"
        elif (self._change_direction_to == "DOWN" and self._direction != "UP"
                and self._direction is not None):
            self._direction = "DOWN"

    def _set_new_snake_position(self):
        if self._direction == "RIGHT":
            self._dx = 30
            self._dy = 0
        elif self._direction == "LEFT":
            self._dx = -30
            self._dy = 0
        elif self._direction == "UP":
            self._dx = 0
            self._dy = -30
        elif self._direction == "DOWN":
            self._dx = 0
            self._dy = 30

    def _check_food_collision(self, snake_body, food_position):
        if snake_body[0] == food_position:
            collision = True
            self._food_position = Food().new_food()
            self._points += 1
        else:
            collision = False
        return collision

    def _game_over_conditions(self, snake_body):
        if GameOver().is_touching_wall(snake_body):
            return True
        if GameOver().is_touching_snake_body(snake_body):
            return True
        return False
