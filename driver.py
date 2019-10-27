import pygame
from player import Player
from view import GameView
from board import Board
import random

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
    player1name = input(str("Select a username: "))
    p1 = Player(player1name)    #create an player1 object
    player2name =  input(str("Select a username: "))
    p2 = Player(playername2)    #create an player2 object
    #TO START THE GAME, SELECTED RANDOMNLY
    choose_player = [player1, player2]
    chosen = random.choice(choose_player)
    print(chosen + "will start first")
    #while game is not over, keep looping through this process --> instructions



    game.on_execute()


