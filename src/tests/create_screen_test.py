import unittest
import pygame
from views.create_screen import CreateScreen
from colors import Colors
from unittest.mock import patch


class TestCreateScreen(unittest.TestCase):
    def setUp(self):
        self._create_screen = CreateScreen()
        self._colors = Colors()
        self._screen_height = 570
        self._screen_width = 690

    @patch("pygame.display.set_mode")
    def test_create_screen_works(self, mock):
        mock.return_value = pygame.Surface(
            (self._screen_width, self._screen_height))
        self._screen = self._create_screen.create_screen()
        self.assertEqual(self._screen.get_width(), 690)
        self.assertEqual(self._screen.get_height(), 570)
