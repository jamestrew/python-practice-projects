from pieces import Bishop
from pieces import King
from pieces import Rook
from pieces import Pawn
from pieces import Queen
from pieces import Knight
from pieces import Null
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

        self.board = np.full((DIM, DIM), Null(), dtype=object)
        # self.board = [['--'] * DIM for _ in range(DIM)]

        self.board[0][0] = Rook((0, 0), self.opponent)
        self.board[0][1] = Knight((0, 1), self.opponent)
        self.board[0][2] = Bishop((0, 2), self.opponent)
        self.board[0][5] = Bishop((0, 5), self.opponent)
        self.board[0][6] = Knight((0, 6), self.opponent)
        self.board[0][7] = Rook((0, 7), self.opponent)

        self.board[1][0] = Pawn((1, 0), self.opponent)
        self.board[1][1] = Pawn((1, 1), self.opponent)
        self.board[1][2] = Pawn((1, 2), self.opponent)
        self.board[1][3] = Pawn((1, 3), self.opponent)
        self.board[1][4] = Pawn((1, 4), self.opponent)
        self.board[1][5] = Pawn((1, 5), self.opponent)
        self.board[1][6] = Pawn((1, 6), self.opponent)
        self.board[1][7] = Pawn((1, 7), self.opponent)

        self.board[6][0] = Pawn((6, 0), self.side)
        self.board[6][1] = Pawn((6, 1), self.side)
        self.board[6][2] = Pawn((6, 2), self.side)
        self.board[6][3] = Pawn((6, 3), self.side)
        self.board[6][4] = Pawn((6, 4), self.side)
        self.board[6][5] = Pawn((6, 5), self.side)
        self.board[6][6] = Pawn((6, 6), self.side)
        self.board[6][7] = Pawn((6, 7), self.side)

        self.board[7][0] = Rook((7, 0), self.side)
        self.board[7][1] = Knight((7, 1), self.side)
        self.board[7][2] = Bishop((7, 2), self.side)
        self.board[7][5] = Bishop((7, 5), self.side)
        self.board[7][6] = Knight((7, 6), self.side)
        self.board[7][7] = Rook((7, 7), self.side)

        # flip the King/Queen depending on the side
        if self.side == 'w':
            qcol = 3
            kcol = 4
        else:
            qcol = 4
            kcol = 3

        self.board[0][qcol] = Queen((0, 3), self.opponent)
        self.board[0][kcol] = King((0, 4), self.opponent)
        self.board[7][qcol] = Queen((7, 3), self.side)
        self.board[7][kcol] = King((7, 4), self.side)

    def make_move(self, move):
        self.board[move.select_row][move.select_col] = Null()
        self.board[move.move_row][move.move_col] = move.piece_moved
        self.moves.append(move)
        print(f"[DEBUG]: {self.moves[-1]}")
        self.white_to_move = not self.white_to_move

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

    def __init__(self, select_pos, ctrl):
        self.ctrl = ctrl  # game instance
        self.select_row = select_pos[0]
        self.select_col = select_pos[1]
        self.piece_moved = self.ctrl.board[self.select_row][self.select_col]
        self._moves = self.piece_moved.get_moves(self.ctrl.board)
        self.debug("init")  # TEMP - debug

    def complete_move(self, move_pos):
        """
        Check that the move is valid, if so play move
        Currently not concerned checking for _moves that will result in
        own king being checked
        """

        if move_pos == (self.select_row, self.select_col):
            return

        # Check it's the right color's turn
        turn = 'w' if self.ctrl.white_to_move else 'b'
        if self.piece_moved.color != turn:  # not the color's turn
            self.debug("turn")
            return

        if move_pos not in self._moves:  # move coord not possible
            self.debug("invalid")
            return

        self.move_row = move_pos[0]
        self.move_col = move_pos[1]
        self.piece_capt = self.ctrl.board[self.move_row][self.move_col]
        self.ctrl.make_move(self)  # makes the changes on the board

    def __repr__(self):
        piece_name = self.piece_moved.unit_type
        if piece_name == 'p':
            piece_name = ''
        return piece_name.upper() + \
            self.get_rank_file(self.move_row, self.move_col)

    def get_rank_file(self, row, col):
        """ Convert array row/col to chess grid notation """
        return str(self.files[col]) + str(self.ranks[row])

    @property
    def moves(self):
        return self._moves

    def debug(self, debug_type):
        pass
        # if debug_type == "init":
        #     print(self.get_rank_file(self.piece_moved.row, self.piece_moved.col))
        #     for r, c in self._moves:
        #         print(f"({self.get_rank_file(r, c)})", end=' ')
        #     print()
        # elif debug_type == "turn":
        #     print("Not your turn")
        # elif debug_type == "invalid":
        #     print("Invalid move")
