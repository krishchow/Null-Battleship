from util.enums import DisplayMode
import pygame
from util.viewSupport import Button, MyImage
from util import parameters
from textbox.pygame_textinput import TextInput

class Stage:
    def __init__(self, screen: pygame.Surface, view):
        self.clickables = []
        self.images = []
        self.screen = screen
        self.view = view
    
    def switch_stage(self):
        pass

    def render(self):
        raise NotImplementedError
    
    def handle_events(self, events):
        pass

class TitlePage(Stage):
    def switch_stage(self):
        button = Button(300,280, 200,60, 'Player V Player')
        button.handler = lambda x=self.view: x.switch_stage(DisplayMode.Selection)
        button2 = Button(300,360, 200,60, 'Player V AI')
        button2.handler = lambda x=self.view: x.switch_stage(DisplayMode.BotSelection)
        self.clickables.append(button)
        self.clickables.append(button2)
        self.images.append(MyImage(0,0, "sprites/island.jpg"))
        self.images.append(MyImage(600,0, "sprites/pirate.png"))
        self.images.append(MyImage(30,60, "sprites/battleship.png"))

    def render(self):
        for i in self.images:
            i.render(self.screen)

        for c in self.clickables:
            c.render(self.screen)
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in self.clickables:
                    i.ifClicked(pygame.mouse.get_pos())

class GameplayPage(Stage):
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                handleMouseDown(self.view)

class SelectionPage(Stage):
    def switch_stage(self):
        self.tb = TextInput(initial_string="First Ship (Integer): ")

    def render(self):
        self.screen.fill(parameters.colors["white"])
        self.screen.blit(self.tb.get_surface(), (10, 460))
    
    def handle_events(self, events):
        self.tb.update(events)

class BotSelectionPage(Stage):
    def render(self):
        self.screen.fill(parameters.colors["red"])

class GameOver(Stage):
    def render(self):
        self.screen.fill(parameters.colors["grey"])

def handleMouseDown(view) -> None:
    pos = pygame.mouse.get_pos()

    # Change the x/y screen coordinates to grid coordinates

    column = pos[0] // (parameters.board_params["cell_width"] + parameters.board_params["margin"])
    row = pos[1] // (parameters.board_params["cell_height"] + parameters.board_params["margin"])

    # Set that location to True
    board = view.game.current_board()
    board.grid[row][column].is_hit = True
    print(board.grid)
    print ('Click ', pos, 'Grid coordinates: ', row, column)