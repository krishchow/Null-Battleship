import pygame
from pygame.locals import QUIT
from enums import DisplayMode
from board import Board

class GameView:
    def __init__(self, Game, player_one, player_two):
        self.game = Game
        self.player_one = player_one
        self.player_Two = player_two
        self.board = Board(self.player_one)
        self.currentMode = DisplayMode.Gameplay
        
    def title_screen(self):
        raise NotImplementedError
    
    def selection_screen(self):
        raise NotImplementedError

    def game_screen(self):
        self.board.get_view(self.player_one)

    def is_over(self):
        raise NotImplementedError

    def play(self):
        pygame.init()
        self.display = pygame.display.set_mode((1000, 600))
        while True:
            if self.currentMode == DisplayMode.Title:
                self.title_screen()
            elif self.currentMode == DisplayMode.Selection:
                self.selection_screen()
            elif self.currentMode == DisplayMode.Gameplay:
                self.game_screen()
            else:
                self.is_over()
            pygame.display.update()
