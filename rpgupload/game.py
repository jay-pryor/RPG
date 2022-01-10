import pygame
from button import Button
from graphics import Graphics
from pygame.locals import *
from art import Art
from  item import Item
from menu import Menu

class Game():
    def __init__(self):
        self.apple = Item("apple")






        ##self.box = Button(0, 0, "Box")

















        self.running = 1
        pygame.init()
        self.graphics = Graphics()




    def update(self):

        self.graphics.update()
        pygame.display.update()
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        self.graphics.draw(self.apple)







        ##self.graphics.draw(self.box)




        for i in events:
            if i.type  == pygame.KEYDOWN:
                quit()







