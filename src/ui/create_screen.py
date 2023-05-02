import pygame


class CreateScreen:
    """Pelinäkymästä vastaava luokka.
    """

    def __init__(self):
        self._screen_height = 570
        self._screen_width = 690
        self._screen = None

    def create_screen(self):
        """Näyttää näkymän.

        Returns:
            Palauttaa Pygame-näyttöobjektin.
        """

        pygame.display.set_caption("SnakeGame")

        self._screen = pygame.display.set_mode(
            (self._screen_width, self._screen_height))

        return self._screen
