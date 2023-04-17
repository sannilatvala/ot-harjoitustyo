import pygame
from colors import Colors


class StartButton:
    def __init__(self):
        self.clicked = False
        self.colors = Colors()

    def start_button(self):
        font = pygame.font.SysFont("Comic Sans MS", 30)
        button = font.render(
            "START", True, self.colors.white(), self.colors.lime_green())
        return button

    def position(self):
        button_rect = self.start_button().get_rect()
        position = pygame.mouse.get_pos()
        if button_rect.collidepoint(position):
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True
        return self.clicked
