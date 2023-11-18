import utils


class Board():
    def __init__(self):
        pass

    def get_vertical_and_horizontal_moves(self, board, square):
        """
        calculate vertical and horizontal moves.
        Used to calculate moves for rooks and queen.
        """
        moves = []
        coordinates = utils.square_to_coordinates(square)
        for i in range(coordinates[0], 8):
            pass

    def get_diagonal_moves(self, board, square):
        """
        calculates legal diagonal moves from square on a chessboard.
        Used for calculating queen and bishop moves.
        """
        coordinates = utils.square_to_coordinates(square)
        right_bottom_limit = 8-max(coordinates)

        legal = []
        for i in range(1, right_bottom_limit):
            legal_coordinate=(coordinates[0]+i, coordinates[1]+i)
            legal.append(utils.coordinates_to_square(legal_coordinate))

        return legal

    def get_pawn_moves(self, board, square):
        pass

    def get_queen_moves(self, board, square):
        pass

    def get_rook_moves(self, board, square):
        pass

    def get_knight_moves(self, board, square):
        pass

    def get_bishop_moves(self, board, square):
        pass

    def get_pawn_moves(self, board, square):
        pass

    def get_king_moves(self, board, square):
        pass
