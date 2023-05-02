import os
import pygame
from colors import Colors
from ui.game_buttons.start_button import StartButton
from ui.create_screen import CreateScreen
from repositories.high_score_repository import HighScoreRepository


class StartView:
    """Pelin aloituksesta vastaava näkymä."""

    def __init__(self):
        """Luokan konstruktori.
        """

        self._colors = Colors()
        self._start_button = StartButton()
        self._create_screen = CreateScreen()
        self._screen = None
        self._running = True
        self._input_text = ""
        self._active = False

    def draw_start_screen(self):
        """Alustaa aloitusnäkymän.
        """

        self._screen = self._create_screen.create_screen()

        self._draw_screen(self._screen)

        font = pygame.font.SysFont("Comic Sans MS", 30)

        input_rect = pygame.Rect(250, 400, 150, 50)

        while self._running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._running = False

                if self._draw_username_input(self._screen, event, font, input_rect):
                    HighScoreRepository().create_user(self._input_text)
                    return self._input_text

                self._draw_username_text(self._screen)

                self._draw_start_button()

                self._draw_game_instructions()

                pygame.display.flip()

    def _draw_screen(self, screen):
        screen.fill(self._colors.black())

    def _draw_start_button(self):
        self._screen.blit(self._start_button.start_button(), (0, 0))

    def _draw_game_instructions(self):
        position_x = 0
        position_y = 90
        font = pygame.font.SysFont("Comic Sans MS", 20)
        instructions = []
        dirname = os.path.dirname(__file__)
        filepath = os.path.join(dirname, "game_instructions.txt")
        try:
            with open(filepath, "r", encoding="utf-8") as file:
                for line in file:
                    text = font.render(line.strip(), True,
                                       self._colors.white())
                    instructions.append(text)
            for text in instructions:
                self._screen.blit(text, (position_x, position_y))
                position_y += 30
        except FileNotFoundError:
            pass

    def _draw_username_text(self, screen):
        font = pygame.font.SysFont("Comic Sans MS", 30)
        text = font.render(
            "Username:", True, self._colors.white())

        screen.blit(text, (260, 350))

    def _draw_red_username(self, screen):
        font = pygame.font.SysFont("Comic Sans MS", 30)

        text = font.render(
            "Username:", True, self._colors.red())

        screen.blit(text, (260, 350))

        pygame.display.flip()

        pygame.time.delay(200)

    def _draw_username_already_exists(self, screen):

        font = pygame.font.SysFont("Comic Sans MS", 20)

        text = font.render(
            "Username already exists", True, self._colors.red())

        screen.blit(text, (240, 460))

        pygame.display.flip()

        pygame.time.delay(500)

    def _draw_username_input(self, screen, event, font, input_rect):

        if self._input_text:
            if self._start_button.position(event):
                if HighScoreRepository().check_if_username_exist(self._input_text):
                    self._running = False
                    return True
                else:
                    self._draw_username_already_exists(screen)

        if self._start_button.position(event) and not self._input_text:
            self._draw_red_username(screen)

        self._start_button.clicked = False

        self._check_events(event, input_rect)

        if self._active:
            color = self._colors.grey()
        else:
            color = self._colors.white()

        screen.fill(self._colors.black())

        pygame.draw.rect(screen, color, input_rect)

        text = font.render(
            self._input_text, True, self._colors.black())

        screen.blit(text, (input_rect.x + 5, input_rect.y + 5))

        input_rect.w = max(200, text.get_width() + 10)

    def _check_events(self, event, input_rect):
        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            if input_rect.collidepoint(position):
                self._active = True
            else:
                self._active = False

        if event.type == pygame.KEYDOWN and self._active:
            if event.key == pygame.K_BACKSPACE:
                self._input_text = self._input_text[:-1]
            else:
                if event.unicode.isalnum() and len(self._input_text) < 10:
                    self._input_text += event.unicode
