from ship import ShipAbstract
import pygame
from util import parameters

class Tile:
    icon: pygame.Surface
    def __init__(self, player):
        self.current_value = None
        self.is_hit = False
        self.player = player

    def add_ship(self, ship: ShipAbstract) -> bool:
        if not self.current_value:
            self.current_value = ship
            return True
        return False

    def register_hit(self):
        if not self.is_hit:
            self.is_hit = True
            if self.current_value:
                self.current_value.register_hit()

    def render(self, screen, x, y, target):
        color = None
        #this needs to be replaced with sprites
        if self.is_hit:
            color = parameters.colors['red']
        elif target == self.player:
            if self.current_value:
                color = parameters.colors['green']
            else:
                color = parameters.colors['white']
        else:
            color = parameters.colors['white']
        pygame.draw.rect(screen,color, x, y, \
            parameters.board_params['cell_width'], parameters.board_params['cell_height'])
