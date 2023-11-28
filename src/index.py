import chess

from services.engine import Engine
from services.ai import Ai

board = chess.Board()
chess_engine = Engine()
ai = Ai()

print(chess_engine.board)
while True:
    move = input("Enter your move ")
    if move == "quit":
        break
    result = chess_engine.make_move(move)

    if result is True:
        ai_move = ai.calculate_move(chess_engine.board, False)
        print(ai_move)
        chess_engine.make_move(ai_move)
        print(chess_engine.board)

    else:
        print(result)
