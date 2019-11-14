from board import Board
import pygame


class Player:
    icon: pygame.Surface     # initialized use of image for object

    def __init__(self, name: str):
        self.name = name
        self.credits = 15
        self.number_of_ships = 0
        self.board = Board(self)

    def deduct_cost(self, cost):
        self.credits -= cost

    def is_done(self) -> bool:
        return self.credits == 0
