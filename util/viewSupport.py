import pygame
from util import parameters

class Button:
    def __init__(self,x,y,width,height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def ifClicked(self, mouse):
        if self.x+self.width > mouse[0] > self.x and \
            self.y+self.height > mouse[1] > self.y:
            print('clicked', self.text)
    
    def render(self, screen):
        pygame.draw.rect(screen, parameters.colors['white'], (self.x,self.y,self.width,self.height))