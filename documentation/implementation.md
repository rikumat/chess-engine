# Implementation

## Classes
This project is divided into 3 classes: Ai, MoveGenerator and Engine. An instance of MoveGenerator is injected to Ai and Instances of Ai and MoveGenerator are injected to Engine. Engine is the only class whose methods (.run) are called from Index.

### MoveGenerator
This class is responsible for generating pseudo-legal moves. This class is used solely by both the Ai and Engine classes. Ai uses MoveGenerator to find moves on each minimax level. Pseudo-legal moves are partially legal, meaning disallowing moving through material / on top of own pieces, but doesn't check for checks. This means 

### Engine
This class is the user interface of the game. This class contains all gameloops, and all the code related to user input. This class contains methods for validating user input, and checking move legality. This class also stores the board state, and executes moves chosen by the player and the ai. Instances of Ai and MoveGenerator are injected for an instance of this class. The .run is the entry point of the program, and starts the main gameloop, which takes input from user and Ai. Once this loop is broken, the program exits.

### Ai
This class is responsible for calculating the best move from a given chessboard for given color. Methods of this class are only used in the Engine class. The alphabeta function is used to calculate a move, validate move legality, and detect checkmates and stalemates. This is done according to the following logic:

- Checkmate: minimax/alphabeta is called on color x with depth 2 (one own and one opponents move) if the best scenario after these moves results in the color x king being eaten, either stalemate or checkmate has occured. To confirm this is a checkmate, alphabeta is also called on depth 1 with the opposite color, to tell whether the king of color x is currently under attack. If it is, a checkmate has occured.

- Stalemate: if best case scenario in 2 moves starting from color x is the color x king being eaten, but color x king is not currently under attack, a stalemate has occured.

- move legality: after color x has moved, call alphabeta/minimax with the opposite color and depth 1. If this results in color x king being eaten, the move is illegal, as color x didn't get out of check.

## Utils

Utils is a file of utility functions. Currently there are 2 functions in this file: coordinates_to_square and square_to_coordinates, which help conversions between chess moves and coordinates that can be used to access the matrix that represents the chess board.

## class diagram
```mermaid
classDiagram
  Engine<|-- Ai
  Engine<|-- MoveGenerator
  Ai <|-- MoveGenerator
  Index <|-- Engine
  Index: move_generator = MoveGenerator()
  Index: ai = Ai(move_generator)
  Index: engine = Engine(ai, move_generator)
  Index: engine.run()
  Engine: self.board = [[...]]
  Engine: def run()
  Engine: def move_is_legal(move, is_white)
  Engine: def make_move(move)
  Ai: def calculate_move(board, is_white)
  MoveGenerator: get_moves_from_board(board, is_white)
  ```

## sequence diagram of user's move and ai's response. where player's move is legal, and neither move results in checkmate.


```mermaid
sequenceDiagram
  actor User
  participant Engine
  participant Ai

  User ->> Engine: input("e2e4")
  Engine ->> Engine: move_is_legal("e2e4", True)
  Engine ->> Ai: alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 1, not is_white, {})

  loop During recursion
  Ai ->> MoveGenerator: get_moves_from_board(board, is_white)
  MoveGenerator -->> Ai: [list of moves]
  Ai ->> Ai: Recursive alphabeta call
  end

  Ai -->> Engine: 0
  Engine -->> Engine: True
  Engine ->> Engine: make_move("e2e4", True)
  Engine -->> User: print(self.board)
  Engine ->> Engine: check_end_condition(True)
  Engine ->> Ai: alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 2, False, {})

  loop During recursion
  Ai ->> MoveGenerator: get_moves_from_board(board, is_white)
  MoveGenerator -->> Ai: [list of moves]
  Ai ->> Ai: Recursive alphabeta call
  end
  Ai -->> Engine: 0

  Engine ->> Ai: alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 1, True, {})
  loop During recursion
  Ai ->> MoveGenerator: get_moves_from_board(board, is_white)
  MoveGenerator -->> Ai: [list of moves]
  Ai ->> Ai: Recursive alphabeta call
  end
  Ai -->> Engine: 0
  Engine -->> Engine: False
  Engine ->> Ai: calculate_move(self.board, False)


  Ai -->> Engine: "d5d7"
  Engine ->> Engine: make_move("d5d7", False)
  Engine -->> User: print(self.board)
  Engine ->> Engine: check_end_condition(False)
  Engine -->> Engine: False
  ```


## sequence diagram where the user checkmates the ai


