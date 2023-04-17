import unittest
import pygame
from draw_objects import DrawObjects


class TestDrawObjects(unittest.TestCase):
    def setUp(self):
        self.screen_height = 10
        self.screen_width = 10
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.draw_objects = DrawObjects()

    def test_drawing_screen_works_correctly(self):
        self.draw_objects.draw_screen(self.screen)
        self.assertEqual(self.screen.get_at((0, 0)), (0, 0, 0))
