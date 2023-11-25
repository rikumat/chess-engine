# Implementation

## Classes
This project is divided into 3 classes: Ai, Board and Engine.

### Board
This class is responsible for generating legal moves. an Instance of this class will be injected to the Ai class in the future.

### Engine
This class is responsible for keeping track of the game state, and verifying the player's moves.

### Ai
This class is responsible for calculating a move in response to the user's move.

## Utils

Utils is a file of utility functions. Currently there are 2 functions in this file: coordinates_to_square and square_to_coordinates, which help conversions between chess moves and coordinates that can be used to access the matrix that represents the chess board.
