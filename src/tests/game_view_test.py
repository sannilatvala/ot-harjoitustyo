import unittest
import pygame
from views.game_view import GameView


class TestGameView(unittest.TestCase):
    def setUp(self):
        self.screen_height = 10
        self.screen_width = 10
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height))
        self.game_view = GameView()

    def test_drawing_game_screen_works(self):
        self.game_view._draw_screen(self.screen)
        self.assertEqual(self.screen.get_at((0, 0)), (0, 0, 0))
