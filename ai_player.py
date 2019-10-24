import queue
import random

from player import Player


class AI(Player):

    def __init__(self):
        super().__init__(self, "AI Player")
        self.moves = queue.Queue

    def search(self):
        potential_move = [self.board[row][col] for row in range(8) for col in
                          range(8) if not self.board[row][col].isHit]
        if len(potential_move) > 0:
            self.attack(potential_move[random.randint(len(potential_move))])
        else:
            # empty potential_moves means game is over
            return None

    def sink(self):
        potential_hit = self.moves.get()
        self.attack(potential_hit)

        # will add adjacent tiles to moves
        for x in [-1, 1]:
            pass
        for y in [-1, 1]:
            pass

    def move(self):
        if self.moves.empty():
            self.search()
        else:
            self.sink()

    def attack(self, tile):
        tile.register_hit()

    def use_ability(self):
        raise NotImplementedError
