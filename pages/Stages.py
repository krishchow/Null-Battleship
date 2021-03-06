from utility.enums import DisplayMode, AttackStage
from utility.view_support import Button, Image, ShipDisplay, Label
from utility import parameters
import pygame
from textbox.pygame_textinput import TextInput
import threading
import time
from players.ai_player import AI


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

    def _timed(self):
        time.sleep(1.5)
        self.transition()

    def timed_transition(self):
        t = threading.Thread(target=self._timed)
        t.start()


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
        self.images.append(Image(30, 60, "sprites/pirate_logo.png"))

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
        self.bg = parameters.colors['ocean']
        self.state = AttackStage.Selection
        self.ship = None
        self.events = []
        self.move_queue = []
        self.tb = TextInput(initial_string="CHOOSE SHIP ROW|COL: ",
                            max_width=950)
        self.selected_tile = None
    
    def switch_stage(self):
        self.transition()

    def _timed(self):
        time.sleep(1.5)
        self.transition()
        self.tb.lock = False

    def render(self):
        self.screen.fill(self.bg)
        self.game.current_board().get_view(self.screen,
                                           50, 20, self.game.current_player())
        self.game.other_board().get_view(self.screen,
                                         530, 20, self.game.current_player())
        self.execute_events()
        self.screen.blit(self.tb.get_surface(), (10, 450))

    def execute_events(self):
        if self.tb.update(self.events):
            self.parse_input()
        self.events = []

    def parse_input(self):
        values = self.game.parse_game(self.tb.get_user_text())
        if values:
            if self.state == AttackStage.Selection: self.selection_operation(values)
            elif self.state == AttackStage.Scouts: self.scout_operation(values)
            elif self.state == AttackStage.Attacks: self.attack_operation(values)

    def selection_operation(self, values):
        if not self.game.current_board().is_ship(*values) or \
                self.game.current_board().is_sunk(*values):
            return
        ship = self.game.current_board().get(*values).current_value
        self.tb.clear_user_text()
        self.sc = ship.num_scouts
        self.ac = ship.num_attacks
        self.game.current_board().get(*values).selected = True
        self.selected_tile = values
        self.swap_state()

    def scout_operation(self, values):
        if not self.game.make_scout(*values):
            return
        self.sc -= 1
        if self.sc == 0:
           self.swap_state()

    def attack_operation(self, values):
        if not self.game.make_attack(*values):
            return
        self.ac -= 1
        if self.ac == 0:
            self.swap_state()

    def swap_state(self):
        if self.sc:
            self.tb.modify_base_string('SCOUT ROW|COL: ')
            self.state = AttackStage.Scouts
        elif self.ac:
            self.tb.modify_base_string('ATTACK ROW|COL: ')
            self.state = AttackStage.Attacks
        else:
            self.state = AttackStage.Selection
            self.tb.lock = True
            self.tb.modify_base_string('CHOOSE SHIP ROW|COL: ')
            self.game.current_board().get(*self.selected_tile).selected = False
            self.selected_tile = None
            if not self.game.game_over():
                self.timed_transition()

    def handle_events(self, events):
        self.events = events

    def re_enter(self):
        self.game.swap_turn()


class BotGamePlayPage(GameplayPage):
    def __init__(self, screen: pygame.Surface, game):
        super().__init__(screen, game)

    def render(self):
        if not isinstance(self.game.current_player(), AI):
            self.screen.fill(self.bg)
            current = self.game.current_board()
            other = self.game.other_board()
            current.get_view(self.screen,
                             50, 20, self.game.current_player())
            other.get_view(self.screen,
                           530, 20, self.game.current_player())
            self.screen.blit(self.tb.get_surface(), (10, 450))
        self.execute_events()

    def execute_events(self):
        if isinstance(self.game.current_player(), AI):
            self.attack()
        else:
            if self.tb.update(self.events):
                self.parse_input()
            self.events = []

    def attack(self):
        self.game.current_player().use_ability()
        self.transition()


