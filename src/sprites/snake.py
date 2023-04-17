import pygame


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def snake(self, position, block):
        rect = pygame.Rect(position[0], position[1], block, block)
        return rect

    def move_snake(self, snake_body, change_x, change_y, collision):
        old_head = snake_body[0]
        new_x = old_head[0] + change_x
        new_y = old_head[1] + change_y
        new_head = [new_x, new_y]
        snake_body.insert(0, new_head)
        if not collision:
            snake_body.pop()

        return snake_body
