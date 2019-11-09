from ship import ShipAbstract
import pygame
from util.parameters import board_params, colors


class Tile:
    icon: pygame.Surface

    def __init__(self, player):
        self.current_value = None
        self.is_hit = False
        self.is_scouted = False
        self.player = player
        self.anchor = None

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

    def register_scout(self):
        self.is_scouted = True

    def render(self, screen, x, y, target):
        color = None
        # this needs to be replaced with sprites
        if self.is_hit:
            color = colors['red']
        elif target == self.player or self.is_scouted:
            if self.current_value:
                color = colors['green']
            else:
                color = colors['white']
        else:
            color = colors['white']
        pygame.draw.rect(screen, color, (x, y,
                         board_params['cell_width'],
                         board_params['cell_height']))

    def draw_image(self, screen, x, y):
        direction = self.anchor
        pass
