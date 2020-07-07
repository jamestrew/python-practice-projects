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

    def neighbor(self, index):
        ''' returns an array of the neighbors indices'''

        leftindex = index - 1
        rightindex = index + 1
        topindex = index - self.ydim
        bottomindex = index + self.ydim

        checks = []
        if index < self.size - self.ydim:  # bottom
            checks.append(bottomindex)
        if index >= self.ydim:  # top
            checks.append(topindex)
        if index not in [i for i in range(self.size) if
                         i % self.ydim == 0]:  # left
            checks.append(leftindex)
        if index not in [i + self.ydim - 1 for i in range(self.size) if
                         i % self.ydim == 0]:  # right
            checks.append(rightindex)
        return checks

    def isPossible(self, clr, checks):
        ''' returns True if move is possible, otherwise return False'''
        for check in checks:
            try:
                if self.grid[check] == clr:
                    return True  # self.isPossible(check // self.ydim, check % self.ydim)
            except IndexError:
                continue
        return False

    def gameOver(self):
        checks = 0
        for i in self.size:
            if self.isPossible(i):
                checks += 1
        if checks < 0:
            return True
        return False

    def kill(self, x, y):
        index = self.ydim * x + y
        clr = self.grid[index]
        if not self.isPossible(clr, self.neighbor(index)):
            print("Move not possible")
        else:
            print(f"Killing all pieces with the color {clr}")
