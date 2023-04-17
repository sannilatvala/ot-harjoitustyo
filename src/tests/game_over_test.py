import unittest
import pygame
from game_over import GameOver


class TestGameOver(unittest.TestCase):
    def setUp(self):
        self.screen_height = 540
        self.screen_width = 660
        self.block = 30
        self.wall_size = 15
        self.game_over = GameOver()

    def test_game_over_if_touches_wall_up(self):
        snake_body = [[self.block, self.wall_size - 1]]
        self.assertTrue(self.game_over.is_touching_wall(
            snake_body, self.screen_height, self.screen_width, self.block, self.wall_size))

    def test_game_over_if_touches_wall_down(self):
        snake_body = [[self.block, self.screen_height - self.wall_size]]
        self.assertTrue(self.game_over.is_touching_wall(
            snake_body, self.screen_height, self.screen_width, self.block, self.wall_size))

    def test_game_over_if_touches_wall_left(self):
        snake_body = [[self.wall_size - 1, self.block]]
        self.assertTrue(self.game_over.is_touching_wall(
            snake_body, self.screen_height, self.screen_width, self.block, self.wall_size))

    def test_game_over_if_touches_wall_right(self):
        snake_body = [[self.screen_width -
                       self.block - self.wall_size + 1, self.block]]
        self.assertTrue(self.game_over.is_touching_wall(
            snake_body, self.screen_height, self.screen_width, self.block, self.wall_size))

    def test_game_not_over_if_not_touches_wall(self):
        snake_body = [[105, 255], [75, 255], [45, 255]]
        self.assertFalse(self.game_over.is_touching_wall(
            snake_body, self.screen_height, self.screen_width, self.block, self.wall_size))

    def test_game_over_if_touches_snake_body(self):
        snake_body = [[135, 255], [105, 255], [75, 255], [45, 255], [135, 255]]
        self.assertTrue(self.game_over.is_touching_snake_body(snake_body))

    def test_game_not_over_if_not_touches_snake_body(self):
        snake_body = [[135, 255], [105, 255], [75, 255], [45, 255]]
        self.assertFalse(self.game_over.is_touching_snake_body(snake_body))
