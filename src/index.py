import pygame
from game_loop import GameLoop
from events import Events
from draw_objects import DrawObjects
from clock import Clock
from game_over import GameOver
from start_button import StartButton
from sprites.snake import Snake
from sprites.food import Food


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
    game_over = GameOver()
    start_button = StartButton()
    snake = Snake()
    food = Food()
    pygame.display.set_caption("SnakeGame")
    draw_objects = DrawObjects()
    game_loop = GameLoop(snake, food, draw_objects, events, clock, block, wall_size,
                         snake_body, screen, screen_height, screen_width, game_over, start_button)
    game_loop.start_screen()


if __name__ == "__main__":
    main()
