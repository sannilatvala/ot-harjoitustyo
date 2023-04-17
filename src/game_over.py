

class GameOver:
    def __init__(self):
        pass

    def is_touching_wall(self, snake_body, screen_height, screen_width, block, wall_size):
        if snake_body[0][0] < wall_size or snake_body[0][0] > screen_width - block - wall_size:
            return True
        if snake_body[0][1] < wall_size or snake_body[0][1] > screen_height - block - wall_size:
            return True
        return False

    def is_touching_snake_body(self, snake_body):
        for snake_body_part in snake_body[2:]:
            if snake_body[0][0] == snake_body_part[0] and snake_body[0][1] == snake_body_part[1]:
                return True
        return False
