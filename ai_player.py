import queue
import random

import ship
from player import Player
from util.enums import Direction


class AI(Player):
    moves: queue

    def __init__(self):
        super().__init__(self, "AI Player")
        self.moves = queue.Queue

    def add_ship(self, new_ship: ship):
        direction = [Direction.UP, Direction.Down, Direction.RIGHT,
                     Direction.LEFT]
        while True:
            row, col = random.randint(8), random.randint(8)
            if not self.board.is_ship(row, col) and self.board.add_ship(row, col
                    , direction[random.randint(4)], new_ship):
                break

    def ship_placement(self):
        while self.credits > 0:
            choose = [ship.Destroyer, ship.Battleship, ship.Carrier, ship.Cruiser, ship.Submarine]
            chosen = choose[random.randint(len(choose))]
            if self.credits - chosen.cost >= 0:
                self.add_ship(chosen)
                self.deduct_cost(chosen.cost)

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
        if self.board.grid[row][col].is_hit:
            # will add adjacent tiles to moves
            for x in [-1, 1]:
                if x + row in range(8) and not self.board.grid[x + row][col].is_hit:
                    self.moves.put_nowait([x + row, col])

            for y in [-1, 1]:
                if y + col in range(8) and not self.board.grid[row][y + col].is_hit:
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
