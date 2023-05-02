import pygame


class ButtonPosition:
    """Pelin painikkeista vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori.
        """

        self._clicked = False

    def check_button_position(self, event, button_rect):
        """Palauttaa tiedon painikkeen painamisesta.

        Args:
            event: kuvaa Pygame-tapahtumia.
            button_rect: 'Pygame.Rect'-objekti.

        Returns:
            Palauttaa True tai False.
        """

        position = pygame.mouse.get_pos()
        if button_rect.collidepoint(position):
            if event.type == pygame.MOUSEBUTTONDOWN:
                self._clicked = True
        return self._clicked
