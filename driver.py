from players.ai_player import AI
from players.human import Player
from view import GameView
from model.board import Board
import model.ship as S
from utility.enums import DisplayMode
from utility.parameters import direction_map
import pages.stages as p
import re


class Main:
    def __init__(self, player_one: str, player_two: str):
        self.player_one = Player(player_one)
        self.player_two = Player(player_two)
        self.view = GameView(self)
        self.select_match = \
            re.compile(r'^([0-7])\s([0-7])\s([\d])\s([LRUDlrud])\s*$')
        self.game_match = re.compile(r'^([0-7])\s([0-7])\s*$')

    def play(self):
        # Note: Switch the 'DisplayMode' enum type before use.
        self.view.play()

    def swap_turn(self) -> None:
        self.player_one, self.player_two = self.player_two, self.player_one

    def judge(self):      ## zeina: needs to be implemented      
        '''
        Returns a tuple with the first index being the winner
        and the second index being the loser.
        '''
        if self.player_one.number_of_ships == 0:
            return (self.player_two, self.player_one)
        elif self.player_two.number_of_ships == 0:
            return (self.player_one, self.player_two)

    def game_over(self) -> bool:       #not sure if its a necessary function to have
        return (self.player_one.number_of_ships == 0 or
                self.player_two.number_of_ships == 0)

    def on_loop(self):
        if self.game_over():
            winner, loser = self.judge()


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

    def add_ship(self, row, col, direction, ship: S.ShipAbstract) -> None:
        return self.player_one.add_ship(row, col, direction, ship)

    def parse_select(self, string) -> tuple:
        match = self.select_match.match(string)
        if not bool(match):
            print("Incorrect formatting for ship placement")
            print("Make sure ROW *SPACE* COL *SPACE* SHIP ID *SPACE* DIRECTION (U or D or L or R)")
            return None
        row, col, ship_num, d_string = match.groups()
        row, col, ship_num = int(row), int(col), int(ship_num)
        direction = direction_map.get(d_string.upper(), None)
        ship = self.get_ship(ship_num)
        if not ship:
            print("Invalid Ship Number")
            return None
        return (row, col, direction, ship)

    def parse_game(self, string) -> tuple:
        match = self.game_match.match(string)
        if not bool(match):
            print("Incorrect format for ship move. Make sure ROW *SPACE* COL")
            return None
        return tuple(map(int, match.groups()))

    def make_attack(self, row, col):
        return self.other_board().add_attack(row, col)

    def make_scout(self, row, col):
        return self.other_board().add_scout(row, col)


def get_ship(ship_num: int) -> S.ShipAbstract:
    if ship_num == 5:
        return S.Carrier()
    elif ship_num == 4:
        return S.Battleship()
    elif ship_num == 3:
        return S.Cruiser()
    elif ship_num == 2:
        return S.Destroyer()
    elif ship_num == 1:
        return S.Scout()
    else:
        return None


if __name__ == '__main__':
    game = Main('Player 1', 'Player 2')
    game.play()
    game.on_execute()