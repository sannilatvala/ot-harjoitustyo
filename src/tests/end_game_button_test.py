import unittest
import pygame
from game_buttons.end_game_button import EndGameButton
from colors import Colors


class TestEndGameButton(unittest.TestCase):
    def setUp(self):
        self._end_game_button = EndGameButton()
        self._colors = Colors()
        pygame.font.init()

    def test_end_game_button_color(self):
        font = pygame.font.SysFont("Comic Sans MS", 30)
        button = self._end_game_button.end_game_button()
        button_color = button.get_at((0, 0))
        self.assertEqual(button_color, self._colors.deep_pink())
