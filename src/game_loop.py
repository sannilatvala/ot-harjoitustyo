import pygame


class GameLoop:
    def __init__(self, snake, food, draw_objects, events,
                 clock, block, wall_size, snake_body, screen,
                 screen_height, screen_width, game_over, start_button):
        self._snake = snake
        self._food = food
        self._draw_objects = draw_objects
        self._events = events
        self._clock = clock
        self._block = block
        self._wall_size = wall_size
        self._snake_body = snake_body
        self._screen = screen
        self._screen_height = screen_height
        self._screen_width = screen_width
        self._game_over = game_over
        self._dx = 0
        self._dy = 0
        self._start_move_snake = False
        self._change_direction_to = None
        self._direction = None
        self._start_button = start_button
        self._stop = False
        self._start_game = False
        self._food_position = self._food.new_food(
            self._screen_height,
            self._screen_width,
            self._block,
            self._wall_size
        )

    def start_screen(self):
        self._draw_start_screen(self._screen)
        pygame.display.flip()
        while True:
            if self._stop:
                break
            for event in self._events.get_event():
                if event.type == pygame.QUIT:
                    self._stop = True
                if self._start_button.position():
                    self._stop = True
                    self._start_game = True
        if self._start_game:
            self.start()

    def start(self):
        while True:
            if self._game_events() is False:
                break

            self._change_direction()

            self._set_new_snake_position()

            self._check_food_collision()
            if self._game_over_conditions(
                    self._snake_body,
                    self._screen_height,
                    self._screen_width,
                    self._block,
                    self._wall_size):
                break

            self._draw_screen(self._screen)

            self._draw_walls(self._wall_size, self._screen,
                             self._screen_height, self._screen_width)

            self._draw_objects.draw_food(self._screen, self._food_position)

            self._draw_snake(self._screen, self._block, self._snake_body)

            self._clock.tick(10)

    def _game_events(self):
        for event in self._events.get_event():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self._start_move_snake = True
                    self._change_direction_to = "RIGHT"
                elif event.key == pygame.K_LEFT:
                    self._change_direction_to = "LEFT"
                elif event.key == pygame.K_UP:
                    self._change_direction_to = "UP"
                elif event.key == pygame.K_DOWN:
                    self._change_direction_to = "DOWN"
            elif event.type == pygame.QUIT:
                return False

    def _change_direction(self):
        if self._change_direction_to == "RIGHT" and self._direction != "LEFT":
            self._direction = "RIGHT"
        elif (self._change_direction_to == "LEFT" and self._direction != "RIGHT"
                and self._direction is not None):
            self._direction = "LEFT"
        elif (self._change_direction_to == "UP" and self._direction != "DOWN"
                and self._direction is not None):
            self._direction = "UP"
        elif (self._change_direction_to == "DOWN" and self._direction != "UP"
                and self._direction is not None):
            self._direction = "DOWN"

    def _set_new_snake_position(self):
        if self._direction == "RIGHT":
            self._dx = self._block
            self._dy = 0
        elif self._direction == "LEFT":
            self._dx = -self._block
            self._dy = 0
        elif self._direction == "UP":
            self._dx = 0
            self._dy = -self._block
        elif self._direction == "DOWN":
            self._dx = 0
            self._dy = self._block

    def _check_food_collision(self):
        if self._snake_body[0] == self._food_position:
            collision = True
            self._food_position = self._food.new_food(
                self._screen_height, self._screen_width, self._block, self._wall_size)
        else:
            collision = False
        if self._start_move_snake:
            self._snake_body = self._snake.move_snake(
                self._snake_body, self._dx, self._dy, collision)

    def _game_over_conditions(self, snake_body, screen_height, screen_width, block, wall_size):
        if self._game_over.is_touching_wall(snake_body, screen_height,
                                            screen_width, block, wall_size):
            return True
        if self._game_over.is_touching_snake_body(snake_body):
            return True
        return False

    def _draw_start_screen(self, screen):
        self._draw_objects.draw_screen(screen)
        self._draw_objects.draw_start_button(screen)
        self._draw_objects.draw_game_instructions(screen)

    def _draw_screen(self, screen):
        self._draw_objects.draw_screen(screen)

    def _draw_walls(self, wall_size, screen, screen_height, screen_width):
        self._draw_objects.draw_walls(
            wall_size, screen, screen_height, screen_width)

    def _draw_snake(self, screen, block, snake_body):
        self._draw_objects.draw_snake(screen, block, snake_body)
