import pygame
from player import Player
from view import GameView
from board import Board
import random

class Main:
    def __init__(self, player_one: str, player_two: str):
        self.player_one = Player(player_one)
        self.player_two = Player(player_two)
        self.view = GameView(self)

    def play(self):
        #Note: Switch the 'DisplayMode' enum type before use.
        self.view.play()

    def swap_turn(self) -> None:
        self.player_one,self.player_two = self.player_two, self.player_one

    def current_player(self) -> Player:
        return self.player_one

    def current_board(self) -> Board:
        return self.player_one.board

if __name__ == '__main__':
    
    game = Main('Player 1', 'Player 2')
    game.play()
    #TO START THE GAME, SELECTED RANDOMNLY
    #while game is not over, keep looping through this process --> instructions

