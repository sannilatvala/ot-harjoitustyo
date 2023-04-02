import pygame

class GameLoop:
    def __init__(self, draw_objects, events, clock, move_objects, block, wall_size, snake_body, screen_height, screen_width, game_over):
        self._draw_objects = draw_objects
        self._events = events
        self._clock = clock
        self._move_objects = move_objects
        self._block = block
        self._wall_size = 15
        self._snake_body = snake_body
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._game_over = game_over
        self._dx = 0
        self._dy = 0
        self._start_move_snake = False
        self._direction = None

    def start(self):
        while True:
            if self._game_events() == False:
                break

            if self._start_move_snake == True:
                self._move_snake()

            if self._game_over_conditions_touching_wall(self._snake_body, self._screen_height, self._screen_width, self._block, self._wall_size):
                break
            
            if self._game_over_conditions_touching_snake_body(self._snake_body):
                break

            self._draw_screen(self._block, self._screen_height, self._screen_width)

            self._draw_walls(self._block, self._wall_size, self._screen_height, self._screen_width)
            
            self._draw_snake(self._block, self._snake_body)

            self._clock.tick(10)

    def _game_events(self):
        for event in self._events.get_event():
            if event.type == pygame.KEYDOWN:
                self._start_move_snake = True
                if event.key == pygame.K_RIGHT and self._direction != "LEFT":
                    self._direction = "RIGHT"
                    self._dx = self._block
                    self._dy = 0
                if event.key == pygame.K_LEFT and self._direction != "RIGHT":
                    self._direction = "LEFT"
                    self._dx = -self._block
                    self._dy = 0
                if event.key == pygame.K_UP and self._direction != "DOWN":
                    self._direction = "UP"
                    self._dx = 0
                    self._dy = -self._block
                if event.key == pygame.K_DOWN and self._direction != "UP":
                    self._direction = "DOWN"
                    self._dx = 0
                    self._dy = self._block
            elif event.type == pygame.QUIT:
                return False
    
    def _game_over_conditions_touching_wall(self, snake_body, screen_height, screen_width, block, wall_size):
        if self._game_over.is_touching_wall(snake_body, screen_height, screen_width, block, wall_size):
            return True
        return False

    def _game_over_conditions_touching_snake_body(self, snake_body):
        if self._game_over.is_touching_snake_body(snake_body):
            return True
        return False
    
    def _move_snake(self):
        self._snake_body = self._move_objects.snake_move(self._snake_body, self._dx, self._dy)

    def _draw_screen(self, block, screen_height, screen_width):
        self._draw_objects.draw_screen(block, screen_height, screen_width)

    def _draw_walls(self, block, wall_size, screen_height, screen_width):
        self._draw_objects.draw_walls(block, wall_size, screen_height, screen_width)

    def _draw_snake(self, block, snake_body):
        self._draw_objects.draw_snake(block, snake_body)