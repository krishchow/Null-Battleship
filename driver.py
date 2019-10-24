from player import Player
from view import GameView


class Main:
    def __init__(self):
        self.player_one = Player('p1')
        self.player_two = Player('p2')
        self.view = GameView(self)

    def play(self):
        self.view.play()

    def validate_position(self, xpos, ypos) -> bool:
        possible = range(0, 8)
        return (xpos in possible and ypos in possible)


if __name__ == '__main__':
    game = Main()
    game.play()
