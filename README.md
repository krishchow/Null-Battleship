# CSC290 - Team NULL - Pirateship

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Installing

1.) Download this repo via the `Clone or download` button or clone it via the git CLI:

```
git clone https://github.com/krishchow/Null-Battleship.git
```

2.) Once the folder is downloaded and opened ensure the requirements are installed via pip:

```
pip install -r requirements.txt
```
3.) Start the game by running `driver.py`, either manually in a python interpreter or via python CLI:

```
python driver.py
```

## Game Demo

A quick narrated playthrough of the game:

[![Pirate Ship Thumbnail](https://i.imgur.com/8Ea8Cbr.png)](http://www.youtube.com/watch?v=rlacfsHVneo "Pirate ship demo")


## Game Controls

The game is played using keyboard inputs.

```
[0-7]       Number range for board coordinates [Row, Column]
```
```
[1-5]       Number range for the game's ships
```
```
[U,D,L,R]   Letter range for choosing ship's direction [Up, Down, Left, Right]
```

**Important**: Inputs must be separated by spaces.

## Ships

The game has 5 different ships, each with their own abilities.
Players spend their credits on ships of their choosing.

|Ship Name|Ship Cost|Ship Ability|
|---------|---------|------------|
|Caravel|1| 1 Attack|
|Corvette|2| 1 Attack, 1 Scout|
|Galley|3| 1 Attack, 2 Scouts|
|Frigate|4| 2 Attacks, 1 Scout|
|Man-O-War|5| 3 Attacks|



## Built With

* [Python 3](https://www.python.org/download/releases/3.0/) - Language
* [Pygame](https://www.pygame.org/news) - Game Library

## Code Overview and Design

We have broken our code up into several key folders and classes. This is captured in the diagram below, which shows we organized the code.

### Directory
![Directory Structure](https://i.imgur.com/AJDQIJC.png)

### Model

Our model folder contains all code related the core data involved with gameplay. This means the following classes:

* Board - The Board is the primary representation of the game's current state, and it mainly contains pointers to 64 Tile objects, each of which maintains the current state of an individual tile.
* Ship - The Ship abstract class and it's implementations, each of which represents one of the possible ships a player might place on their board.
* Tile - The Tile class maintains all information about a specific tile, and also contains a pointer to the Ship object currently on that Tile (if there is one).

These classes interact with each other through a variety of functions defined in the Board class. The Board class is responsible for maintaining the overall state of a player's Board and allowing for standard operations on that board, such as placing a ship, making an attack or scout on that ship and reporting if all ships are sunk.

### View

The view code is all captured in the view, view_support and stages files. There are several key classes, such as Stage, GameView, Clickable, ShipDisplay and Button.

* GameView - This is the central class responsible for running the view and performing the core parsing
* Stage - The Stage abstract class is the class responsible for rendering and handling input from any stage in the game
* ShipDisplay - The ShipDisplay is used to render the Ship sprites in the Ship Selection Stage.
* Label - The Label is a common class used in various stages, which renders some dynamic text
* Image - The Image is also a common class used for rendering an Image at some coordinates
* Button - The Button is a Clickable object which calls a handler function when it is clicked.

The primary interaction is between the Controller and the Stages. At a high level, the stages can be dynamically swaped when going between different game states. This allows for a cleaner and more extensible page structure.

Each stage encapsulates one specific game function, and calls on the appropriate helper functions where required. Options like background color, image sizes, button locations and display text can all be found in the appropiate stage for the game state.

### Controller

The driver is the file which must be executed to run this application. The Main class is responsible for coordinating the view and the model. It also provides critical parsing functionality which is used by the various stages. The controller also checks if win conditions are met and handles Ship building.

## Contributing

The first step to contribute to this project would be to clone the GitHub repository, and install the prerequisite software.

In order to contribute to this project, we encourage you to first read the existing code base. This should provide with an understanding of the various code components and logic behind the model. From here, you can begin working on your additional features, while making use of the existing helper functions. Please ensure that all new code conforms to the flake8 style standard.

After finishing your code features, please create a pull request on GitHub. You can find a great guide for how to create a [Pull Request here](https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/creating-a-pull-request).

### Extending Pirateship

Pirateship is a user-friendly interactive game that the public can extend in order to add features and personalize game aspects which will enhance the experience of a childhood favourite playdown. Don’t know where to start? The following are examples that an individual can incorporate in order to extend the game:

    Obstacles that increase the difficulty of the board configuration when players select the location of their ship on the map. For example, particular areas within the board boundaries can be set as island or rock objects.

    Different and personalized themed maps, ships and game graphics. For example, as opposed to the traditional battleship and Pirateship, one can choose to extend the game to play an aircraft version of the game, “AirShip”.

    Minigames and other game modes. For example, a survival game mode can be implemented where you and your opponent only possess one ship and must play until one player kills the other players sole ship.

How to extend Pirateship (Instructions):

--> In order to add obstacles to an extended version of Pirateship, follow the instructions below:

## Authors/Summary's

* **Krish Chowdhary** - I had a multi-faceted role in the team, and as a result, my code contributions can be found throughout the repository.  Some of the key features that I worked on included writing the majority of the individual game stages, the Main class, the Board and the Tile classes. My work on the Board and Tile also involved designing how we wanted to model the Battleship game, and this initial planning stage was critical for the success of the game itself. The Main class involved bringing together all the different application components, and integrating them through a series of helper functions. These provided an easy API and made modifying and improving the code fairly straight forward. For the README, I worked on the “Code Overview and Design” section and one part of the “Contributing” section. I chose to work on the former since I had led to the discussion on the original design of the application, this meant that I had a deep understanding of how all the classes interacted with each other. For the latter, since I have some experience with open-source projects, I chose to write up a small guide to teach people how to contribute to the project.
* **Sabeeh Ashraf** - Throughout the journey of this project, I played an assistive and open-minded role. I worked to establish and code the credit system that is associated with the ships, particularly, the credits and types of available to each ship object (supported by Krish). Having past experience with pygame and being comfortable with graphics, I worked on the graphics for the ship objects. As per the README, my contributions can be witnessed through the “Extending Pirateship” portion. Within this section, I outlined potential out-of-scope features for individuals that may struggle to extend and personalize the game for themselves. I also provided an example of how to implement out-of-scope features. Lastly, I refined and edited the README document, checking for grammatical and spelling errors, and improved the document’s format in order to appeal to readers. Such tasks were assigned to me as I worked on out-of-scope features for our game, and displayed strong collaborative when refining our project plan. 

* **Jaden Banson** - *[Insert Summary]*
* **Zeina Adi** - *[Insert Summary]*
* **Kevin Borja** - *[Insert Summary]*

See also the list of [contributors](https://github.com/krishchow/Null-Battleship/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
