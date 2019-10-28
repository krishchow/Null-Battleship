import pygame
from pygame import Surface
from pygame.locals import QUIT
from util.enums import DisplayMode
from board import Board
from player import Player
from util import parameters
from util.viewSupport import *
from textbox.pygame_textinput import TextInput

class GameView:
    screen: Surface

    def __init__(self, game):
        self.game = game
        self.board = game.current_board()
        self.currentMode = None
        self._running = False        # This is to begin running the game
        self._keys_pressed = False   #sequence of keys that are pressed
        self.screen = None
        self.clock = pygame.time.Clock()
        self.clickables = []
        self.images = []
        self.events = None
        self.switch_stage(DisplayMode.Title)
        
    def title_screen(self):
        for i in self.images:
            i.render(self.screen)

        for c in self.clickables:
            c.render(self.screen)
    
    def selection_screen(self):
        self.screen.fill(parameters.colors["white"])
        if self.tb.update(self.events):
            pass
        self.screen.blit(self.tb.get_surface(), (10, 460))
    
    def bot_selection_screen(self):
        self.screen.fill(parameters.colors["white"])

    def game_screen(self):
        self.screen.fill(parameters.colors["grey"])

    def winner(self):
        raise NotImplementedError

    def is_over(self):
        raise NotImplementedError

    def switch_stage(self, newStage: DisplayMode):
        self.clickables = []
        self.images = []
        if newStage == DisplayMode.Title:    
            button = Button(300,280, 200,60, 'Player V Player')
            button.handler = lambda x=self: x.switch_stage(DisplayMode.Selection)
            button2 = Button(300,360, 200,60, 'Player V AI')
            button2.handler = lambda x=self: x.switch_stage(DisplayMode.BotSelection)
            self.clickables.append(button)
            self.clickables.append(button2)
            self.images.append(MyImage(0,0, "sprites/island.jpg"))
            self.images.append(MyImage(600,0, "sprites/pirate.png"))
            self.images.append(MyImage(30,60, "sprites/battleship.png"))
            self.currentMode = newStage
        elif newStage == DisplayMode.Selection:
            self.currentMode = newStage
            self.tb = TextInput(initial_string="First Ship (Integer): ")
             
        elif newStage == DisplayMode.BotSelection:
            self.currentMode = newStage
        elif newStage == DisplayMode.Gameplay:
            self.currentMode = newStage
        else:
            self.currentMode = newStage

    def on_execute(self)-> None:
        """
        Run the game until the game ends.
        """

        while self._running:
            #pygame.time.wait(100)
            self.events = pygame.event.get()
            for event in self.events:
                self.on_event(event)
            #self.on_loop()
            self.on_render()
            self.clock.tick(30)
        self.on_cleanup()

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        #self.screen = pygame.display.set_mode \
        #    (self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self.screen = pygame.display.set_mode((1000, 500))
        self._running = True

    def on_event(self, event: pygame.event) -> None:
        """
        React to the given <event> as appropriate.
        """

        if event.type == pygame.QUIT:
            self._running = False
        elif self.currentMode == DisplayMode.Gameplay:
            if event.type == pygame.MOUSEBUTTONDOWN:
                handleMouseDown(self)
        elif self.currentMode == DisplayMode.Title:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in self.clickables:
                    i.ifClicked(pygame.mouse.get_pos())
        elif self.currentMode == DisplayMode.Selection:
            pass


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
        elif self.currentMode == DisplayMode.BotSelection:
            self.bot_selection_screen()
        elif self.currentMode == DisplayMode.Gameplay:
            self.game_screen()
        else:
            self.is_over()
        pygame.display.update()
    
    def on_cleanup(self) -> None:
        pygame.quit()

    def play(self):
        self.on_init()
        self.on_execute()

def handleMouseDown(view: GameView) -> None:
    pos = pygame.mouse.get_pos()

    # Change the x/y screen coordinates to grid coordinates

    column = pos[0] // (parameters.board_params["cell_width"] + parameters.board_params["margin"])
    row = pos[1] // (parameters.board_params["cell_height"] + parameters.board_params["margin"])

    # Set that location to True
    board = view.game.current_board()
    board.grid[row][column].is_hit = True
    print(board.grid)
    print ('Click ', pos, 'Grid coordinates: ', row, column)