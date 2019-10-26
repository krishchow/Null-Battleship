import pygame
from tile import Tile
from ship import ShipAbstract
from enums import Direction


class Board:
    
    def __init__(self, player):
        #TODO: Integrate Tile Class
        
        self.grid = [[[] for x in range(8)] for y in range(8)]
        self.player = player
        self.colors = {
            "white": (255, 255, 255),
            "grey": (169, 169, 169),
            "green": (0, 255, 0)
        }
        self.board_params = {
            "window_size": [512,512],
            "cell_width": 55,
            "cell_height": 55,
            "margin": 5
        }
        self.screen = pygame.display.set_mode(self.board_params["window_size"])
        self.quit_flag = False
        self.clock = pygame.time.Clock()
        
    def get_view(self, target_player):
        
        pygame.init()
        
        while not self.quit_flag:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.quit_flag = True
                elif event.type == pygame.MOUSEBUTTONDOWN:

                    pos = pygame.mouse.get_pos()

                    # Change the x/y screen coordinates to grid coordinates

                    column = pos[0] // (self.board_params["cell_width"] + self.board_params["margin"])
                    row = pos[1] // (self.board_params["cell_height"] + self.board_params["margin"])

                    # Set that location to one

                    self.grid[row][column] = 1
                    print(self.grid)
                    print ('Click ', pos, 'Grid coordinates: ', row, column)

            # Set the screen background

            self.screen.fill(self.colors["grey"])

            # Draw the grid

            for row in range(8):
                for column in range(8):
                    color = self.colors["white"]
                    if self.grid[row][column] == 1:
                        color = self.colors["green"]
                    pygame.draw.rect(self.screen, color, [(self.board_params["margin"] + self.board_params["cell_width"]) * column
                                     + self.board_params["margin"], (self.board_params["margin"] + self.board_params["cell_height"]) * row
                                     + self.board_params["margin"], self.board_params["cell_width"], self.board_params["cell_height"]])

            # Limit to 60 frames per second

            self.clock.tick(60)

            # Go ahead and update the screen with what we've drawn.

            pygame.display.flip()

        # Be IDLE friendly. If you forget this line, the program will 'hang'
        # on exit.

        pygame.quit()

        
        

    def add_ship(self, row: int, column: int, direction: Direction,
                 ship: ShipAbstract):
        raise NotImplementedError

    def add_attack(self, row: int, column: int):
        raise NotImplementedError
