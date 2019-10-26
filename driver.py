import pygame
from player import Player
from view import GameView
from board import Board

class Main:
    def __init__(self):
        self.player_one = Player('p1')
        self.player_two = Player('p2')
        self.board = Board(self.player_one)
        self.view = GameView(self, self.player_one, self.player_two)

    def play(self):
        #Note: Switch the 'DisplayMode' enum type before use.
        self.view.play()

    def validate_position(self, xpos, ypos)-> bool:
        possible = range(0, 8)
        return (xpos in possible and ypos in possible)


if __name__ == '__main__':
    game = Main()
    game.play()

    game.on_execute()