class SelectionPage(TStage):
    def __init__(self, screen: pygame.Surface, game):
        super().__init__(screen, game)
        self.stage_count = 0
        self.events = []
        self.bg = parameters.colors['ocean']

    def switch_stage(self):
        self.tb = TextInput(initial_string="ROW COL SHIP DIRECTION: ",
                            max_width=600)
        base_string = "credits: " + str(self.game.current_player().credits)
        self.credits = Button(500, 20, 100, 30, base_string)
        self.credits.bg = self.bg
        self.ships = []
        for index, value in enumerate(range(50, 50+(4*95) + 1, 95)):
            self.ships.append(ShipDisplay(630, value,
                              self.game.get_ship(index + 1)))

    def render(self):
        self.screen.fill(self.bg)
        if self.game.current_player().is_done():
            self.stage_count += 1
            if self.stage_count < 2:
                self.transition()
            else:
                self.game.switch_stage(DisplayMode.Gameplay)

        self.execute_input()
        pygame.draw.rect(self.screen, parameters.colors['land'],
                         (610, 0, 390, 500))
        # drawing map
        # self.game.current_board().get_map_view(self.screen, 720, 0)
        self.credits.text = "credits: " + \
                            str(self.game.current_player().credits)
        self.credits.render(self.screen)
        self.game.current_board().get_view(self.screen,
                                           50, 20, self.game.current_player())
        self.screen.blit(self.tb.get_surface(), (10, 450))
        for s in self.ships:
            s.render(self.screen)

    def execute_input(self):
        if self.tb.update(self.events):
            values = self.game.parse_select(self.tb.get_user_text())
            if not values or not self.game.add_ship(*values):
                print('Ship is out of bounds (even if coordinates are valid)')
            self.tb.clear_user_text()
        self.events = []

    def handle_events(self, events):
        self.events = events

    def re_enter(self):
        self.game.swap_turn()
        self.events = []
        self.tb.clear_user_text()


class BotGameplayPage(GameplayPage):
    pass


class BotSelectionPage(SelectionPage):
    def __init__(self, screen: pygame.Surface, game):
        super().__init__(screen, game)
        self.stage_count = 0
        self.events = []
        self.bg = parameters.colors['lightgrey']
        self.game.player_two = AI()

    def re_enter(self):
        self.events = []
        self.tb.clear_user_text()

    def render(self):
        self.screen.fill(self.bg)
        if self.game.current_player().is_done():
            self.game.player_two.ship_placement()
            self.game.switch_stage(DisplayMode.BotGameplay)

        self.execute_input()
        pygame.draw.rect(self.screen, parameters.colors['grey'],
                         (610, 0, 390, 500))
        # drawing map
        # self.game.current_board().get_map_view(self.screen, 720, 0)
        self.credits.text = "credits: " + \
                            str(self.game.current_player().credits)
        self.credits.render(self.screen)
        self.game.current_board().get_view(self.screen,
                                           50, 20, self.game.current_player())
        self.screen.blit(self.tb.get_surface(), (10, 450))
        for s in self.ships:
            s.render(self.screen)


class GameOver(Stage):
    def switch_stage(self):
        winner, loser = self.game.judge()
        self.win_text = Label(500, 40, 0, 0, winner.name + " Wins!", 60)
        self.lose_text = Label(500, 150, 0, 0, loser.name + " Loses!", 30)
        self.bg = Image(0, 0, "sprites/island.jpg")

    def render(self):
        self.bg.render(self.screen)
        self.win_text.render(self.screen)
        self.lose_text.render(self.screen)

class Transiton(Stage):
    def __init__(self, screen: pygame.Surface, game, next_stage: TStage):
        super().__init__(screen, game)
        self.next_stage = next_stage
        self.bg = Image(0, 0, "sprites/island.jpg")
        self.player = Label(200, 50, 200, 40,
                            str(game.player_two)+"'s turn", 50)
        self.instruct = Label(200, 50, 200, 130,
                              "Click anywhere to go to the next turn", 30)
        # self.pirate = Image(600, 0, "sprites/pirate.png")

    def render(self):
        self.bg.render(self.screen)
        self.player.render(self.screen)
        self.instruct.render(self.screen)
        # self.pirate.render(self.screen)

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONUP:
                self.next_stage.re_enter()
                self.game.set_page(self.next_stage)
