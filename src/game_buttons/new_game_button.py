import pygame
from colors import Colors
from game_buttons.button_position import ButtonPosition


class NewGameButton:
    def __init__(self):
        self.colors = Colors()
        self._button_position = ButtonPosition()

    def new_game_button(self):
        font = pygame.font.SysFont("Comic Sans MS", 30)
        button = font.render(
            "NEW GAME", True, self.colors.white(), self.colors.lime_green())
        return button

    def position(self, event):
        button_rect = self.new_game_button().get_rect()
        button_rect.x = 400
        button_rect.y = 300
        return self._button_position.check_button_position(
            event, button_rect)
