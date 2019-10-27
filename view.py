import pygame
from pygame.locals import QUIT
from enums import DisplayMode
from board import Board
from player import Player
from sprites import parameters

class GameView:
    screen: pygame.Surface()

    def __init__(self, Game):
        self.game = Game
        self.board = game.current_board()
        self.currentMode = DisplayMode.Title
        self._running = False        # This is to begin running the game
        self._keys_pressed = False   #sequence of keys that are pressed
        self.screen = None
        self.colors = parameters.colors
        self.board_params = parameters.board_params
        self.clock = pygame.time.Clock()
        
    def title_screen(self):
        raise NotImplementedError
    
    def selection_screen(self):
        raise NotImplementedError

    def game_screen(self):
        
        self.screen.fill(self.colors["grey"])

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
            self.clock.tick(30)
        self.on_cleanup()

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        screen = pygame.display.set_mode \
            (self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        #self.display = pygame.display.set_mode((1000, 600))
        self._running = True

    def on_event(self, event: pygame.Event) -> None:
        """
        React to the given <event> as appropriate.
        """

        if event.type == pygame.QUIT:
            self._running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            handleMouseDown(self)

    def on_loop(self)-> None:                           ## FIX SELF.PLAYER with actual player once I define
        """
        Check for win/lose conditions and game keeps looping till a winner is announced
        """
        self._keys_pressed = pygame.key.get_pressed()
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

    def on_render(self) -> None:
        if self.currentMode == DisplayMode.Title:
            self.title_screen()
        elif self.currentMode == DisplayMode.Selection:
            self.selection_screen()
        elif self.currentMode == DisplayMode.Gameplay:
            self.game_screen()
        else:
            self.is_over()
        pygame.display.flip()
    
    def on_cleanup(self) -> None:
        pygame.quit()

    def play(self):
        self.on_init()
        self.on_execute()

def handleMouseDown(view: GameView) -> None:
    pos = pygame.mouse.get_pos()

    # Change the x/y screen coordinates to grid coordinates

    column = pos[0] // (view.board_params["cell_width"] + view.board_params["margin"])
    row = pos[1] // (view.board_params["cell_height"] + view.board_params["margin"])

    # Set that location to True
    board = view.game.current_board()
    board.grid[row][column].is_hit = True
    print(board.grid)
    print ('Click ', pos, 'Grid coordinates: ', row, column)