```mermaid
sequenceDiagram
  actor User
  participant Engine
  participant Ai
  participant Board

  User ->> Engine: input("a5d8")
  Engine ->> Engine: move_is_legal("a5d8", True)
  Engine ->> Ai: alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 1, False, {})

  loop During recursion
  Ai ->> MoveGenerator: get_moves_from_board(board, is_white)
  MoveGenerator -->> Ai: [list of moves]
  Ai ->> Ai: Recursive alphabeta call
  end

  Ai -->> Engine: 30
  Engine -->> Engine: True
  Engine ->> Engine: make_move("e2e4", True)
  Engine -->> User: print(self.board)

  Engine ->> Engine: check_end_condition(True)

  Engine ->> Ai: alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 2, False, {})
  loop During recursion
  Ai ->> MoveGenerator: get_moves_from_board(board, is_white)
  MoveGenerator -->> Ai: [list of moves]
  Ai ->> Ai: Recursive alphabeta call
  end
  Ai -->> Engine: 10**10

  Engine ->> Ai: alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 1, True, {})
  loop During recursion
  Ai ->> MoveGenerator: get_moves_from_board(board, is_white)
  MoveGenerator -->> Ai: [list of moves]
  Ai ->> Ai: Recursive alphabeta call
  end
  Ai -->> Engine: 10**10

  Engine -->> Engine: 'checkmate'

  Engine ->> Engine: ending_menu('Player', 'checkmate')
  ```

# Square values
The ai uses several matrices to calculate values for preferred positions. These values can be found in the location_values.py file in a dictionary of the same name. These matrices contain values for each square which are added to material balance as long as a specified type of piece is on top of a given square.

# Implemented algorithms

## Minimax and alpha-beta pruning
According to original plan, the final production of Ai uses minimax with alpha-beta pruning. The achieved time-complexity for this is O(2^n) (exponential). The space-complexity of this program is O(n) (linear). This is the result of storing information about best moves on each level of the recursion. Against the original plan, legal moves are not maintained. Instead, they are generated from a given chessboard for a given color.

## Iterative deepening and transposition table
In addition to original plan, minimax is also enhanced with iterative deepening search. This approach iteratively finds the best move on increasing depths, until a time limit (3 seconds) is surpassed for the previous depth. This allows the Ai to calculate deeper into the tree when calculation happens fast. This also allows to quickly find best move on a lower depth, which is typically at least a good move on higher depths. If this move happens to be the best move, then the large amount of alphabeta pruning occurs. Even if it is not the best move, the search window will be greatly reduced, increasing the effect of alphabeta pruning.

The efficiency of minimax was further improved with the implementation of a transposition table. This table stores return values of the function in memory, which can be utilized if the algorithm ends in the same position later in execution. The transposition table stores 2 different kinds of values: limit values and exact values. A return value of an alphabeta call is only exact if no pruning occured. If this is the case, this value can be immediately returned when the algorithm ends in the same state in the future. If pruning has occured, we know the true value of the best move in this position is at least as good as the best value achieved before pruning occured. In this case, this value can be used as a limit for alpha / beta if the algorithm ends in this position in the future. This decreases the search window size, resulting in more alpha-beta pruning.



# Limitations

## Moves
Currently legal moves don't include castling or en passant. This is due to the fact that the MoveGenerator was built to calculate moves only from the state of the chessboard, while both of these moves need additional information. Castling is only allowed if rook and king haven't been moved yet, and en passant is only allowed for pawns that started by moving 2 squares forward, and haven't been moved since. Allowing these moves would improve the Ai greatly, since it would know to prepare for them, even if it didn't use the moves itself. One option for better user experience is to only allow these moves for the player but not for the Ai. This would be much easier to implement, and wouldn't affect performance.

## Ai draws
Related to the previous issue, the Ai can't tell apart stalemate and checkmate. This is problematic especially when the Ai has gained a large advantage, since stalemate is increasingly likely. Similarly, the Ai doesn't recognize draw by repetition, which is a common occurence as the Ai always executes the same move in a given state. This can result in the Ai drawing a winning position.

## Gameplay
Currently the player is always white, and Ai is always black. This also means the player always starts the game. This is something that should be changed in the future, if development of this project continues. This wouldn't demand much work, since the calculate_move method takes color as an argument.

# Sources
- **Generative AI was not used as a source in the making of this program.**
- https://www.youtube.com/watch?v=l-hh51ncgDI
- https://www.chessstrategyonline.com/content/tutorials/basic-chess-concepts-material

