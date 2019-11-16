import pygame
from utility import parameters


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
        self.bg = p.colors['white']
        self.fg = p.colors['black']
        self.draw_bg = True
        self.fontsize = 20
        self.font_text = \
            pygame.font.Font('./util/fonts/OpenSans-Bold.ttf', self.fontsize)

    def render(self, screen):
        if self.draw_bg:
            pygame.draw.rect(screen, self.bg,
                             (self.x, self.y, self.width, self.height))
        font_text = pygame.font.Font('./utility/fonts/OpenSans-Bold.ttf',
                                     self.fontsize)

        text_surface, text_rect = text_objects(self.text, self.font_text, self.fg)

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


class ShipDisplay:
    def __init__(self, x, y, ship):
        self.x = x
        self.y = y
        self.ship = ship
        surface = pygame.transform.rotate(ship.sprite,
                                          p.direction_angle[Direction.RIGHT])
        self.surface = surface
        self.fontsize = 20
        self.font_text = \
            pygame.font.Font('./util/fonts/OpenSans-Bold.ttf', self.fontsize)
        self.fg = p.colors['black']
        self.display_name = self.ship.name + ": " + str(self.ship.cost)

    def render(self, screen):
        screen.blit(self.surface, [self.x, self.y])

        text_surface, text_rect = \
            text_objects(self.display_name, self.font_text, self.fg)

        text_rect.x = self.x
        text_rect.y = self.y - 30

        screen.blit(text_surface, text_rect)


class Label:
    def __init__(self, x, y, width, height, text, font_size):
        self.x = x
        self.y = y
        self.text = text
        self.font_s = font_size
        self.font_text = \
            pygame.font.Font('./util/fonts/OpenSans-Bold.ttf', self.font_s)
        self.fg = p.colors['black']
        self.width = width
        self.height = height

    def render(self, screen):
        screen.blit(self.surface, [self.x, self.y])

        text_surface, text_rect = \
            text_objects(self.text, self.font_text, self.fg)

        text_rect.center = ((self.x+(self.width/2)),
                            (self.y+(self.height/2)))

        screen.blit(text_surface, text_rect)
