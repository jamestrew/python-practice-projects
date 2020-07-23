
class Piece():
    """ color, name"""

    def __init__(self, name, position, white=True, alive=True):
        self.name = name
        self.position = position
        self.alive = alive
        self.white = white


class Pawn(Piece):

    def __init__(self, name, position, white=True, alive=True):
        super().__init__(name, position, white, alive)


bp1 = Pawn("bp1", "E9", white=False)
print(bp1.white)
print(bp1.name)
print(bp1.position)
