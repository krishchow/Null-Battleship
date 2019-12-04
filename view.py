import pygame
from utility.enums import DisplayMode
from utility.parameters import board_params
from pages.stages import Stage


class GameView:
    screen: pygame.Surface
    current_page: Stage

    def __init__(self, game):
        self.game = game
        self.current_page = None
        self._running = False        # This is to begin running the game
        self._keys_pressed = False   # sequence of keys that are pressed
        self.screen = None
        self.clock = pygame.time.Clock()

    def on_execute(self) -> None:
        """
        Run the game until the game ends.
        """

        while self._running:
            # pygame.time.wait(100)
            self.parse_events()
            self.current_page.render()
            pygame.display.update()
            #self.on_loop()
            self.clock.tick(30)
        self.on_cleanup()

    def on_init(self) -> None:
        """
        Initialize the game's screen, and begin running the game.
        """

        pygame.init()
        width, height = board_params['window_size']
        self.screen = pygame.display.set_mode((1000, 500))
        self.game.switch_stage(DisplayMode.Title)
        self._running = True

    def on_loop(self) -> None:
        """
        Check for win/lose conditions
        """
        if self.game.on_loop():
            self._running = False

    def on_cleanup(self) -> None:
        '''
        Cleanup and close game
        '''
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
