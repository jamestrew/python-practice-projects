
class Piece():
    """ color, name"""

    def __init__(self, position, color):
        self.row = position[0]
        self.col = position[1]
        self._color = color

        unit_type = self.__class__.__name__
        if unit_type != "Knight":
            self._unit = unit_type[0].lower()
        else:
            self._unit = 'n'

        self._name = self._color + self._unit

    @property
    def unit_type(self):
        return self._unit

    @property
    def color(self):
        return self._color

    @property
    def name(self):
        return self._name


class Pawn(Piece):

    def __init__(self, position, color):
        super().__init__(position, color)
        self.first_move = True

    def get_moves(self, board):
        """ returns a list(tuples) of all valid moves"""

        # Currently ignores diagonal take move and en passant
        # and ignores impeding pieces
        moves = []
        fwd = -1 if self.color == 'w' else 1

        if not isinstance(board[self.row + fwd][self.col], Null):
            return

        moves.append((self.row + fwd, self.col))
        if self.first_move:
            moves.append((self.row + 2 * fwd, self.col))

        self.first_move = False

        return moves

    def __str__(self):
        return self.color + 'p'


class Rook(Piece):
    def __str__(self):
        return self.color + 'r'


class Knight(Piece):
    def __str__(self):
        return self.color + 'n'


class Bishop(Piece):
    def __str__(self):
        return self.color + 'b'


class Queen(Piece):
    def __str__(self):
        return self.color + 'q'


class King(Piece):
    def __str__(self):
        return self.color + 'k'


class Null:
    """ Represents empty spaces on the chess board """

    def __init__(self):
        self._name = '--'

    @property
    def name(self):
        return self._name
