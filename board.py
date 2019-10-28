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
    
    def validate_position(self, row, col)-> bool:
        possible = range(0, 8)
        return (col in possible and row in possible)

    def add_ship(self, row: int, column: int, direction: Direction,
                 ship: ShipAbstract):                                 ###Review this method, tramslate dimensions of ship onto grid
        positons = []
        d, start, end = 0,0,0
        if direction == Direction.UP:
            d, start, end = -1, row, row-ship.vertical_length
        elif direction == Direction.DOWN:
            d, start, end = 1, row, row+ship.vertical_length
        elif direction == Direction.LEFT:
            d, start, end = -1, column, column-ship.horizontal_length
        else:
            d, start, end = 1, column, column+ship.horizontal_length

        for i in range(start, end, d):
            if direction in (Direction.DOWN, Direction.UP):
                if not validate_position(i, column) or grid[i][column].current_value:
                    return False
                else:
                    positons.append((i,column))
            else:
                if not validate_position(row, i) or grid[row][i].current_value:
                    return False
                else:
                    positons.append((row,i))
        
        for i in positons:
            grid[i[0]][i[1]].add_ship(ship)

    def add_attack(self, row: int, column: int):
        if not validate_position(row,column):
            return False
        self.grid[row][column].register_hit()
    
    def add_scout(self, row: int, column: int):
        if not validate_position(row,column):
            return False
        self.grid[row][column].register_scout()

