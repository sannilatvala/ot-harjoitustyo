import unittest
import pygame
from game_buttons.start_button import StartButton
from colors import Colors


class TestStartButton(unittest.TestCase):
    def setUp(self):
        self._start_button = StartButton()
        self._colors = Colors()
        pygame.font.init()

    def test_start_button_color(self):
        font = pygame.font.SysFont("Comic Sans MS", 30)
        button = self._start_button.start_button()
        button_color = button.get_at((0, 0))
        self.assertEqual(button_color, self._colors.lime_green())
