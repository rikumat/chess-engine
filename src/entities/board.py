import utils
from multiplier_matrices import multiplier_matrices
move_priority = {
    "p": 15,
    "n":10,
    "b": 10,
    "r":5,
    "q":0,
    "k":-10
}

values = {
    "k": 10**10,
    "q": 90,
    "r": 50,
    "n":30,
    "b":30,
    "p":10,
    ".":0
}

list_indexes = {
    "k":0,
    "q":1,
    "r":2,
    "n":3,
    "b":4,
    "p":5,
    ".":6
}

class Board():
    def __init__(self):
        self.initial_board = [
            ["r", "n", "b", "q", "k", "b", "n", "r"],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            ["R", "N", "B", "Q", "K", "B", "N", "R"]
        ]
        self.moves = []
    def reset(self):
        self.moves = []

    def coordinates_valid(self, coordinates):
        return coordinates[0]<=7 and coordinates[0]>=0 and coordinates[1]<=7 and coordinates[1]>=0

    def get_vertical_and_horizontal_moves(self, board, square):
        """
        calculate vertical and horizontal moves.
        Used to calculate moves for rooks and queen.
        """
        legal = []
        coordinates = utils.square_to_coordinates(square)
        current_piece = board[coordinates[0]][coordinates[1]]

        for i in range(coordinates[0]-1, -1, -1):
            taken_piece = board[i][coordinates[1]]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square((i, coordinates[1])))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break
        
        for i in range(coordinates[0]+1, 8):
            taken_piece = board[i][coordinates[1]]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square((i, coordinates[1])))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break
        
        for i in range(coordinates[1]-1, -1, -1):
            taken_piece = board[coordinates[0]][i]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square((coordinates[0], i)))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break
        
        for i in range(coordinates[1]+1, 8):
            taken_piece = board[coordinates[0]][i]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square((coordinates[0], i)))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break
 

    def get_diagonal_moves(self, board, square):
        """
        calculates legal diagonal moves from square on a chessboard.
        Used for calculating queen and bishop moves.
        """
        coordinates = utils.square_to_coordinates(square)

        right_bottom_limit = 8 - max(coordinates)
        right_top_limit =  min(coordinates[0], 7-coordinates[1])+1
        left_top_limit = min(coordinates)+1
        left_bottom_limit = min(7-coordinates[0], coordinates[1])+1
        current_piece = board[coordinates[0]][coordinates[1]]

        legal = []
        for i in range(1, right_bottom_limit):
            legal_coordinate=(coordinates[0]+i, coordinates[1]+i)
            taken_piece = board[legal_coordinate[0]][legal_coordinate[1]]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(1, right_top_limit):
            legal_coordinate=(coordinates[0]-i, coordinates[1]+i)
            taken_piece = board[legal_coordinate[0]][legal_coordinate[1]]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break
        
        for i in range(1, left_top_limit):
            legal_coordinate = (coordinates[0]-i, coordinates[1]-i)
            taken_piece = board[legal_coordinate[0]][legal_coordinate[1]]

            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(1, left_bottom_limit):
            legal_coordinate=(coordinates[0]+i, coordinates[1]-i)
            taken_piece = board[legal_coordinate[0]][legal_coordinate[1]]

            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            self.moves.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break



    def get_pawn_moves(self, board, square):
        coordinates = utils.square_to_coordinates(square)
        legal = []

        if not board[coordinates[0]][coordinates[1]].islower():
            if coordinates[0]==6 and board[5][coordinates[1]]=="." and board[4][coordinates[1]]==".":

                self.moves.append(square+utils.coordinates_to_square((4, coordinates[1])))

            if board[coordinates[0]-1][coordinates[1]]==".":
                self.moves.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1])))

            if coordinates[1]+1<=7 and board[coordinates[0]-1][coordinates[1]+1].islower():
                taken_piece = board[coordinates[0]-1][coordinates[1]+1]

                self.moves.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1]+1)))

            if coordinates[1]-1>=0 and board[coordinates[0]-1][coordinates[1]-1].islower():
                taken_piece = board[coordinates[0]-1][coordinates[1]-1]
                self.moves.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1]-1)))

            return

        if coordinates[0]==1 and board[2][coordinates[1]]=="." and board[3][coordinates[1]]==".":
                self.moves.append(square+utils.coordinates_to_square((3, coordinates[1])))

        if board[coordinates[0]+1][coordinates[1]]==".":
            self.moves.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1])))

        if coordinates[1]+1<=7:
            eat_right = board[coordinates[0]+1][coordinates[1]+1]
            if not eat_right.islower() and eat_right!=".":
                self.moves.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1]+1)))

        if coordinates[1]-1>=0:
            eat_left = board[coordinates[0]+1][coordinates[1]-1]
            if not eat_left.islower() and eat_left!=".":
                self.moves.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1]-1)))

    def get_queen_moves(self, board, square):
        self.get_diagonal_moves(board, square)
        self.get_vertical_and_horizontal_moves(board, square)

    def get_knight_moves(self, board, square):
        legal = []
        coordinates = utils.square_to_coordinates(square)
        current = board[coordinates[0]][coordinates[1]]
        for i in [-1, 1]:
            for j in [-1, 1]:
                coordinate1 = (coordinates[0]+2*i, coordinates[1]+j)
                coordinate2 = (coordinates[0]+j, coordinates[1]+2*i)
                for move in [coordinate1, coordinate2]:
                    if self.coordinates_valid(move):
                        taken = board[move[0]][move[1]]
                        if taken=="." or taken.islower() != current.islower():
                            self.moves.append(square+utils.coordinates_to_square(move))

    def get_king_moves(self, board, square):
        legal=[]
        coordinates = utils.square_to_coordinates(square)
        current = board[coordinates[0]][coordinates[1]]
        for i in [1, -1, 0]:
            for j in [1, -1, 0]:
                if i==0 and j==0:
                    continue
                target_coordinates = (coordinates[0]+i, coordinates[1]+j)
                if self.coordinates_valid(target_coordinates):
                    target = board[coordinates[0]+i][coordinates[1]+j]
                    if target=="." or current.islower() != target.islower():
                        self.moves.append(square+utils.coordinates_to_square(target_coordinates))

    def get_moves_from_board(self, board, is_white):
        """
        finds and returns all legal moves of given player on a given board.
        """
        self.moves = []
        functions = {
            "q": self.get_queen_moves,
            "k": self.get_king_moves,
            "r": self.get_vertical_and_horizontal_moves,
            "n": self.get_knight_moves,
            "b": self.get_diagonal_moves,
            "p": self.get_pawn_moves,
        }
        def move_sort(move):
            coords_end = utils.square_to_coordinates(move[2:])
            coords_start=utils.square_to_coordinates(move[:2])
            value=0
            taken = board[coords_end[0]][coords_end[1]]
            own = board[coords_start[0]][coords_start[1]]

            if taken.lower()=="k":
                return 10**15

            if taken!=".":
                return round(values[taken.lower()]*multiplier_matrices[taken][coords_end[0]][coords_start[1]], 5)

            if own.lower()!="k":
                return round(values[own.lower()]*multiplier_matrices[own][coords_end[0]][coords_end[1]]-values[own.lower()]*multiplier_matrices[own][coords_start[0]][coords_start[1]], 5)

            return -1

        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if piece==".":
                    continue
                if is_white and not piece.islower() and piece!=".":
                    functions[piece.lower()](board, utils.coordinates_to_square((i, j)))
                if not is_white and piece.islower() and piece!=".":
                    functions[piece](board, utils.coordinates_to_square((i, j)))
        self.moves.sort(key=move_sort)
        return self.moves

