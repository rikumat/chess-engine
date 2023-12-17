# Implementation

## Classes
This project is divided into 3 classes: Ai, Board and Engine.

### MoveGenerator
This class is responsible for generating legal moves. This class is used solely by both the Ai and Engine classes. Ai uses MoveGenerator to find legal moves on each minimax level.

### Engine
This class is the user interface of the game. This class contains all gameloops, and all the code related to user input. This class contains methods for validating user input, and checking move legality. This class also stores the board state, and executes moves chosen by the player and the ai. Instances of Ai and MoveGenerator are injected for an instance of this class. The .run is the entry point of the program, and starts the main gameloop, which takes input from user and Ai. Once this loop is broken, the program exits.

### Ai
This class is responsible for calculating the best move from a given chessboard for given color. Methods of this class are only used in the Engine class. The alphabeta function is used to calculate a move, validate move legality, and detect checkmates and stalemates. This is done according to the following logic:

- Checkmate: minimax/alphabeta is called on color x with depth 2 (one own and one opponents move) if the best scenario after these moves results in the color x king being eaten, either stalemate or checkmate has occured. To confirm this is a checkmate, alphabeta is also called on depth 1 with the opposite color, to tell whether the king of color x is currently under attack. If it is, a checkmate has occured.

- Stalemate: if best case scenario in 2 moves starting from color x is the color x king being eaten, but color x king is not currently under attack, a stalemate has occured.

- move legality: after color x has moved, call alphabeta/minimax with the opposite color and depth 1. If this results in color x king being eaten, the move is illegal, as color x didn't get out of check.

## Utils

Utils is a file of utility functions. Currently there are 2 functions in this file: coordinates_to_square and square_to_coordinates, which help conversions between chess moves and coordinates that can be used to access the matrix that represents the chess board.

## sequence diagram of user's move and ai's response.


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
The ai uses several matrices to calculate values for preferred positions. These values can be found in the location_values.py file in a dictionary of the same name. These matrices contain values for each square which are added to material balance as long as a specified type of piece is on top of a given square.


# Limitations

## Moves
Currently legal moves don't include castling or en passant. This is due to the fact that the MoveGenerator was built to calculate moves only from the state of the chessboard, while both of these moves need additional information. Castling is only allowed if rook and king haven't been moved yet, and en passant is only allowed for pawns that started by moving 2 squares forward, and haven't been moved since. Allowing these moves would improve the Ai greatly, since it would know to prepare for them, even if it didn't use the moves itself. One option for better user experience is to only allow these moves for the player but not for the Ai. This would be much easier to implement, and wouldn't affect performance.

## Ai draws
Related to the previous issue, the Ai can't tell apart stalemate and checkmate. This is problematic especially when the Ai has gained a large advantage, since stalemate is increasingly likely. Similarly, the Ai doesn't recognize draw by repetition, which is a common occurence as the Ai always executes the same move in a given state. This can result in the Ai drawing a winning position.

## Gameplay
Currently the player is always white, and Ai is always black. This also means the player always starts the game. This is something that should be changed in the future, if development of this project continues. This wouldn't demand much work, since the calculate_move method takes color as an argument.
