import pygame
from move_objects import MoveObjects

class Snake(pygame.sprite.Sprite):
    def __init__(self):
        pass
    
    def snake(self, position, block):
        rect = pygame.Rect(position[0], position[1], block, block)
        return rect