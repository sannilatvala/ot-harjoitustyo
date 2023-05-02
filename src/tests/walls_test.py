import unittest
import pygame
from entities.walls import Walls


class TestWalls(unittest.TestCase):
    def setUp(self):
        self.walls = Walls()

    def test_walls(self):
        self.walls._screen_width = 30
        self.walls._screen_height = 30
        self.assertEqual(self.walls.walls(), [
                         (0, 0, 15, 15), (0, 15, 15, 15), (15, 0, 15, 15), (15, 15, 15, 15)])
