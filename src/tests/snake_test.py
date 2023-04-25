import unittest
import pygame
from game_objects.snake import Snake


class TestGameOver(unittest.TestCase):
    def setUp(self):
        self.snake = Snake()
        self.block_size = 30

    def test_snake_returns_the_correct_rect(self):
        position = [0, 0]
        self.assertEqual(self.snake.snake(
            position, self.block_size), pygame.Rect(0, 0, 30, 30))

    def test_snake_moves_when_no_collision_and_does_not_grow(self):
        collision = False
        snake_body = [[0, 0]]
        dx = 30
        dy = 0
        self.assertEqual(self.snake.move_snake(
            snake_body, dx, dy, collision), [[30, 0]])

    def test_snake_moves_when_collision_and_grows(self):
        collision = True
        snake_body = [[0, 0]]
        dx = 30
        dy = 0
        self.assertEqual(self.snake.move_snake(
            snake_body, dx, dy, collision), [[30, 0], [0, 0]])
