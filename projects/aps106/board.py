import random

class Board():

    grid = []

    def __init__(self, dim):
        # validate len(dim) = 2
        # validate that each value is positive int
        if type(dim) is not tuple:
            raise ValueError(
                f"Expected a board dimension of 2, but found 1."
            )
        if len(dim) != 2:
            raise ValueError(
                f"Expected board dimension of 2, but found {len(dim)}."
            )
        if type(dim[0]) is not int or type(dim[1]) is not int:
            raise TypeError(
                f"Expected integer dimensions."
            )

        self.xdim = dim[0]
        self.ydim = dim[1]
        self.size = self.xdim * self.ydim
        self.grid = random.choices(['r', 'g', 'b', 'y'], k=self.size)

    def __str__(self):
        return '\n'.join(' '.join(self.grid[i:i + self.ydim]) for i in range(0, self.size, self.ydim))
