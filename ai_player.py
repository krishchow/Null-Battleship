import queue
import random

from player import Player


class AI(Player):
    moves: queue

    def __init__(self):
        super().__init__(self, "AI Player")
        self.moves = queue.Queue

    def add_ship(self):

        raise NotImplementedError

    def search(self):
        potential_move = [[row, col] for row in range(8) for col in
                          range(8) if not self.board.grid[row][col].isHit]
        if len(potential_move) > 0:
            self.sink(potential_move[random.randint(len(potential_move))][0],
                                       [random.randint(len(potential_move))][1])
        else:
            # empty potential_moves means game is over
            return None

    def sink(self, row: int, col: int):
        if self.moves.empty():
            self.attack(row, col)
        else:
            potential_hit = self.moves.get()
            row, col = potential_hit[0], potential_hit[1]
        if self.board.grid[row][col].isHit:
            # will add adjacent tiles to moves
            for x in [-1, 1]:
                if x + row in range(8) and not self.board.grid[x + row][col].isHit:
                    self.moves.put_nowait([x + row, col])

            for y in [-1, 1]:
                if y + col in range(8) and not self.boar.grid[row][y+ol].isHit:
                    self.moves.put_nowait([row, y + col])

    def move(self):
        if self.moves.empty():
            self.search()
        else:
            self.sink(-1, -1)

    def attack(self, row: int, col: int):
        self.board.add_attack(row, col)

    def use_ability(self):
        raise NotImplementedError


