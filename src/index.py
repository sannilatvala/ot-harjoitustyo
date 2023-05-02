import pygame
from ui.start_view import StartView
from game_loop import GameLoop
from database.initialize_database import initialize_database


def main():

    initialize_database()

    start_view = StartView()
    game_loop = GameLoop()
    pygame.init()

    username = start_view.draw_start_screen()

    if username:
        game_loop.start(username)


if __name__ == "__main__":
    main()
