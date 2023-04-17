import pygame


class Clock:
    def __init__(self):
        self._clock = pygame.time.Clock()

    def tick(self, time):
        self._clock.tick(time)
