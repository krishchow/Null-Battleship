from util.enums import DisplayMode
import pygame
from util.viewSupport import Button, Image
from util import parameters
from textbox.pygame_textinput import TextInput


class Stage:
    def __init__(self, screen: pygame.Surface, game):
        self.clickables = []
        self.images = []
        self.screen = screen
        self.game = game

    def switch_stage(self):
        pass

    def render(self):
        raise NotImplementedError

    def handle_events(self, events):
        pass


class TStage(Stage):
    def transition(self):
        new_stage = Transiton(self.screen, self.game, self)
        self.game.switch_stage(DisplayMode.Transiton, new_page=new_stage)

    def re_enter(self):
        raise NotImplementedError


class TitlePage(Stage):
    def switch_stage(self):
        button = Button(300, 280, 200, 60, 'Player V Player')
        button.handler = \
            lambda x=self.game: x.switch_stage(DisplayMode.Selection)
        button2 = Button(300, 360, 200, 60, 'Player V AI')
        button2.handler = \
            lambda x=self.game: x.switch_stage(DisplayMode.BotSelection)
        self.clickables.append(button)
        self.clickables.append(button2)
        self.images.append(Image(0, 0, "sprites/island.jpg"))
        self.images.append(Image(600, 0, "sprites/pirate.png"))
        self.images.append(Image(30, 60, "sprites/battleship.png"))

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


class GameplayPage(TStage):
    def __init__(self, screen: pygame.Surface, game):
        super().__init__(screen, game)
        self.bg = parameters.colors['blue'] 

    def switch_stage(self):
        self.transition()

    def render(self):
        self.screen.fill(self.bg)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # handleMouseDown(self.game)
                pass
    
    def re_enter(self):
        self.game.swap_turn()


class SelectionPage(TStage):
    def __init__(self, screen: pygame.Surface, game):
        super().__init__(screen, game)
        self.stage_count = 0
        self.events = []
        self.bg = parameters.colors['lightgrey']        

    def switch_stage(self):
        self.tb = TextInput(initial_string="First Ship (Integer): ",
                            max_width=600)
        
        self.credits = Button(500, 20, 100, 30,  "credits: " +
                              str(self.game.current_player().credits))
        self.credits.bg = self.bg

    def render(self):
        self.screen.fill(self.bg)
        if self.game.current_player().is_done():
            self.stage_count+=1
            if self.stage_count < 2:
                self.transition()
            else:
                self.game.switch_stage(DisplayMode.Gameplay)

        
        self.execute_input()
        pygame.draw.rect(self.screen, parameters.colors['grey'],
                         (610, 0, 390, 500))
        self.credits.text = "credits: " + \
                            str(self.game.current_player().credits)
        self.credits.render(self.screen)
        self.game.current_board().get_view(self.screen,
                                           50, 10, self.game.current_player())
        self.screen.blit(self.tb.get_surface(), (10, 450))

    def execute_input(self):
        if self.tb.update(self.events):
            values = None
            try:
                values = self.game.parse(self.tb.get_user_text())
            except ValueError:
                values = None
            if values:
                self.game.add_ship(*values)
                self.tb.clear_user_text()
        self.events = []

    def handle_events(self, events):
        self.events = events

    def re_enter(self):
        self.game.swap_turn()
        self.events = []
        self.tb.clear_user_text()


class BotSelectionPage(TStage):
    def render(self):
        self.screen.fill(parameters.colors["lightgrey"])
        pygame.draw.rect(self.screen, parameters.colors['grey'],
                         (610, 0, 390, 500))
        self.game.current_board().get_view(self.screen,
                                           50, 10, self.game.current_player())


class GameOver(Stage):
    def render(self):
        self.screen.fill(parameters.colors["grey"])


class Transiton(Stage):
    def __init__(self, screen: pygame.Surface, game, next_stage: TStage):
        super().__init__(screen, game)
        self.next_stage = next_stage

    def render(self):
        self.screen.fill(parameters.colors["lightgrey"])

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.next_stage.re_enter()
                self.game.set_page(self.next_stage)


def handleMouseDown(game) -> None:
    pos = pygame.mouse.get_pos()

    # Change the x/y screen coordinates to grid coordinates
    width = parameters.board_params["cell_width"]
    height = parameters.board_params["cell_height"]
    margin = parameters.board_params["margin"]
    column = pos[0] // width + margin
    row = pos[1] // height + margin

    # Set that location to True
    board = game.current_board()
    board.grid[row][column].is_hit = True
    print(board.grid)
    print('Click ', pos, 'Grid coordinates: ', row, column)
