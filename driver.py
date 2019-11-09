from player import Player
from view import GameView
from board import Board
from util.enums import Direction, DisplayMode
from ship import ShipAbstract, Destroyer, Carrier, Cruiser, Battleship, Scout
import pages.Stages as p


class Main:
    def __init__(self, player_one: str, player_two: str):
        self.player_one = Player(player_one)
        self.player_two = Player(player_two)
        self.view = GameView(self)

    def play(self):
        # Note: Switch the 'DisplayMode' enum type before use.
        self.view.play()

    def swap_turn(self) -> None:
        self.player_one, self.player_two = self.player_two, self.player_one

    def current_player(self) -> Player:
        return self.player_one

    def current_board(self) -> Board:
        return self.player_one.board

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
        self.view.current_page.switch_stage()

    def set_page(self, stage: p.Stage):
        self.view.current_page = stage

    def add_ship(self, row, col, direction, ship: ShipAbstract) -> bool:
        # need input verification, parsing and then passed to player board
        if self.current_player().credits >= ship.cost:
            if self.current_board().add_ship(row, col, direction, ship):
                self.current_player().deduct_cost(ship.cost)

    def parse(self, string) -> tuple:
        values = string.split()
        if len(values) != 4:
            raise ValueError
        row, col, ship_num = int(values[0]), int(values[1]), int(values[2])
        direction = None
        if values[3] == 'L':
            direction = Direction.LEFT
        elif values[3] == 'R':
            direction = Direction.RIGHT
        elif values[3] == 'U':
            direction = Direction.UP
        elif values[3] == 'D':
            direction = Direction.DOWN
        return (row, col, direction, get_ship(ship_num))


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
    # while game is not over, keep looping through this process -> instructions
