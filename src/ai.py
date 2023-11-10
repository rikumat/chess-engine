import chess
from copy import deepcopy
values = {
    ".":0,
    "k": -10**20,
    "q": -9,
    "r": -5,
    "n":-3,
    "b":-3,
    "p":-1,
    "K": 10**20,
    "Q": 9,
    "R": 5,
    "N":3,
    "B":3,
    "P":1,
    " ":0,
    "\n":0,
}
class Ai():
    """This class is responsible for calculating a chess move given an arbitrary position."""
    def __init__(self):
        pass

    def evaluate(self, board:str):
        """
        This function numerically evaluates a chess board. Positive valuation means advantage for white,
        negative means advantage for black.
        """
        value = 0
        for i in board:
            value+=values[i]

        if value != 0:
            print(value)

        return value

    def calculate_move(self, board):
        """This function takes a chessboard as an argument, 
        and returns the best possible move according to the alphabeta function."""
        value, move = self.alphabeta(board, -10**15, 10**15, 5, False)
        return move

    def alphabeta(self, board: chess.Board, alpha, beta, depth, maximizing):
        print("______")
        """
        This function uses minimax algorithm with alpha beta pruning to calculate the best possible move
        from a given chessboard.
        """

        if depth==0:
            return self.evaluate(str(board)), None

        if maximizing:
            best_move=None
            max_eval=-10**15
            for move in board.legal_moves:
                new_board = deepcopy(board)
                new_board.push(move)

                evaluation, next_move = self.alphabeta(new_board, alpha, beta, depth-1, False)
                alpha = max(alpha, evaluation)
                if evaluation>max_eval:
                    best_move=move

                max_eval = max(evaluation, max_eval)
                if alpha >= beta:
                    break

            return max_eval, best_move

        else:
            min_eval = 10**15
            best_move=None
            for move in board.legal_moves:
                new_board = deepcopy(board)
                new_board.push(move)

                evaluation, next_move = self.alphabeta(new_board, alpha, beta, depth-1, True)
                beta = min(beta, evaluation)

                if evaluation < min_eval:
                    best_move=move

                min_eval = min(min_eval, evaluation)
                if beta <= alpha:
                    break

            return min_eval, best_move

  






