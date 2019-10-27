import pygame
from util import parameters

def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

class Button:
    def __init__(self,x,y,width,height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.bg = parameters.colors['white']
        self.fg = parameters.colors['black']

    def ifClicked(self, mouse, handler = lambda: print('clicked')):
        if self.x+self.width > mouse[0] > self.x and \
            self.y+self.height > mouse[1] > self.y:
            handler()
    
    def render(self, screen):
        pygame.draw.rect(screen, self.bg, (self.x, self.y, self.width, self.height))
        font_text = pygame.font.Font('./util/fonts/OpenSans-Bold.ttf', 20)
        
        text_surface, text_rect = text_objects(self.text, font_text, self.fg)
        
        text_rect.center = ((self.x+(self.width/2)),
                            (self.y+(self.height/2)))
        
        screen.blit(text_surface, text_rect)
        
        