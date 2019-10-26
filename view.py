import pygame
from pygame.locals import QUIT
from enums import DisplayMode
from board import Board

class GameView:
    screen: Pygame.Surface()


    def __init__(self, Game, player_one, player_two):
        self.game = Game
        self.player_one = player_one
        self.player_Two = player_two
        self.board = Board(self.player_one)
        self.currentMode = DisplayMode.Gameplay
        self._running = False        # This is to begin running the game
        self._keys_pressed = False   #sequence of keys that are pressed

        
    def title_screen(self):
        raise NotImplementedError
    
    def selection_screen(self):
        raise NotImplementedError

    def game_screen(self):
        self.board.get_view(self.player_one)
    def winner(self):
        raise NotImplementedError
    def is_over(self):
        raise NotImplementedError

    def on_execute(self)-> None:
        """
        Run the game until the game ends.
        """

        self.on_init()

        while self._running:
            pygame.time.wait(100)
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()

        self.on_cleanup()

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        screen = pygame.display.set_mode \
            (self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True

    def on_event(self, event: pygame.Event) -> None:
        """
        React to the given <event> as appropriate.
        """

        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self)-> None:                                 #            ## FIX SELF.PLAYER with actual player once I define
        """
        Check for win/lose conditions and game keeps looping till a winner is announced
        """
        keys_pressed = pygame.key.get_pressed()
        if self.player == None:        ## if he has no ships print
            print("You lose! :( Better luck next time.")
            self._running = False
        elif self.player.has_won(self):
            print("Congradulations, you won!")
            self._running = False



    def play(self):
        on_init()
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
