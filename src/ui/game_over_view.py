import pygame
from colors import Colors
from ui.game_buttons.end_game_button import EndGameButton
from ui.game_buttons.new_game_button import NewGameButton
from ui.create_screen import CreateScreen
from repositories.high_score_repository import HighScoreRepository


class GameOverView:
    """Pelin lopetusnäytöstä vastaava näkymä.
    """

    def __init__(self):
        """Luokan konstruktori.
        """

        self._colors = Colors()
        self._end_game_button = EndGameButton()
        self._new_game_button = NewGameButton()
        self._create_screen = CreateScreen()
        self._screen_height = 570
        self._screen_width = 690
        self._screen = None

    def draw_game_over_screen(self, points, username):
        """Alustaa lopetusnäkymän.

        Args:
            points: muuttuja pelissä kerätyille pisteille.
            username: muuttuja käyttäjänimelle.

        Returns:
            Palautta None tai Boolean-arvon True

        """

        self._screen = self._create_screen.create_screen()

        self._draw_screen(self._screen)

        self._draw_end_game_button()

        self._draw_new_game_button()

        self._draw_game_over_text(self._screen, points)

        self._update_high_score(points, username)

        self._draw_highscores(self._screen)

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

    def _update_high_score(self, points, username):
        HighScoreRepository().update_highscore(points, username)

    def _draw_highscores(self, screen):
        font = pygame.font.SysFont("Comic Sans MS", 20)

        text = font.render(
            "High scores:", True, self._colors.white())

        screen.blit(text, (50, 70))

        highscores = HighScoreRepository().find_highest_highscores()

        y = 100

        for i in range(len(highscores)):
            highscore = font.render(
                f"{highscores[i][0]}: {highscores[i][1]}", True, self._colors.white())
            screen.blit(highscore, (50, y))
            y += 20
