from tile import Tile
from ship import ShipAbstract
from util.enums import Direction
from typing import List
from util.parameters import board_params


class Board:
    grid: List[List[Tile]]

    def __init__(self, player):
        # TODO: Integrate Tile Class
        self.grid = [[Tile(player) for x in range(8)] for y in range(8)]
        self.player = player
        self.width = board_params['cell_width']
        self.height = board_params['cell_height']
        self.margin = board_params['margin']

    def get_view(self, screen, target):
        for row in range(8):
            for column in range(8):
                xpos = (self.margin + self.width) * column + self.margin
                ypos = (self.margin + self.height) * row + self.margin
                self.grid[column][row].render(screen, xpos, ypos, target)

    def is_ship(self, y, x):
        return self.validate_pos(y, x) and self.grid[y][x].current_value
    
    def validate_pos(self, row, col) -> bool:
        possible = range(0, 8)
        return (col in possible and row in possible)

    def add_ship(self, row: int, column: int, direction: Direction,
                 ship: ShipAbstract):
        positons = []
        d, start, end = 0, 0, 0
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
                if not self.is_ship(i, column):
                    return False
                else:
                    positons.append((i, column))
            else:
                if not self.is_ship(row, i):
                    return False
                else:
                    positons.append((row, i))

        for i in positons:
            self.grid[i[0]][i[1]].add_ship(ship)

    def add_attack(self, row: int, column: int):
        if not self.validate_pos(row, column):
            return False
        self.grid[row][column].register_hit()

    def add_scout(self, row: int, column: int):
        if not self.validate_pos(row, column):
            return False
        self.grid[row][column].register_scout()
