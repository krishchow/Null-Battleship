from enum import Enum


class Direction(Enum):
    UP = 1
    RIGHT = 2
    DOWN = 3
    LEFT = 4


class DisplayMode(Enum):
    Title = 0
    Selection = 1
    Gameplay = 2
    GameOver = 3
    BotSelection = 4
    Transiton = 5


class AttackStage(Enum):
    Selection = 0
    Scouts = 1
    Attacks = 2