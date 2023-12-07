import utils
start_board = [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"]
    ]
class Engine():
    """This class is responsible for keeping the state of the game."""
    def __init__(self, board=start_board):

        """
        self.board: the current situation on chess board.
        """
        self.board=board

    def make_move(self, move):
        """
        This function takes a move as an argument, and updates self.board.
        """

        if len(move)!=4:
            return "Invalid move"

        start = utils.square_to_coordinates(move[:2])
        end=utils.square_to_coordinates(move[2:])
        if self.board[start[0]][start[1]]=="p" and end[0]==7:
            self.board[start[0]][start[1]]="q" 

        if self.board[start[0]][start[1]]=="P" and end[0]==0:
            self.board[start[0]][start[1]]="Q" 

        self.board[end[0]][end[1]]=self.board[start[0]][start[1]]
        self.board[start[0]][start[1]]="."

        return True

