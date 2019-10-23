from board import Board


class Player:
    def __init__(self, name: str):
        self.name = name
        self.credits = 16
        self.number_of_ships = 0
        self.board = Board(self)
