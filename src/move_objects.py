import pygame

class MoveObjects:
    def __init__(self):
        pass

    def snake_move(self, snake_body, x, y):
        head = snake_body[0]
        new_head = [head[0] + x, head[1] + y]
        snake_body.insert(0, new_head)
        snake_body.pop()
        
        return snake_body