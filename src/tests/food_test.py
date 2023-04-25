import unittest
import pygame
from game_objects.food import Food


class TestGameOver(unittest.TestCase):
    def setUp(self):
        self.food = Food()
        self.screen_height = 570
        self.screen_width = 690
        self.block = 30
        self.wall_size = 15

    def test_food_returns_the_correct_rect(self):
        position = [0, 0]
        self.assertEqual(self.food.food(position), pygame.Rect(0, 0, 30, 30))

    def test_new_food_returns_correct_position(self):
        food_position = self.food.new_food()
        self.assertTrue(food_position[0] in range(self.wall_size, self.screen_width - self.block - self.wall_size)
                        and food_position[1] in range(self.wall_size, self.screen_height - self.block - self.wall_size))
