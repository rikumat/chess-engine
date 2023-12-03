import utils
from services.engine import Engine
from services.ai import Ai


chess_engine = Engine()
ai = Ai()

for i in chess_engine.board:
    print(''.join(i))

editor_open = False

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

    if move == "quit":
        break
    result = chess_engine.make_move(move)

    if result is True:
        ai_move = ai.calculate_move(chess_engine.board, False)
        print(ai_move)
        chess_engine.make_move(ai_move)
        for i in chess_engine.board:
            print(''.join(i))

    else:
        print(result)
