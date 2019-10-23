import pygame


class GameView:
    def __init__(self, is_bot: bool):
        self.bot_game = is_bot


class SelectionView:
    def __init__(self, is_bot: bool):
        self.bot_game = is_bot
        pygame.init()
