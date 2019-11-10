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
        self.ships = []

    def add_ship(self, new_ship: ship):
        direction = [Direction.UP, Direction.Down, Direction.RIGHT,
                     Direction.LEFT]
        while True:
            row, col = random.randint(8), random.randint(8)
            # Try to place ship, break loop if successful
            if not self.board.is_ship(row, col) and self.board.add_ship(row, col
                    , direction[random.randint(4)], new_ship):
                break

    def ship_placement(self):
        while self.credits > 0:
            # Continuously select and place a random ship until all credits have been spent
            choose = [ship.Destroyer, ship.Battleship, ship.Carrier,
                      ship.Cruiser, ship.Submarine]
            chosen = choose[random.randint(len(choose))]
            if self.credits - chosen.cost >= 0:
                self.add_ship(chosen)
                self.deduct_cost(chosen.cost)
                self.ships.append(chosen.get_total())

    def search(self):
        # add all unhit tiles on board to list
        potential_move = [[row, col] for row in range(8) for col in
                          range(8) if not self.board.grid[row][col].isHit]

        # Randomly chose an unhit tile to attack
        if len(potential_move) > 0:
            self.sink(potential_move[random.randint(len(potential_move))][0],
                      potential_move[random.randint(len(potential_move))][1])
        else:
            # empty potential_moves means game is over
            return None

    def sink(self, row: int, col: int):
        # This is used for search mode attack
        if self.moves.empty():
            self.attack(row, col)

        # Used when AI knows general location of a ship
        else:
            potential_hit = self.moves.get()
            row, col = potential_hit[0], potential_hit[1]

        # add adjacent tiles to moves
        if self.board.grid[row][col].is_hit:
            for x in [-1, 1]:
                if x + row in range(8) and not self.board.grid[x + row][col].is_hit:
                    self.moves.put_nowait([x + row, col])
            for y in [-1, 1]:
                if y + col in range(8) and not self.board.grid[row][y + col].is_hit:
                    self.moves.put_nowait([row, y + col])

    # AI makes a move on its turn
    def move(self):
        if self.moves.empty():
            self.search()
        else:
            self.sink(-1, -1)

    def attack(self, row: int, col: int):
        self.board.add_attack(row, col)

    def scout(self):
        potential_move = [[row, col] for row in range(8) for col in
                          range(8) if not self.board.grid[row][col].isHit]
        # Randomly chose an unhit tile to attack
        if len(potential_move) > 0:
            scouted_tile = (potential_move[random.randint(len(potential_move))][0], potential_move[random.randint(len(potential_move))][1])
        else:
            # empty potential_moves means game is over
            return None
        if self.board.is_ship(scouted_tile[0], scouted_tile[1]):
            for x in [-1, 0, 1]:
                if x + scouted_tile[0] in range(8) and not self.board.grid[x + scouted_tile[0]][scouted_tile[1]].is_hit:
                    self.moves.put_nowait([x + scouted_tile[0], scouted_tile[1]])
            for y in [-1, 0, 1]:
                if y + scouted_tile[1] in range(8) and not self.board.grid[scouted_tile[0]][y + scouted_tile[1]].is_hit:
                    self.moves.put_nowait([scouted_tile[0], y + scouted_tile[1]])

    def use_ability(self):
        # Use a random one of the AI's ships' abilities
        ability = self.ships[random.randint(len(self.ships))]
        if ability == 1:
            pass
        elif ability == 2:
            self.move()
        elif ability == 3:
            for _ in range(2):
                self.move()
        elif ability == 4:
            self.move()
        elif ability == 5:
            for _ in range(3):
                self.move()
        else:
            self.move()
