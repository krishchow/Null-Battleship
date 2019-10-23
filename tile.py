from player import Player
from ship import ShipAbstract


class Tile:
    def __init__(self, player: Player, ship):
        self.current_value = None
        self.is_hit = False
        self.player = player

    def add_ship(self, ship: ShipAbstract) -> bool:
        if not self.current_value:
            self.current_value = ship
            return True
        return False

    def register_hit(self):
        if not self.is_hit:
            self.is_hit = True
            if self.current_value:
                self.current_value.register_hit()

