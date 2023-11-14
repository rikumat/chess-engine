from copy import deepcopy
from math import sqrt
import chess

values = {
    ".":0,
    "k": 10**20,
    "q": 90,
    "r": 50,
    "n": 30,
    "b": 30,
    "p": 10,
    "K": -10**20,
    "Q": -90,
    "R": -50,
    "N": -30,
    "B": -30,
    "P": -10,
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

    def square_to_coordinates(self, square):
        x=letter_to_number[square[0]]
        y=8-int(square[1])
        return (y, x)

    def coordinates_to_square(self, x, y):
        letter=number_to_letter[y]
        number=8-x
        return letter+str(number)

    def evaluate(self, board:str, game_data):
        """
        This function numerically evaluates a chess board. 
        Positive valuation means advantage for white,
        negative means advantage for black.
        """
        value = 0
        value += game_data["material_balance"]

        return value

    def piece_in_square(self, board, square):
        piece = board.piece_at(letter_to_number[square[0]]+(int(square[1])-1)*8)
        if piece == None:
            return "."
        return piece
         
    def calculate_move(self, board, white):
        """This function takes a chessboard as an argument, 
        and returns the best possible move according to the alphabeta function."""
        game_data = {}
        game_data["material_balance"]=0
        value, move = self.alphabeta(board, -10**15, 10**15, game_data, 5, white)
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
                piece_taken = self.piece_in_square(new_board, move.uci()[2:])
                new_data["material_balance"]+=values[str(piece_taken)]
                
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
            new_data["material_balance"]+=values[str(self.piece_in_square(new_board, move.uci()[2:]))]

            evaluation, next_move, = self.alphabeta(new_board, alpha, beta, new_data, depth-1, True)
            beta = min(beta, evaluation)

            if evaluation < min_eval:
                best_move=move

            min_eval = min(min_eval, evaluation)
            if beta <= alpha:
                break

        return min_eval, best_move
