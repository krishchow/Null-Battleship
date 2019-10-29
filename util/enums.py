from enum import Enum


class Direction(Enum):
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3


class DisplayMode(Enum):
    Title = 0
    Selection = 1
    Gameplay = 2
    GameOver = 3
    BotSelection = 4
    Transiton = 5
