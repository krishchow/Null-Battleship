import pygame
from util.enums import DisplayMode
import pages.Stages as p


class GameView:
    screen: pygame.Surface
    currentPage: p.Stage

    def __init__(self, game):
        self.game = game
        self.currentPage = None
        self._running = False        # This is to begin running the game
        self._keys_pressed = False   # sequence of keys that are pressed
        self.screen = None
        self.clock = pygame.time.Clock()

    def switch_stage(self, new_stage: DisplayMode):
        if new_stage == DisplayMode.Title:
            self.currentPage = p.TitlePage(self.screen, self.game)
        elif new_stage == DisplayMode.Selection:
            self.currentPage = p.SelectionPage(self.screen, self.game)
        elif new_stage == DisplayMode.BotSelection:
            self.currentPage = p.BotSelectionPage(self.screen, self.game)
        elif new_stage == DisplayMode.Gameplay:
            self.currentPage = p.GameplayPage(self.screen, self.game)
        else:
            self.currentPage = p.GameOver(self.screen, self.game)
        self.currentPage.switch_stage()

    def on_execute(self) -> None:
        """
        Run the game until the game ends.
        """

        while self._running:
            # pygame.time.wait(100)
            events = pygame.event.get()
            if events:
                self.currentPage.handle_events(events)
            self.currentPage.render()
            pygame.display.update()
            self.clock.tick(30)
        self.on_cleanup()

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
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
