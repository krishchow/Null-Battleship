from model.board import Board
import pygame
from model.ship import ShipAbstract


class Player:
    icon: pygame.Surface     # initialized use of image for object

    def __init__(self, name: str):
        self.name = name
        self.credits = 5
        self.number_of_ships = 0
        self.board = Board(self)

    def deduct_cost(self, cost):
        self.credits -= cost

    def is_done(self) -> bool:
        return self.credits == 0

    def add_ship(self, row, col, direction, ship: ShipAbstract) -> None:
        # while row pygame.font.init()
        #  need input verification, parsing and then passed to player board
        if self.credits >= ship.cost:
            if self.board.add_ship(row, col, direction, ship):
                self.credits -= ship.cost
                self.number_of_ships += 1
                return True
        return False

    def add_attack(self, row, col) -> None:
        if self.board.add_attack(row, col):
            if self.board.is_sunk(row, col):
                self.number_of_ships -= 1
            return True
        return False

    def add_scout(self, row, col) -> None:
        return self.board.add_scout(row, col)

    def __str__(self):
        return self.name
