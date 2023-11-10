from services.engine import Engine
from services.ai import Ai
import chess
board = chess.Board()
chess_engine = Engine(board)
ai = Ai()

print(chess_engine.get_board())
while True:
    move = input("Enter your move ")
    if move == "quit":
        break
    result = chess_engine.make_move(move)

    if result==True:
        ai_move = ai.calculate_move(chess_engine.get_board())
        chess_engine.make_move(ai_move.uci())
        print(chess_engine.get_board())

    else:
        print(result)




    
    


