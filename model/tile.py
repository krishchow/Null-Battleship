from model.ship import ShipAbstract
import pygame
from utility.parameters import board_params, colors
from utility.enums import Direction


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

    def is_sunk(self):
        return bool(self.current_value) and self.current_value.is_sunk

    def render(self, screen, x, y, target):
        color = None
        if self.is_hit:
            if bool(self.current_value) and target != self.player:
                color = colors['green']
            else:
                color = colors['red']
        elif (target == self.player and self.has_ship()):
            color = colors['green']
        elif self.is_scouted:
            color = colors['orange']
        else:
            color = colors['white']
        if self.is_sunk():
            color = colors['black']
        pygame.draw.rect(screen, color, (x, y,
                         board_params['cell_width'],
                         board_params['cell_height']))

    def draw_image(self, screen, x, y, target):
        if self.player != target or self.current_value.is_sunk:
            return
        direction = self.anchor
        angle = direction_angle[direction]
        surface = pygame.transform.rotate(self.current_value.sprite, angle)
        offsetx, offsety=0,0
        if direction == Direction.UP:
            offsety = board_params['cell_height']*(self.current_value.vertical_length-1)
        elif direction == Direction.LEFT:
            offsetx = board_params['cell_width']*(self.current_value.horizontal_length-1)
        
        screen.blit(surface, [x-offsetx, y-offsety])       