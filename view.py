import pygame
from pygame import Surface
from pygame.locals import QUIT
from util.enums import DisplayMode
from board import Board
from player import Player
from util import parameters
from util.viewSupport import *
from pages.Stages import *

class GameView:
    screen: Surface
    currentPage: Stage

    def __init__(self, game):
        self.game = game
        self.board = game.current_board()
        self.currentPage = None
        self._running = False        # This is to begin running the game
        self._keys_pressed = False   #sequence of keys that are pressed
        self.screen = None
        self.clock = pygame.time.Clock()

    def switch_stage(self, new_stage: DisplayMode):
        if new_stage == DisplayMode.Title:
            self.currentPage = TitlePage(self.screen, self)
        elif new_stage == DisplayMode.Selection:
            self.currentPage = SelectionPage(self.screen, self)
        elif new_stage == DisplayMode.BotSelection:
            self.currentPage = BotSelectionPage(self.screen, self)
        elif new_stage == DisplayMode.Gameplay:
            self.currentPage = GameplayPage(self.screen, self)
        else:
            self.currentPage = GameOver(self.screen, self)
        self.currentPage.switch_stage()
    
    def on_execute(self)-> None:
        """
        Run the game until the game ends.
        """

        while self._running:
            #pygame.time.wait(100)
            events = pygame.event.get()
            if events:
                self.currentPage.handle_events(events)
            self.currentPage.render()
            pygame.display.update()
            self.clock.tick(30)
        self.on_cleanup()

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        self.screen = pygame.display.set_mode((1000, 500))
        self.switch_stage(DisplayMode.Title)
        self._running = True

    def on_loop(self)-> None:                           ## FIX SELF.PLAYER with actual player once I define
        """
        Check for win/lose conditions and game keeps looping till a winner is announced
        """
        #self._keys_pressed = pygame.key.get_pressed()
        if (player.number_of_ships == 0) and (board.player != winner()):
            print("You lose! :( Better luck next time.")
            #self._running = False
            #do not set running false right away, the user should quit the game by themselves.
        elif (player.number_of_ships != 0) and (board.player != winner()):
            print("Congradulations, you won!")
            #self._running = False
            #do not set running false right away, the user should quit the game by themselves.
        else:
            pass        
    
    def on_cleanup(self) -> None:
        pygame.quit()

    def play(self):
        self.on_init()
        self.on_execute()

