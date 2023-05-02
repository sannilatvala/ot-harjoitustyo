import pygame
from colors import Colors
from ui.game_buttons.button_position import ButtonPosition


class EndGameButton:
    """Pelin 'lopetus'-painikkeesta vastaava luokka.
    """

    def __init__(self):
        """Luokan konstruktori.
        """

        self.colors = Colors()
        self._button_position = ButtonPosition()

    def end_game_button(self):
        """Palauttaa piirrettävän 'lopetus'-painikkeen.

        Returns:
            Palauttaa 'Surface'-objektin.
        """

        font = pygame.font.SysFont("Comic Sans MS", 30)
        button = font.render(
            "END GAME", True, self.colors.white(), self.colors.deep_pink())
        return button

    def position(self, event):
        """Palauttaa tiedon painikkeen painamisesta.

        Args:
            event: kuvaa Pygame-tapahtumia.

        Returns:
            Palautta Boolean-arvon True tai False.
        """

        button_rect = self.end_game_button().get_rect()
        button_rect.x = 200
        button_rect.y = 300
        return self._button_position.check_button_position(
            event, button_rect)
