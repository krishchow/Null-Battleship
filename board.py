from tile import Tile
from ship import ShipAbstract
from enums import Direction


class Board:
    def __init__(self, player):
        self.grid = [[Tile(player) for _ in range(8)] for _ in range(8)]
        self.player = player

    def add_ship(self, row: int, column: int, direction: Direction,
                 ship: ShipAbstract):
        raise NotImplementedError

    def get_view(self, target_player):
        raise NotImplementedError

    def add_attack(self, row: int, column: int):
        raise NotImplementedError
