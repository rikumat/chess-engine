import chess

class Engine():
    """This class is responsible for keeping the state of the game."""
    def __init__(self, board: chess.Board):
        """
        self.board: the current situation on chess board.
        """
        self.board=board

    def make_move(self, uci):
        """
        This function takes a move as an argument, and updates self.board.
        """
        try:
            move = chess.Move.from_uci(uci)
            if move in self.board.legal_moves:
                self.board.push(move)
                return True
            else:
                return "Illegal move"
        except chess.InvalidMoveError:
            return "Invalid move"

    def get_board(self):
        return self.board


    

