from copy import deepcopy
from math import sqrt
import chess
import utils

values = {
    ".":0,
    "k": -10**20,
    "q": -90,
    "r": -50,
    "n":-30,
    "b":-30,
    "p":-10,
    "K": 10**20,
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

    def evaluate(self, board:str, game_data):
        """
        This function numerically evaluates a chess board. 
        Positive valuation means advantage for white,
        negative means advantage for black.
        """
        board = board.replace(" ","").split("\n")
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

        value+=(5/player_distance_to_king)*200
        value-=(5/ai_distance_to_king)*200

        return value

    def calculate_move(self, board, white):
        print(board)
        """This function takes a chessboard as an argument, 
        and returns the best possible move according to the alphabeta function."""
        game_data = {}
        list_board = str(board).replace(" ","").split("\n")
        for i, row in enumerate(list_board):
            for j, piece in enumerate(row):
                if piece=="k":
                    game_data["ai_king"]=utils.coordinates_to_square((i, j))
                if piece=="K":
                    game_data["player_king"]=utils.coordinates_to_square((i, j))

        value, move = self.alphabeta(board, -10**15, 10**15, game_data, 4, white)
        print(value)
        return move

    def alphabeta(self, board: chess.Board, alpha, beta, game_data, depth, maximizing):
        """
        This function uses minimax algorithm with alpha beta pruning
        to calculate the best possible move
        from a given chessboard.
        """

        if depth==0:
            return self.evaluate(str(board), game_data), None

        if maximizing:
            best_move=None
            max_eval=-10**15
            for move in board.legal_moves:
                new_board = deepcopy(board)
                new_board.push(move)

                new_data = game_data.copy()
                if move.uci()[:2]==new_data["player_king"]:
                    new_data["player_king"]=move.uci()[2:]

                evaluation, next_move = self.alphabeta(new_board, alpha, beta, new_data, depth-1, False)
                alpha = max(alpha, evaluation)
                if evaluation>max_eval:
                    best_move=move

                max_eval = max(evaluation, max_eval)

                if alpha >= beta:
                    break

            return max_eval, best_move

        min_eval = 10**15
        best_move=None

        for move in board.legal_moves:
            new_board = deepcopy(board)
            new_board.push(move)

            new_data = game_data.copy()
            if move.uci()[:2]==new_data["ai_king"]:
                new_data["ai_king"]=move.uci()[2:]

            evaluation, next_move, = self.alphabeta(new_board, alpha, beta, new_data, depth-1, True)
            beta = min(beta, evaluation)

            if evaluation < min_eval:
                best_move=move

            min_eval = min(min_eval, evaluation)
            if beta <= alpha:
                break

        return min_eval, best_move
