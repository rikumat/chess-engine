import utils


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
            print("yks")
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
        coordinates = utils.square_to_coordinates(square)
        legal = []
        if not board[coordinates[0]][coordinates[1]].islower():
            if board[coordinates[0]-1][coordinates[1]]==".":
                legal.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1])))
            if board[coordinates[0]-1][coordinates[1]+1].islower():
                legal.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1]+1)))
            if board[coordinates[0]-1][coordinates[1]-1].islower():
                legal.append(square+utils.coordinates_to_square((coordinates[0]-1, coordinates[1]-1)))
            return legal

        if board[coordinates[0]+1][coordinates[1]]==".":
            legal.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1])))
        eat_right = board[coordinates[0]+1][coordinates[1]+1]
        if not eat_right.islower() and eat_right!=".":
            legal.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1]+1)))
        eat_left = board[coordinates[0]+1][coordinates[1]-1]
        if not eat_left.islower() and eat_left!=".":
            legal.append(square+utils.coordinates_to_square((coordinates[0]+1, coordinates[1]-1)))
        return legal


    def get_queen_moves(self, board, square):
        pass

    def get_rook_moves(self, board, square):
        pass

    def get_knight_moves(self, board, square):
        legal = []
        moves = []
        coordinates = utils.square_to_coordinates(square)
        current = board[coordinates[0]][coordinates[1]]
        for i in [-1, 1]:
            for j in [-1, 1]:
                moves.append((coordinates[0]+2*i, coordinates[1]+j))
                moves.append((coordinates[0]+j, coordinates[1]+2*i))

        for move in moves:
            if self.coordinates_valid(move):
                taken = board[move[0]][move[1]]
                if taken=="." or taken.islower() != current.islower():
                    legal.append(square+utils.coordinates_to_square(move))
        return legal
    

    def get_bishop_moves(self, board, square):
        pass

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
                        legal.append(square+utils.coordinates_to_square(target_coordinates))

        return legal

