from board import Board
from player import Player


class Main:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.b1 = Board(self.p1)
        self.b2 = Board(self.p2)
