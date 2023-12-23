import utils
from location_values import location_values

bias=0

move_priority = {
    "p": 15,
    "n":10,
    "b": 10,
    "r":5,
    "q":0,
    "k":-10
}

values = {
    "K": 10**10,
    "Q": 90+bias,
    "R": 50+bias,
    "N":30+bias,
    "B":30+bias,
    "P":10+bias,
    "K": 10**10,
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

class MoveGenerator():
    def __init__(self):
        """
        This class is responsible for generating pseudo-legal moves 
        from a given square on a given board.
        """

    def coordinates_valid(self, coordinates):
        """
        check if coordiates (y, x) are on a chessboard.
        """
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

            legal.append(square+utils.coordinates_to_square((i, coordinates[1])))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(coordinates[0]+1, 8):
            taken_piece = board[i][coordinates[1]]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            legal.append(square+utils.coordinates_to_square((i, coordinates[1])))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(coordinates[1]-1, -1, -1):
            taken_piece = board[coordinates[0]][i]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            legal.append(square+utils.coordinates_to_square((coordinates[0], i)))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(coordinates[1]+1, 8):
            taken_piece = board[coordinates[0]][i]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            legal.append(square+utils.coordinates_to_square((coordinates[0], i)))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        return legal


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

            legal.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(1, right_top_limit):
            legal_coordinate=(coordinates[0]-i, coordinates[1]+i)
            taken_piece = board[legal_coordinate[0]][legal_coordinate[1]]
            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            legal.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(1, left_top_limit):
            legal_coordinate = (coordinates[0]-i, coordinates[1]-i)
            taken_piece = board[legal_coordinate[0]][legal_coordinate[1]]

            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            legal.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break

        for i in range(1, left_bottom_limit):
            legal_coordinate=(coordinates[0]+i, coordinates[1]-i)
            taken_piece = board[legal_coordinate[0]][legal_coordinate[1]]

            if (taken_piece.islower() == current_piece.islower() and taken_piece !="."):
                break

            legal.append(square+utils.coordinates_to_square(legal_coordinate))

            if taken_piece.islower() != current_piece.islower() and taken_piece!=".":
                break
        return legal



    def get_pawn_moves(self, board, square):
        """returns a list of legal moves on a chessboard
        from given square, when the piece to be moved is a pawn."""
        coordinates = utils.square_to_coordinates(square)
        legal = []

        if not board[coordinates[0]][coordinates[1]].islower():
            if coordinates[0]==6 and board[5][coordinates[1]]=="." and board[4][coordinates[1]]==".":

                legal.append(square+utils.coordinates_to_square((4, coordinates[1])))

            if board[coordinates[0]-1][coordinates[1]]==".":
                legal.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1])))

            if coordinates[1]+1<=7 and board[coordinates[0]-1][coordinates[1]+1].islower():
                taken_piece = board[coordinates[0]-1][coordinates[1]+1]

                legal.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1]+1)))

            if coordinates[1]-1>=0 and board[coordinates[0]-1][coordinates[1]-1].islower():
                taken_piece = board[coordinates[0]-1][coordinates[1]-1]
                legal.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1]-1)))

            return legal

        if coordinates[0]==1 and board[2][coordinates[1]]=="." and board[3][coordinates[1]]==".":
            legal.append(square+utils.coordinates_to_square((3, coordinates[1])))

        if board[coordinates[0]+1][coordinates[1]]==".":
            legal.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1])))

        if coordinates[1]+1<=7:
            eat_right = board[coordinates[0]+1][coordinates[1]+1]
            if not eat_right.islower() and eat_right!=".":
                legal.append(square+utils.coordinates_to_square(
                    (coordinates[0]+1, coordinates[1]+1)
                ))

        if coordinates[1]-1>=0:
            eat_left = board[coordinates[0]+1][coordinates[1]-1]
            if not eat_left.islower() and eat_left!=".":
                legal.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1]-1)))
        return legal

    def get_queen_moves(self, board, square):
        """returns a list of legal moves on a chessboard
        from given square, when the piece to be moved is a queen."""
        return self.get_diagonal_moves(board, square)+self.get_vertical_and_horizontal_moves(board, square)


    def get_knight_moves(self, board, square):
        """returns a list of legal moves on a chessboard
        from given square, when the piece to be moved is a knight."""
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
                            legal.append(square+utils.coordinates_to_square(move))
        return legal

    def get_king_moves(self, board, square):
        """returns a list of legal moves on a chessboard
        from given square, when the piece to be moved is a king."""
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
                        legal.append(square+utils.coordinates_to_square(target_coordinates))
        return legal

    def get_moves_from_board(self, board, is_white):
        """
        finds and returns all legal moves of given player on a given board.
        """
        legal = []
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

            if taken!="." and own.lower()!="k":
                value+=values[taken]
                value+=(1/values[own])*10
                value+=location_values[taken][coords_end[0]][coords_end[1]]
                value+=location_values[own][coords_end[0]][coords_end[1]]
                value-=location_values[own][coords_start[0]][coords_start[1]]
                return round(value, 3)

            if own.lower()!="k":
                value += location_values[own][coords_end[0]][coords_end[1]]
                value -= location_values[own][coords_start[0]][coords_start[1]]
                return round(value, 3)
            return -1

        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if piece==".":
                    continue
                if is_white and not piece.islower() and piece!=".":

                    legal.extend(functions[piece.lower()](board, utils.coordinates_to_square((i, j))))
                if not is_white and piece.islower() and piece!=".":
                    legal.extend(functions[piece](board, utils.coordinates_to_square((i, j))))

        legal.sort(key=move_sort)
        return legal
