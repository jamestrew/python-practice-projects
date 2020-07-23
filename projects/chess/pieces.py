
class Piece():
    """ color, name"""

    def __init__(self, position, color, alive=True):
        self.position = position
        self.color = color
        self.alive = alive


class Pawn(Piece):

    def __repr__(self):
        return self.color + 'p'


class Rook(Piece):
    def __repr__(self):
        return self.color + 'r'


class Knight(Piece):
    def __repr__(self):
        return self.color + 'n'


class Bishop(Piece):
    def __repr__(self):
        return self.color + 'b'


class Queen(Piece):
    def __repr__(self):
        return self.color + 'q'


class King(Piece):
    def __repr__(self):
        return self.color + 'k'
