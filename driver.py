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

    def validate_position(self, xpos, ypos)-> bool:
        possible = range(0, 8)
        return (xpos in possible and ypos in possible)

    def swap_turn(self) -> None:
        self.player_one,self.player_two = self.player_two, self.player_one

    def current_player(self) -> Player:
        return self.player_one

    def current_board(self) -> Board:
        return self.player_one.board

if __name__ == '__main__':
    
    #player1name = input(str("Select a username: "))
    #player2name =  input(str("Select a username: "))
    
    #game = Main(player1name, player2name)
    game = Main('k', 'c')
    game.play()
    #TO START THE GAME, SELECTED RANDOMNLY
    #choose_player = [player1, player2]
    #chosen = random.choice(choose_player)
    #print(chosen + "will start first")
    #while game is not over, keep looping through this process --> instructions

