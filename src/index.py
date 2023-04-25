import pygame
from views.start_view import StartView
from game_loop import GameLoop


def main():

    start_view = StartView()
    game_loop = GameLoop()
    pygame.init()

    if start_view.draw_start_screen():
        game_loop.start()


if __name__ == "__main__":
    main()
