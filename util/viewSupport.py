import pygame
from util import parameters


def text_objects(text, font, color):
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


class Clickable:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.handler = lambda: print('clicked', self)

    def ifClicked(self, mouse):
        if self.x+self.width > mouse[0] > self.x and \
           self.y+self.height > mouse[1] > self.y:
            self.handler()


class Button(Clickable):
    def __init__(self, x, y, width, height, text):
        super().__init__(x, y, width, height)
        self.text = text
        self.bg = parameters.colors['white']
        self.fg = parameters.colors['black']
        self.draw_bg = True
        self.fontsize = 20

    def render(self, screen):
        if self.draw_bg:
            pygame.draw.rect(screen, self.bg,
                             (self.x, self.y, self.width, self.height))
        font_text = pygame.font.Font('./util/fonts/OpenSans-Bold.ttf',
                                     self.fontsize)

        text_surface, text_rect = text_objects(self.text, font_text, self.fg)

        text_rect.center = ((self.x+(self.width/2)),
                            (self.y+(self.height/2)))

        screen.blit(text_surface, text_rect)


class Image:
    def __init__(self, x, y, path):
        self.asset = pygame.image.load(path)
        self.x = x
        self.y = y

    def render(self, screen):
        screen.blit(self.asset, [self.x, self.y])
