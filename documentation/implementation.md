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

## sequence diagram of user's move and ai's response. (after board class is integrated to Ai)


```mermaid
sequenceDiagram
  actor User
  participant Index
  participant Engine
  participant Ai
  participant Board

User ->> Index:input e2e4
Index ->> Engine: engine.make_move("e2e4")
Engine -->> Index: True
Index ->> Ai: Ai.calculate_move(Engine.get_board(), False)
Ai ->> Board: Board.get_all_moves(board, False)
Board -->> Ai: list of moves
Ai->>Ai: alphabeta
Ai -->> Index: "b8c6"
Index -->> User: output b8c6
  ```
