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
            if bool(self.current_value):
                self.current_value.register_hit()

    def register_scout(self):
        self.is_scouted = True

    def has_ship(self):
        return bool(self.current_value)

    def render(self, screen, x, y, target):
        color = None
        # this needs to be replaced with sprites
        if self.is_hit:
            if bool(self.current_value):
                color = colors['orange']
            else:
                color = colors['red']
        elif (target == self.player or self.is_scouted) and self.has_ship():
            color = colors['green']
        else:
            color = colors['white']
        if self.has_ship() and self.current_value.is_sunk:
            color = colors['black']
        pygame.draw.rect(screen, color, (x, y,
                         board_params['cell_width'],
                         board_params['cell_height']))

    def draw_image(self, screen, x, y):
        # direction = self.anchor
        pass
