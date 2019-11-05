import pygame
from util.enums import DisplayMode
from util.parameters import board_params
import pages.Stages as p


class GameView:
    screen: pygame.Surface
    current_page: p.Stage

    def __init__(self, game):
        self.game = game
        self.current_page = None
        self._running = False        # This is to begin running the game
        self._keys_pressed = False   # sequence of keys that are pressed
        self.screen = None
        self.clock = pygame.time.Clock()

    def switch_stage(self, new_stage: DisplayMode, new_page=None):
        if new_stage == DisplayMode.Title:
            self.current_page = p.TitlePage(self.screen, self.game)
        elif new_stage == DisplayMode.Selection:
            self.current_page = p.SelectionPage(self.screen, self.game)
        elif new_stage == DisplayMode.BotSelection:
            self.current_page = p.BotSelectionPage(self.screen, self.game)
        elif new_stage == DisplayMode.Gameplay:
            self.current_page = p.GameplayPage(self.screen, self.game)
        elif new_stage == DisplayMode.Transiton:
            self.current_page = new_page
        else:
            self.current_page = p.GameOver(self.screen, self.game)
        self.current_page.switch_stage()

    def on_execute(self) -> None:
        """
        Run the game until the game ends.
        """

        while self._running:
            # pygame.time.wait(100)
            self.parse_events()
            self.current_page.render()
            pygame.display.update()
            self.clock.tick(30)
        self.on_cleanup()

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        width, height = board_params['window_size']
        self.screen = pygame.display.set_mode((1000, 500))
        self.switch_stage(DisplayMode.Title)
        self._running = True

    def on_loop(self) -> None:
        """
        Check for win/lose conditions
        """
        raise NotImplementedError

    def on_cleanup(self) -> None:
        pygame.quit()

    def play(self):
        self.on_init()
        self.on_execute()

    def parse_events(self) -> list:
        events = pygame.event.get()
        if not events:
            return None
        events = list(events)
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
        self.current_page.handle_events(events)
