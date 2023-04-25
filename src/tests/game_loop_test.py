import unittest
import pygame
from game_loop import GameLoop
from colors import Colors


class TestGameLoop(unittest.TestCase):
    def setUp(self):
        self._game_loop = GameLoop()
        self._colors = Colors()
        self._screen_height = 570
        self._screen_width = 690

    def test_game_over_conditions_touching_wall(self):
        snake_body = [[0, 0]]
        self.assertTrue(self._game_loop._game_over_conditions(snake_body))

    def test_game_over_conditions_not_touching_wall(self):
        snake_body = [[30, 30]]
        self.assertFalse(self._game_loop._game_over_conditions(snake_body))

    def test_game_over_conditions_touching_snake_body(self):
        snake_body = [[135, 255], [105, 255], [75, 255], [45, 255], [135, 255]]
        self.assertTrue(self._game_loop._game_over_conditions(snake_body))

    def test_game_over_conditions_not_touching_snake_body(self):
        snake_body = [[135, 255], [105, 255], [75, 255], [45, 255]]
        self.assertFalse(self._game_loop._game_over_conditions(snake_body))
