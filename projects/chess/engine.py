from pieces import Bishop
from pieces import King
from pieces import Rook
from pieces import Pawn
from pieces import Queen
from pieces import Knight
from resources import *
import numpy as np

class Board():

    def __init__(self, side='w'):
        self.side = side  # side closes to you aka the color you are playing

        if self.side == 'w':
            self.opponent = 'b'
        else:
            self.opponent = 'w'

        self.white_to_move = True
        self.moves = []  # log of moves

        self.board = np.full((DIM, DIM), '--')

        self.board[0][0] = Rook((0, 0), self.opponent)
        self.board[0][1] = Knight((0, 1), self.opponent)
        self.board[0][2] = Bishop((0, 2), self.opponent)
        self.board[0][5] = Bishop((0, 5), self.opponent)
        self.board[0][6] = Knight((0, 6), self.opponent)
        self.board[0][7] = Rook((0, 7), self.opponent)

        self.board[1][0] = Pawn((1, 0), self.opponent)
        self.board[1][1] = Pawn((1, 0), self.opponent)
        self.board[1][2] = Pawn((1, 0), self.opponent)
        self.board[1][3] = Pawn((1, 0), self.opponent)
        self.board[1][4] = Pawn((1, 0), self.opponent)
        self.board[1][5] = Pawn((1, 0), self.opponent)
        self.board[1][6] = Pawn((1, 0), self.opponent)
        self.board[1][7] = Pawn((1, 0), self.opponent)

        self.board[6][0] = Pawn((1, 0), self.side)
        self.board[6][1] = Pawn((1, 0), self.side)
        self.board[6][2] = Pawn((1, 0), self.side)
        self.board[6][3] = Pawn((1, 0), self.side)
        self.board[6][4] = Pawn((1, 0), self.side)
        self.board[6][5] = Pawn((1, 0), self.side)
        self.board[6][6] = Pawn((1, 0), self.side)
        self.board[6][7] = Pawn((1, 0), self.side)

        self.board[7][0] = Rook((0, 0), self.side)
        self.board[7][1] = Knight((0, 1), self.side)
        self.board[7][2] = Bishop((0, 2), self.side)
        self.board[7][5] = Bishop((0, 5), self.side)
        self.board[7][6] = Knight((0, 6), self.side)
        self.board[7][7] = Rook((0, 7), self.side)

        # flip the King/Queen depending on the side
        if self.side == 'w':
            qcol = 3
            kcol = 4
        else:
            qcol = 4
            kcol = 3

        self.board[0][qcol] = Queen((0, 3), self.opponent)
        self.board[0][kcol] = King((0, 4), self.opponent)
        self.board[7][qcol] = Queen((0, 3), self.side)
        self.board[7][kcol] = King((0, 4), self.side)

    def make_move(self, move):
        self.board[move.select_row][move.select_col] = '--'
        self.board[move.move_row][move.move_col] = move.piece_moved
        self.white_to_move = not white_to_move

    def __str__(self):
        return str(self.board)

class Move():

    # Rank - File notation
    files = {  # "rows"
        0: 'a', 1: 'b', 2: 'c', 3: 'd',
        4: 'e', 5: 'f', 6: 'g', 7: 'h'
    }

    ranks = {  # "columns"
        0: 8, 1: 7, 2: 6, 3: 5,
        4: 4, 5: 3, 6: 2, 7: 1
    }

    def __init__(self, select_pos, move_pos, board):
        self.select_row = select_pos[0]
        self.select_col = select_pos[1]
        self.move_row = move_pos[0]
        self.move_col = move_pos[1]
        self.piece_moved = board[self.select_row][self.select_col]
        self.piece_capt = board[self.move_row][self.move_col]

    def make_chess_notation(self):
        return self.get_rank_file(self.select_row, self.select_col) + \
            self.get_rank_file(self.move_row, self.move_col)

    def get_rank_file(self, row, col):
        return str(files[row]) + str(rank[col])
