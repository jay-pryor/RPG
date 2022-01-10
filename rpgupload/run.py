import pygame
import time
from game import Game
from pygame.locals import *
from graphics import Graphics
from pixel import Pixel
pygame.init()
game = Game()
fpsclock = pygame.time.Clock()
fps = 100

while game.running == 1:
    game.update()
    fpsclock.tick(fps)



