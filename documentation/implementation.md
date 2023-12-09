# Implementation

## Classes
This project is divided into 3 classes: Ai, Board and Engine.

### Board
This class is responsible for generating legal moves. This class is used solely by The Ai class. Board's only interface to outside modules is the .get_moves_from_board method, which takes board and player's color as argument. 

### Engine
This class is responsible for keeping track of the game state, and verifying the player's moves. this class's game matrix is updated every time Ai's .calculate_move method returns a new move, and when player inputs a valid move.

### Ai
This class is responsible for calculating a move in response to the user's move. This class is only used in the main gameloop found in index.py. This class's only interface to other modules is the .calculate_move method, which takes a 2-dimensional list (chess board) and players's color as arguments, and returns a move in the same form user inputs their move.

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
Index ->> Ai: Ai.calculate_move(board matrix, False)
loop on every recursive Alphabeta call
  Ai ->> Board: Board.get_moves_from_board(board, False)
  Board -->> Ai: list of moves
    end
Ai -->> Index: "b8c6"
Index -->> User: output b8c6
  ```

## class diagram
```mermaid
classDiagram
  Index<|-- Ai
  Ai <|-- Board
  Index <|-- Engine
  Index: player_move = input("Enter your move")
  Index: engine.make_move(player_move)
  Index: ai_move = ai.calculate_move(board, False)
  Index: engine.make_move(ai_move)
  Index: print(engine.board)
  Ai: calculate_move()
  Board: get_moves_from_board()
  Engine: make_move()
  Engine: self.board
  ```
# Square values
The ai uses several matrices to calculate values for preferred positions. These values can be found in the multiplier_matrices.py file. Each piece has it's own matrix, which is used to alter evaluation depending on the piece's location on the board.

