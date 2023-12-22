from datetime import datetime
import utils
from location_values import location_values

bias=0

values = {
    ".":0,
    "q": -90,
    "r": -50,
    "n":-30,
    "b":-30,
    "p":-10,
    "Q": 90+bias,
    "R": 50+bias,
    "N":30+bias,
    "B":30+bias,
    "P":10+bias,
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
    def __init__(self, move_generator):
        self.move_generator = move_generator

    def calculate_balance(self, board):
        """
        This method takes a chessboard as an argument and returns the material balance
        Where 0 is equal position, negative number indicates black's advantage and positive
        the advantage of white.
        """
        balance=0

        for i, row in enumerate(board):
            for j, piece in enumerate(row):
                if piece.lower()!="k":
                    balance += values[piece]
                    if piece.islower():
                        balance -= location_values[piece][i][j]
                        continue
                    balance+=location_values[piece][i][j]

        return round(balance, 3)

    def evaluate(self, board, game_data):
        """
        This function numerically evaluates a chess board. 
        Positive valuation means advantage for white,
        negative means advantage for black.
        """
        value = round(game_data["balance"], 5)
        return value

    def calculate_move(self, board, white):
        """This function takes a chessboard as an argument, 
        and returns the best possible move according to the alphabeta function.
        """
        cached_moves = {}
        game_data = {}
        game_data["balance"] = 0
        game_data["winner"]=0
        value, move = 0, 0
        for i in range(4, 15):
            start_time = datetime.now()
            value, move = self.alphabeta(board, -10**15, 10**15, game_data, i, white, cached_moves)
            if (datetime.now()-start_time).total_seconds()>=3 and i>=6:
                break
        return value, move

    def alphabeta(self, board, alpha, beta, game_data, depth, maximizing, memo):
        """
        This function uses minimax algorithm with alpha beta pruning
        to calculate the best possible move
        from a given chessboard.
        """

        player_number={
            True: "1",
            False: "0"
        }

        if game_data["winner"] != 0:
            return game_data["winner"]*10**10+game_data["winner"]*depth, None

        if depth==0:
            return self.evaluate(board, game_data), None

        board_key = "".join(["".join(x) for x in board])+player_number[maximizing]
        transposition_key=board_key+"|"+str(depth)
        first_move = memo.get(board_key)
        cached_move = memo.get(transposition_key)

        if cached_move is not None and cached_move[2]==0:
            return (cached_move[0], cached_move[1])

        if maximizing:
            if cached_move is not None:
                alpha = max(alpha, cached_move[0])
            best_move=None
            max_eval=-10**15
            moves = self.move_generator.get_moves_from_board(board, True)
            broken=False
            if first_move is not None and moves[-1]!=first_move:
                moves.append(first_move)

            for i in range(len(moves)-1, -1, -1):
                move = moves[i]

                coords_start = utils.square_to_coordinates(move[:2])
                coords_end = utils.square_to_coordinates(move[2:])

                piece_taken = board[coords_end[0]][coords_end[1]]
                current_piece = board[coords_start[0]][coords_start[1]]
                current_piece_after = current_piece

                if coords_end[0]==0 and current_piece=="P":
                    board[coords_start[0]][coords_start[1]]="Q"
                    current_piece_after="Q"

                if piece_taken=="k":
                    game_data["winner"]=1

                board[coords_end[0]][coords_end[1]]=board[coords_start[0]][coords_start[1]]
                board[coords_start[0]][coords_start[1]]="."

                balance_change=0
                if piece_taken!="k":
                    balance_change-=values[piece_taken]
                    balance_change+=location_values[piece_taken][coords_end[0]][coords_end[1]]

                if current_piece!="K":
                    balance_change-=location_values[current_piece][coords_start[0]][coords_start[1]]
                    balance_change+=values[current_piece_after]
                    balance_change-=values[current_piece]
                    balance_change+=location_values[current_piece_after][coords_end[0]][coords_end[1]]

                game_data["balance"]+=round(balance_change, 4)

                evaluation, next_move = self.alphabeta(board, alpha, beta, game_data, depth-1, False, memo)

                game_data["winner"]=0

                game_data["balance"]-=balance_change

                board[coords_start[0]][coords_start[1]]=current_piece
                board[coords_end[0]][coords_end[1]]=piece_taken

                alpha = max(alpha, evaluation)
                if evaluation>max_eval:
                    best_move=move

                max_eval = max(evaluation, max_eval)

                if alpha >= beta:
                    memo[transposition_key]=(evaluation, best_move, 1)
                    broken=True
                    break

            memo[board_key]=best_move

            if not broken:
                memo[transposition_key]=(max_eval, best_move, 0)

            return max_eval, best_move

        if cached_move is not None:
            beta = min(beta, cached_move[0])

        min_eval = 10**15
        best_move=None
        broken=False

        moves = self.move_generator.get_moves_from_board(board, False)
        if first_move is not None and moves[-1]!=first_move:
            moves.append(first_move)

        for i in range(len(moves)-1, -1, -1):
            move = moves[i]
            coords_start = utils.square_to_coordinates(move[:2])
            coords_end = utils.square_to_coordinates(move[2:])

            piece_taken = board[coords_end[0]][coords_end[1]]
            current_piece = board[coords_start[0]][coords_start[1]]
            current_piece_after = current_piece

            if piece_taken=="K":
                game_data["winner"]=-1

            if coords_end[0]==7 and current_piece=="p":
                board[coords_start[0]][coords_start[1]]="q"
                current_piece_after="q"

            board[coords_end[0]][coords_end[1]]=board[coords_start[0]][coords_start[1]]
            board[coords_start[0]][coords_start[1]]="."

            balance_change=0
            if piece_taken!="K":
                balance_change-=values[piece_taken]
                balance_change-=location_values[piece_taken][coords_end[0]][coords_end[1]]

            if current_piece!="k":
                balance_change+=values[current_piece_after]
                balance_change-=values[current_piece]
                balance_change+=location_values[current_piece][coords_start[0]][coords_start[1]]
                balance_change-=location_values[current_piece_after][coords_end[0]][coords_end[1]]

            game_data["balance"]+=round(balance_change, 4)

            evaluation, next_move = self.alphabeta(board, alpha, beta, game_data, depth-1, True, memo)

            game_data["winner"]=0

            game_data["balance"]-=balance_change

            board[coords_start[0]][coords_start[1]]=current_piece
            board[coords_end[0]][coords_end[1]]=piece_taken

            beta = min(beta, evaluation)

            if evaluation < min_eval:
                best_move=move

            min_eval = min(min_eval, evaluation)

            if beta <= alpha:
                memo[transposition_key]=(min_eval, best_move, 1)
                broken=True
                break

        memo[board_key]=best_move

        if not broken:
            memo[transposition_key]=(min_eval, best_move, 0)

        return min_eval, best_move
