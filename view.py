import pygame
from pygame.locals import QUIT
from enums import DisplayMode


class GameView:
    def __init__(self, Game):
        self.game = Game
        self.currentMode = DisplayMode.Title

    def title_screen(self):
        raise NotImplementedError
    
    def selection_screen(self):
        raise NotImplementedError

    def game_screen(self):
        raise NotImplementedError

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
