import unittest
import pygame
from views.start_view import StartView


class TestStartView(unittest.TestCase):
    def setUp(self):
        self.screen_height = 10
        self.screen_width = 10
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.start_view = StartView()

    def test_drawing_start_screen_works(self):
        self.start_view._draw_screen(self.screen)
        self.assertEqual(self.screen.get_at((0, 0)), (0, 0, 0))
