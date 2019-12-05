from model.tile import Tile
from model.ship import ShipAbstract
from typing import List
from utility.parameters import board_params, direction_angle
from utility import parameters
from utility.enums import Direction
import pygame


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
                self.get(row, column).render(screen,
                                             xpos + offx, ypos + offy, target)
                if self.get(row, column).anchor:
                    anchor_points.append((self.get(row, column),
                                          xpos + offx, ypos + offy))
        for point, x, y in anchor_points:
            point.draw_image(screen, x, y, target)

    def get_map_view(self, curr_screen, xpos, ypos):
        """
        xpos & ypos: represent bounding box of the maps.
        curr_screen: represents the parent view the map subiew is presented in.

        This is not so elegant, we'll need to add a method to
        handle hits/misses, your oponents board would be the
        data source for these methods
        """
        #  data source
        grid = []
        width = 20
        height = 20
        margin = 2
        for row in range(8):
            grid.append([])
            for column in range(8):
                grid[row].append(0)

        # 1's represent hits and are red
        grid[1][5] = 1
        # 2's represent misses and are blue
        grid[3][6] = 2

        # draw grid
        for row in range(8):
            for column in range(8):
                color = parameters.colors['white']
                if grid[row][column] == 1:
                    color = parameters.colors['red']
                pygame.draw.rect(curr_screen,
                                 color,
                                 [((margin + width) * column + margin)+xpos,
                                  ((margin + height) * row + margin)+ypos,
                                  width,
                                  height])
                if grid[row][column] == 2:
                    color = parameters.colors['blue']
                pygame.draw.rect(curr_screen,
                                 color,
                                 [((margin + width) * column + margin)+xpos,
                                  ((margin + height) * row + margin)+ypos,
                                  width,
                                  height])

    def is_ship(self, row, col):
        print(bool(self.get(row, col).current_value))
        return bool(self.get(row, col).current_value)

    def is_sunk(self, row, col):
        return self.is_ship(row, col) and self.get(row, col).is_sunk()

    def get(self, row, col) -> Tile:
        if self.validate_pos(row, col):
            return self.grid[row][col]

    def validate_pos(self, row, col) -> bool:
        possible = range(0, 8)
        return (col in possible and row in possible)

    def add_ship(self, row: int, column: int, direction: Direction,
                 ship: ShipAbstract):
        positions = []
        if not self.get(row, column):
            return False
        d, start, end = 0, 0, 0
        if direction == Direction.UP:
            d, start, end = -1, row, row - ship.vertical_length
        elif direction == Direction.DOWN:
            d, start, end = 1, row, row + ship.vertical_length
        elif direction == Direction.LEFT:
            ship.rotate()
            d, start, end = -1, column, column - ship.horizontal_length
        else:
            ship.rotate()
            d, start, end = 1, column, column + ship.horizontal_length

        for i in range(start, end, d):
            if direction in (Direction.DOWN, Direction.UP):
                print(i,column)
                if self.is_ship(i, column) or not self.validate_pos(i, column):
                    return False
                else:
                    positions.append((i, column))
            else:
                print(i,row)
                if self.is_ship(row, i) or not self.validate_pos(row, i):
                    return False
                else:
                    positions.append((row, i))

        for r, c in positions:
            self.get(r, c).add_ship(ship)

        self.get(row, column).anchor = direction
        return True

    def add_attack(self, row: int, column: int):
        if not self.validate_pos(row, column):
            return False
        self.grid[row][column].register_hit()
        return True

    def add_scout(self, row: int, column: int):
        if not self.validate_pos(row, column):
            return False
        self.grid[row][column].register_scout()
        return True
