import unittest
import pygame
from game_buttons.new_game_button import NewGameButton
from colors import Colors


class TestNewGameButton(unittest.TestCase):
    def setUp(self):
        self._new_game_button = NewGameButton()
        self._colors = Colors()
        pygame.font.init()

    def test_new_game_button_color(self):
        font = pygame.font.SysFont("Comic Sans MS", 30)
        button = self._new_game_button.new_game_button()
        button_color = button.get_at((0, 0))
        self.assertEqual(button_color, self._colors.lime_green())
