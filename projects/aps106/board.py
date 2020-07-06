import random

class Board():

    def __init__(self, dim, grid=None):
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

        if grid is None:
            self.grid = random.choices(['r', 'g', 'b', 'y'], k=self.size)
        else:
            self.grid = grid

    def __str__(self):
        return '\n'.join(' '.join(self.grid[i:i + self.ydim])
                         for i in range(0, self.size, self.ydim))

    def __getitem__(self, key):
        return self.grid[key[0] * self.ydim + key[1]]

    def isPossible(self, x, y):
        ''' check whether move is possible
            if possible, return score, otherwise return False
        '''
        index = self.ydim * x + y
        clr = self.grid[index]

        leftindex = index - 1
        rightindex = index + 1
        topindex = index - self.ydim
        bottomindex = index + self.ydim

        checks = [leftindex, rightindex, topindex, bottomindex]

        counts = 0
        for check in checks:
            try:
                if self.grid[check] == clr:
                    counts += 1  # self.isPossible(check // self.ydim, check % self.ydim)
            except IndexError:
                continue

        return counts
