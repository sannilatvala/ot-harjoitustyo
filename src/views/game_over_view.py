import pygame
from colors import Colors
from game_buttons.end_game_button import EndGameButton
from game_buttons.new_game_button import NewGameButton
from views.create_screen import CreateScreen


class GameOverView:
    def __init__(self):
        self._colors = Colors()
        self._end_game_button = EndGameButton()
        self._new_game_button = NewGameButton()
        self._create_screen = CreateScreen()
        self._screen_height = 570
        self._screen_width = 690
        self._screen = None

    def draw_game_over_screen(self, points):

        self._screen = self._create_screen.create_screen()

        self._draw_screen(self._screen)

        self._draw_end_game_button()

        self._draw_new_game_button()

        self._draw_game_over_text(self._screen, points)

        pygame.display.flip()

        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if self._end_game_button.position(event):
                    running = False
                if self._new_game_button.position(event):
                    running = False
                    return True

    def _draw_screen(self, screen):
        screen.fill(self._colors.black())

    def _draw_end_game_button(self):
        self._screen.blit(self._end_game_button.end_game_button(), (180, 300))

    def _draw_new_game_button(self):
        self._screen.blit(self._new_game_button.new_game_button(), (380, 300))

    def _draw_game_over_text(self, screen, points):

        font = pygame.font.SysFont("Comic Sans MS", 30)
        text = font.render(
            "Game over", True, self._colors.white())

        screen.blit(text, (270, 150))

        points = font.render(
            f"points: {points}", True, self._colors.white())

        screen.blit(points, (280, 200))
