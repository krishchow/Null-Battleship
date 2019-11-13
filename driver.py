from ai_player import AI
from player import Player
from view import GameView
from board import Board
from util.enums import Direction, DisplayMode
from ship import ShipAbstract, Destroyer, Carrier, Cruiser, Battleship, Scout
import pages.Stages as p
import re

direction_map = {
    'L': Direction.LEFT,
    'R': Direction.RIGHT,
    'D': Direction.DOWN,
    'U': Direction.UP,
}

class Main:
    def __init__(self, player_one: str, player_two: str):
        self.player_one = Player(player_one)
        self.player_two = Player(player_two)
        self.view = GameView(self)
        self.select_match = re.compile(r'^([0-7])\s([0-7])\s([0-7])\s([LRUDlrud])\s*$')
        self.game_match = re.compile(r'^([0-7])\s([0-7])\s*$')

    def play(self):
        # Note: Switch the 'DisplayMode' enum type before use.
        self.view.play()

    def swap_turn(self) -> None:
        
        self.player_one, self.player_two = self.player_two, self.player_one
        
        
    def judge(self, player_one, player_two):      ## zeina: needs to be implemented      
        '''
        Returns a list with the first index being the winner and the second index being the loser.
        '''
        results = []
        #print ("lol")
        if player_one.number_of_ships == 0:
            results.append(player_two)
            results.append(player_one)
        elif player_two.number_of_ships == 0: 
            results.append(player_one)
            results.append(player_two)
        else: 
            play()          #else keep playing 

    def game_over(self, player_one, player_two) -> bool :       #not sure if its a necessary function to have
        return (player_one.number_of_ships == 0 or player_two.number_of_ships == 0)

    def current_player(self) -> Player:
        return self.player_one

    def current_board(self) -> Board:
        return self.player_one.board

    def other_board(self) -> Board:
        return self.player_two.board

    def switch_stage(self, new_stage: DisplayMode, new_page=None):
        if new_stage == DisplayMode.Title:
            self.set_page(p.TitlePage(self.view.screen, self))
        elif new_stage == DisplayMode.Selection:
            self.set_page(p.SelectionPage(self.view.screen, self))
        elif new_stage == DisplayMode.BotSelection:
            self.set_page(p.BotSelectionPage(self.view.screen, self))
        elif new_stage == DisplayMode.Gameplay:
            self.set_page(p.GameplayPage(self.view.screen, self))
        elif new_stage == DisplayMode.Transiton:
            self.set_page(new_page)
        elif new_stage == DisplayMode.GameOver:
            self.set_page(p.GameOver(self.view.screen, self))
        elif new_stage == DisplayMode.BotGameplay:
            self.set_page(p.BotGameplayPage(self.view.screen, self))
        self.view.current_page.switch_stage()

    def set_page(self, stage: p.Stage):
        self.view.current_page = stage

    def add_ship(self, row, col, direction, ship: ShipAbstract) -> None:
        #while row pygame.font.init()
        #  need input verification, parsing and then passed to player board
        if self.current_player().credits >= ship.cost:
            if self.current_board().add_ship(row, col, direction, ship):
                self.current_player().deduct_cost(ship.cost)
    

    def parse_select(self, string) -> tuple:
        match = self.select_match.match(string)
        if not bool(match):
            print("Syntactically Incorrect")     #TODO: Zeina -- make a Stage 
            return None
        row, col, ship_num, d_string = match.groups()
        row, col, ship_num = int(row), int(col), int(ship_num)
        direction = direction_map.get(d_string.upper(), None)
        return (row, col, direction, get_ship(ship_num))

    def parse_game(self, string) -> tuple:
        match = self.game_match.match(string)
        if not bool(match):
            print("Syntactically Incorrect")        #Zeina: add stage
            return None
        return tuple(map(int, match.groups()))

    def make_attack(self, row, col):
        return self.other_board().add_attack(row, col)

    def make_scout(self, row, col):
        return self.other_board().add_scout(row, col)


def get_ship(ship_num: int) -> ShipAbstract:
    if ship_num == 5:
        return Carrier()
    elif ship_num == 4:
        return Battleship()
    elif ship_num == 3:
        return Cruiser()
    elif ship_num == 2:
        return Destroyer()
    elif ship_num == 1:
        return Scout()
    else:
        return None


if __name__ == '__main__':
    game = Main('Player 1', 'Player 2')
    game.play()
    game.on_execute()