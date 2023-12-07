from datetime import datetime

import sys
from entities.board import Board
from math import sqrt

import utils
from multiplier_matrices import multiplier_matrices
generator = Board()


values = {
    ".":0,
    "k": -10**10,
    "q": -90,
    "r": -50,
    "n":-30,
    "b":-30,
    "p":-10,
    "K": 10**10,
    "Q": 90,
    "R": 50,
    "N":30,
    "B":30,
    "P":10,
    " ":0,
    "\n":0,
}
letter_to_number = {
    "a":0,
    "b":1,
    "c":2,
    "d":3,
    "e":4,
    "f":5,
    "g":6,
    "h":7
}
number_to_letter = {number:letter for letter, number in letter_to_number.items()}



class Ai():
    """This class is responsible for calculating a chess move given an arbitrary position."""
    def __init__(self):
        pass

    def calculate_balance(self, board):
        balance=0
        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                balance+=multiplier_matrices[piece][i][j]*values[piece]
        return balance

    def evaluate(self, board, game_data):
        """
        This function numerically evaluates a chess board. 
        Positive valuation means advantage for white,
        negative means advantage for black.
        """
        return game_data["balance"]
        value=0

        ai_king = utils.square_to_coordinates(game_data["ai_king"])
        player_king = utils.square_to_coordinates(game_data["player_king"])

        player_distance_to_king=0
        ai_distance_to_king=0

        for i, row in enumerate(board):
            for j, piece in enumerate(row):

                value+=values[piece]

                if piece.islower() and piece != ".":
                    ai_distance_to_king+=sqrt((i-player_king[0])**2+(j-player_king[1])**2)

                elif not piece.islower() and piece != ".":
                    player_distance_to_king+=sqrt((i-ai_king[0])**2+(j-ai_king[1])**2)
        if game_data["balance"] != value:
            print(game_data["balance"])
            print(value)
        value+=(5/player_distance_to_king)*10
        value-=(5/ai_distance_to_king)*10

        return value

    def calculate_move(self, board, white):
        """This function takes a chessboard as an argument, 
        and returns the best possible move according to the alphabeta function."""
        game_data = {}
        game_data["balance"] = self.calculate_balance(board)
        game_data["winner"]=0

        move_dict={}
        cached_moves = {}
        value, move = 0, 0
        for i in range(4, 15):
                start_time = datetime.now()
                value, move = self.alphabeta(board, -10**15, 10**15, game_data, i, white, move_dict, cached_moves)
                print(i, end="\n", flush=True)
                if (datetime.now()-start_time).total_seconds()>=3 and i>=6:
                    break
        print(value, i)
        return move

    def alphabeta(self, board, alpha, beta, game_data, depth, maximizing, move_dict, memo):
        """
        This function uses minimax algorithm with alpha beta pruning
        to calculate the best possible move
        from a given chessboard.
        """
        player_number={
            True: "1",
            False: "0"
        }

        if game_data["winner"] != 0:
            return game_data["winner"]*10**10+game_data["winner"]*depth, None

        if depth==0:
            return self.evaluate(board, game_data), None

        board_key = "".join(["".join(x) for x in board])+player_number[maximizing]
        transposition_key=board_key+"|"+str(depth)
        first_move = move_dict.get(board_key)
        cached_move = memo.get(transposition_key)

        if cached_move != None:
            return cached_move

        if maximizing:
            best_move=None
            max_eval=-10**15
            moves = generator.get_moves_from_board(board, True)

            if first_move!=None and moves[-1]!=first_move:
                moves.append(first_move)

            for i in range(len(moves)-1, -1, -1):
                move = moves[i]

                coords_start = utils.square_to_coordinates(move[:2])
                coords_end = utils.square_to_coordinates(move[2:])

                piece_taken = board[coords_end[0]][coords_end[1]]
                current_piece = board[coords_start[0]][coords_start[1]]
                current_piece_after = current_piece

                if coords_end[0]==0 and current_piece=="P":
                    board[coords_start[0]][coords_start[1]]="Q"
                    current_piece_after="Q"

                multiplier_own = multiplier_matrices[current_piece][coords_start[0]][coords_start[1]]
                multiplier_own_after = multiplier_matrices[current_piece_after][coords_end[0]][coords_end[1]]
                multiplier_opponent = multiplier_matrices[piece_taken][coords_end[0]][coords_end[1]]

                if piece_taken=="k":
                    game_data["winner"]=1


                board[coords_end[0]][coords_end[1]]=board[coords_start[0]][coords_start[1]]
                board[coords_start[0]][coords_start[1]]="."

                balance_change=0
                balance_change-=values[piece_taken]*multiplier_opponent
                balance_change-=values[current_piece]*multiplier_own
                balance_change+=values[current_piece_after]*multiplier_own_after
                game_data["balance"]+=balance_change
                evaluation, next_move = self.alphabeta(board, alpha, beta, game_data, depth-1, False, move_dict, memo)
                game_data["winner"]=0

                game_data["balance"]-=balance_change

                board[coords_start[0]][coords_start[1]]=current_piece
                board[coords_end[0]][coords_end[1]]=piece_taken

                alpha = max(alpha, evaluation)
                if evaluation>max_eval:
                    best_move=move

                max_eval = max(evaluation, max_eval)

                if alpha >= beta:
                    break

            move_dict[board_key]=best_move
            memo[transposition_key]=(max_eval, best_move)
            return max_eval, best_move

        min_eval = 10**15
        best_move=None

        moves = generator.get_moves_from_board(board, False)
        if first_move!=None and moves[-1]!=first_move:
            moves.append(first_move)

        for i in range(len(moves)-1, -1, -1):
            move = moves[i]
            coords_start = utils.square_to_coordinates(move[:2])
            coords_end = utils.square_to_coordinates(move[2:])

            piece_taken = board[coords_end[0]][coords_end[1]]
            current_piece = board[coords_start[0]][coords_start[1]]
            current_piece_after = current_piece

            if piece_taken=="K":
                game_data["winner"]=-1
            
            if coords_end[0]==7 and current_piece=="p":
                board[coords_start[0]][coords_start[1]]="q"
                current_piece_after="q"


            multiplier_own = multiplier_matrices[current_piece][coords_start[0]][coords_start[1]]
            multiplier_own_after = multiplier_matrices[current_piece_after][coords_end[0]][coords_end[1]]
            multiplier_opponent = multiplier_matrices[piece_taken][coords_end[0]][coords_end[1]]

            board[coords_end[0]][coords_end[1]]=board[coords_start[0]][coords_start[1]]
            board[coords_start[0]][coords_start[1]]="."

            balance_change=0
            balance_change-=values[piece_taken]*multiplier_opponent
            balance_change-=values[current_piece]*multiplier_own
            balance_change+=values[current_piece_after]*multiplier_own_after

            game_data["balance"]+=balance_change

            evaluation, next_move = self.alphabeta(board, alpha, beta, game_data, depth-1, True, move_dict, memo)

            game_data["winner"]=0

            game_data["balance"]-=balance_change

            board[coords_start[0]][coords_start[1]]=current_piece
            board[coords_end[0]][coords_end[1]]=piece_taken

            beta = min(beta, evaluation)

            if evaluation < min_eval:
                best_move=move

            min_eval = min(min_eval, evaluation)
            if beta <= alpha:
                break

        move_dict[board_key]=best_move
        memo[transposition_key]=(min_eval, best_move)

        return min_eval, best_move
