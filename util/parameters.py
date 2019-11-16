from util.enums import Direction


colors = {
    "white": (255, 255, 255),
    "grey": (169, 169, 169),
    "green": (0, 255, 0),
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "lightgrey": (210, 210, 210),
    "orange": (255, 165, 0),
    "ocean": (0, 119, 190),
    "land": (0, 148, 50)
}

board_params = {
    "window_size": (1000, 500),
    "cell_width": 50,
    "cell_height": 50,
    "margin": 1
}

direction_angle = {
    Direction.UP: 0,
    Direction.RIGHT: 270,
    Direction.DOWN: 180,
    Direction.LEFT: 90
}
