import utils
from copy import deepcopy

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
    def __init__(self, ai, move_generator, board=start_board):

        """
        self.board: the current situation on chess board.
        """
        self.move_generator =  move_generator
        self.ai=ai
        self.board=board
        self.previous_state=None


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

    def editor(self):
        """
        while this method is running, the player can use 
        editor commands to modify the chessboard.
        """
        while True:
            command = input("Enter command: ")
            if command == "exit":
                break
            if len(command)==3:
                coords = utils.square_to_coordinates(command[1:])
                self.board[coords[0]][coords[1]]=command[0]

    def run(self):
        """
        this method is the main gameloop.
        """
        while True:
            for i in self.board:
                print(''.join(i), end="\n", flush=True)

            move = input("Enter your move: ")
            if move == "editor":
                self.editor()

            if move == "cancel":
                self.board = deepcopy(self.previous_state)
                continue

            if move == "quit":
                break

            if not move in self.move_generator.get_moves_from_board(self.board, True):
                print("Warning: illegal move!")
            
            self.previous_state=deepcopy(self.board)

            result = self.make_move(move)
            for i in self.board:
                print(''.join(i), end="\n", flush=True)

            if result is True:
                ai_move = self.ai.calculate_move(self.board, False)
                print("computer moves {}".format(ai_move))
                self.make_move(ai_move)
            else:
                print(result)
                



