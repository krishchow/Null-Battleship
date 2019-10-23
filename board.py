from tile import Tile
from player import Player
from ship import ShipAbstract
from driver import Direction


class Board:
    def __init__(self, player: Player):
        self.grid = [[Tile(player) for _ in range(8)] for _ in range(8)]
        self.player = player

    def add_ship(self, row: int, column: int, direction: Direction,
                 ship: ShipAbstract):
        raise NotImplementedError

    def get_view(self, target_player: Player):
        raise NotImplementedError

    def add_attack(self, row: int, column: int):
        raise NotImplementedError
