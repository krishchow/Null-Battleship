from board import Board
from player import Player
from enum import Enum
from view import GameView, SelectionView


class Main:
    def __init__(self):
        self.p1 = Player()
        self.p2 = Player()
        self.view = None

    def play(self):
        raise NotImplementedError


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3
