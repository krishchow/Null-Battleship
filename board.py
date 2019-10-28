import pygame
from tile import Tile
from ship import ShipAbstract
from util.enums import Direction
from typing import List

class Board:
    grid : List[List[Tile]]

    def __init__(self, player):
        #TODO: Integrate Tile Class
        self.grid = [[Tile(player) for x in range(8)] for y in range(8)]
        self.player = player
        
    def get_view(self, screen, target_player):        
        for row in range(8):
            for column in range(8):
                xpos = (self.board_params["margin"] + self.board_params["cell_width"]) * column + self.board_params["margin"]                
                ypos = (self.board_params["margin"] + self.board_params["cell_height"]) * row + self.board_params["margin"]
                self.grid[column][row].render(screen, xpos,ypos, target_player)
        
    def add_ship(self, row: int, column: int, direction: Direction,
                 ship: ShipAbstract):                                 ###Review this method, tramslate dimensions of ship onto grid
        for i in range(self.grid):
            for j in range(self.grid[i]):
                if self.grid[i][j] != self.player:
                    self.grid[i][j] = self.player

    def add_attack(self, row: int, column: int):
        for i in range(self.grid):
            for j in range(self.grid[i]):
                if self.grid[i][j] == self.player:
                    return True
