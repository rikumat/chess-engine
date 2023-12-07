import utils
from copy import deepcopy
from services.engine import Engine
from services.ai import Ai
from entities.board import Board
board = Board()

chess_engine = Engine()
ai = Ai()

for i in chess_engine.board:
    print(''.join(i))

editor_open = False

previous_state=None

while True:
    while editor_open:
        command = input("Enter command: ")
        if command == "exit":
            editor_open = False
            continue
        if len(command)==3:
            coords = utils.square_to_coordinates(command[1:])
            chess_engine.board[coords[0]][coords[1]]=command[0]

    move = input("Enter your move: ")
    if move == "editor":
        editor_open=True
        continue
    if move == "cancel":
        chess_engine.board = deepcopy(previous_state)
        continue

    if move == "quit":
        break
    
    if not move in board.get_moves_from_board(chess_engine.board, True):
        print("Warning: illegal move!")
    
    previous_state=deepcopy(chess_engine.board)

    revert_move = move[2:]+move[:2]
    result = chess_engine.make_move(move)

    if result is True:
        ai_move = ai.calculate_move(chess_engine.board, False)
        revert_ai_move=ai_move[2:]+ai_move[:2]
        print(ai_move)
        chess_engine.make_move(ai_move)
        for i in chess_engine.board:
            print(''.join(i))

    else:
        print(result)
