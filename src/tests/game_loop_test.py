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

    def test_check_food_collision_true(self):
        snake_body = [[0, 0]]
        food_position = [0, 0]
        self.assertTrue(self._game_loop._check_food_collision(
            snake_body, food_position))

    def test_check_food_collision_false(self):
        snake_body = [[0, 0]]
        food_position = [30, 0]
        self.assertFalse(self._game_loop._check_food_collision(
            snake_body, food_position))

    def test_set_new_snake_position_right(self):
        self._game_loop._direction = "RIGHT"
        self._game_loop._set_new_snake_position()
        self.assertEqual((self._game_loop._dx, self._game_loop._dy), (30, 0))

    def test_set_new_snake_position_left(self):
        self._game_loop._direction = "LEFT"
        self._game_loop._set_new_snake_position()
        self.assertEqual((self._game_loop._dx, self._game_loop._dy), (-30, 0))

    def test_set_new_snake_position_up(self):
        self._game_loop._direction = "UP"
        self._game_loop._set_new_snake_position()
        self.assertEqual((self._game_loop._dx, self._game_loop._dy), (0, -30))

    def test_set_new_snake_position_down(self):
        self._game_loop._direction = "DOWN"
        self._game_loop._set_new_snake_position()
        self.assertEqual((self._game_loop._dx, self._game_loop._dy), (0, 30))

    def test_change_direction_right(self):
        self._game_loop._change_direction_to = "RIGHT"
        self._game_loop._direction = "RIGHT"
        self._game_loop._change_direction()
        self.assertEqual(self._game_loop._direction, "RIGHT")

    def test_change_direction_left(self):
        self._game_loop._change_direction_to = "LEFT"
        self._game_loop._direction = "LEFT"
        self._game_loop._change_direction()
        self.assertEqual(self._game_loop._direction, "LEFT")

    def test_change_direction_up(self):
        self._game_loop._change_direction_to = "UP"
        self._game_loop._direction = "UP"
        self._game_loop._change_direction()
        self.assertEqual(self._game_loop._direction, "UP")

    def test_change_direction_down(self):
        self._game_loop._change_direction_to = "DOWN"
        self._game_loop._direction = "DOWN"
        self._game_loop._change_direction()
        self.assertEqual(self._game_loop._direction, "DOWN")
