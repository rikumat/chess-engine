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
        self.starting_position = [x[::] for x in board[::]]
        self.board=board
        self.previous_state=None

    def reset(self):
        self.board = [x[::] for x in self.starting_position[::]]
    
    def move_is_legal(self, move, is_white):
        if not move in self.move_generator.get_moves_from_board(self.board, is_white):
            return False

        checkmate_value={
            False: 10**10,
            True: -10**10
        }

        original_board = deepcopy(self.board)
        self.make_move(move)
        value, move = self.ai.alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 1, not is_white, {})
        self.board=deepcopy(original_board)

        return not value == checkmate_value[is_white]

    def check_end_condition(self, is_white):
        """
        returns 'checkmate' if player has been checkmated, 'stalemate' if the game is in stalemate, False otherwise.
        """
        checkmate_value={
            False: 10**10,
            True: -10**10
        }
        eating_value, move = self.ai.alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 1, not is_white, {})
        move_value, move = self.ai.alphabeta(self.board, -10**15, 10**15, {"balance":0, "winner":0}, 2, is_white, {})

        if eating_value != checkmate_value[is_white] and move_value==checkmate_value[is_white]:
            return "stalemate"

        if move_value==checkmate_value[is_white]:
            return "checkmate"

        return False

    def validate_move(self, move, is_white):
        letters = "abcdefgh"
        numbers = "12345678"
        valid = move[0] in letters and move[1] in numbers and move[2] in letters and move[3] in numbers
        if len(move) !=4 or not valid:
            return "Invalid move"

        if not self.move_is_legal(move, is_white):
            return "Illegal move"

        return True

    def print_board(self):
        board = deepcopy(self.board)
        letters = "#  A B C D E F G H  #"
        print(letters, flush=True)
        for i in range(0, 8):
            board[i].insert(0, str(8-i)+" ")
            board[i].append(" " + str(8-i))
            print(" ".join(board[i]), flush=True)
        print(letters, flush=True)


    def make_move(self, move):
        """
        This function takes a move as an argument, and updates self.board.
        """

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

    def ending_menu(self, winner, ending):
        if ending=="checkmate":
            print("{} wins by checkmate".format(winner))
        else:
            print("Draw by stalemate")

        while True:
            replay = input("Do you want to play another game? y/n")
            if replay=="y":
                return True
            if replay=="n":
                return False
            print("Invalid choice")

    def run(self):
        """
        this method is the main gameloop.
        """
        while True:
            self.print_board()

            if self.check_end_condition(True):
                replay = self.ending_menu("Computer", self.check_end_condition(True))
                if replay:
                    self.reset()
                    continue
                break

            move = input("Enter your move: ")

            if move == "cancel":
                if self.previous_state!=None:
                    self.board = deepcopy(self.previous_state)
                continue

            if move == "quit":
                break

            self.previous_state=deepcopy(self.board)
            
            result = self.validate_move(move, True)

            if result != True:
                print(result)
                continue

            self.make_move(move)

            self.print_board()

            if self.check_end_condition(False):
                replay = self.ending_menu("Player", self.check_end_condition(False))
                if replay: 
                    self.reset()
                    continue
                break

            value, ai_move = self.ai.calculate_move(self.board, False)
            print("computer moves {}".format(ai_move))
            self.make_move(ai_move)




