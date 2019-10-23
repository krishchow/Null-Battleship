from player import Player


class Tile:
    def __init__(self, player: Player):
        self.current_value = None
        self.isHit = False
