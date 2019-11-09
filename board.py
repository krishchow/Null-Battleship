from tile import Tile
from ship import ShipAbstract
from util.enums import Direction
from typing import List
from util.parameters import board_params


class Board:
    grid: List[List[Tile]]

    def __init__(self, player):
        self.grid = [[Tile(player) for x in range(8)] for y in range(8)]
        self.player = player
        self.width = board_params['cell_width']
        self.height = board_params['cell_height']
        self.margin = board_params['margin']

    def get_view(self, screen, offx, offy, target):
        anchor_points = []
        for row in range(8):
            for column in range(8):
                xpos = (self.margin + self.width) * column + self.margin
                ypos = (self.margin + self.height) * row + self.margin
                self.grid[row][column].render(screen,
                                              xpos+offx, ypos+offy, target)
                if self.grid[row][column].anchor:
                    anchor_points.append((self.grid[row][column],
                                          xpos+offx, ypos+offy))
        for point, x, y in anchor_points:
            point.draw_image(screen, x, y)

    def is_ship(self, row, col):
        return (self.validate_pos(row, col) and
                not self.grid[row][col].current_value)

    def get(self, row, col) -> Tile:
        if self.validate_pos(row, col):
            return self.grid[row][col]

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
            ship.rotate()
            d, start, end = -1, column, column-ship.horizontal_length
        else:
            ship.rotate()
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
            self.grid.get(row,column).add_ship(ship)

        self.get(row, column).anchor = direction
        return True

    def add_attack(self, row: int, column: int):
        if not self.validate_pos(row, column):
            return False
        self.grid[row][column].register_hit()

    def add_scout(self, row: int, column: int):
        if not self.validate_pos(row, column):
            return False
        self.grid[row][column].register_scout()
