import pygame
from pygame.locals import *
class Pixel():
    def __init__(self, x, y, col):
        self.x = x
        self.y = y
        self.col = col
        self.width = 12
        self.height = 12
        self.rect = Rect(x, y, 11, 11)

