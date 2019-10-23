from tile import Tile
from player import Player


class Board:
    def __init__(self, player: Player):
        self.grid = [[Tile() for _ in range(8)] for _ in range(8)]


