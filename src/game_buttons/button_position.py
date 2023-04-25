import pygame


class ButtonPosition:
    def __init__(self):
        self._clicked = False

    def check_button_position(self, event, button_rect):
        position = pygame.mouse.get_pos()
        if button_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._clicked = True
        return self._clicked
