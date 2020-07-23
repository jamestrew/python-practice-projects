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

    def __str__(self):
        return str(self.board)
