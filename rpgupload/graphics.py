import pygame
from button import Button
from art import Art
from pygame.locals import *
from pixel import Pixel
# 960 x 540
# 160 x 90
class Graphics():
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.horizontal = 160
        self.vertical = 90
        self.glist = []
        self.temp = []
        self.hcounter = 0
        self.vcounter = 0

        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        #pygame.draw.rect(screen, RED, a.rect)
        #pygame.display.update()

        while self.vcounter < self.vertical:
            for i in range(self.horizontal):
                self.temp.append(Pixel(i*12, self.vcounter * 12, [200, 200, 200]))


            self.glist.append(self.temp)
            self.temp = []
            self.vcounter += 1

        for i in self.glist:
            for n in i:
                pygame.draw.rect(self.screen, n.col, n.rect)







    def draw(self, object):
        if object.x == -1 or object.y == -1:
            return
        counterx = 0
        countery = 0

        for i in range(object.art.h):


            counterx = 0






            for n in range(object.art.w):
                if object.art.img_map[countery][counterx] != [0, 0, 0]:

                    self.glist[object.y + countery][object.x + counterx].col = object.art.img_map[countery][counterx]
                else:
                    pass

                counterx += 1
            countery += 1






            pass






    def update(self):
        for i in self.glist:
            for n in i:
                pygame.draw.rect(self.screen, n.col, n.rect)





















