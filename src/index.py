import pygame
from game_loop import GameLoop
from events import Events
from draw_objects import DrawObjects
from clock import Clock
from colors import Colors
from move_objects import MoveObjects
from game_over import GameOver

def main():

    pygame.init()
    screen_height = 570
    screen_width = 690
    block = 30
    wall_size = 15
    screen = pygame.display.set_mode((screen_width, screen_height))
    events = Events()
    clock = Clock()
    snake_body = [[105, 255], [75, 255], [45, 255]]
    move_objects = MoveObjects()
    colors = Colors()
    game_over = GameOver()
    screen.fill(colors.black())
    pygame.display.set_caption("SnakeGame")
    draw_objects = DrawObjects(screen)
    game_loop = GameLoop(draw_objects, events, clock, move_objects, block, wall_size, snake_body, screen_height, screen_width, game_over)
    game_loop.start()

if __name__ == "__main__":
    main()