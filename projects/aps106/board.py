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

        checks = []
        if index < self.size - self.ydim:  # bottom
            checks.append(index + self.ydim)
        if index >= self.ydim:  # top
            checks.append(index - self.ydim)
        if index not in [i for i in range(self.size) if
                         i % self.ydim == 0]:  # left
            checks.append(index - 1)
        if index not in [i + self.ydim - 1 for i in range(self.size) if
                         i % self.ydim == 0]:  # right
            checks.append(index + 1)
        return checks

    def isPossible(self, clr, checks):
        ''' returns list of possible kills'''
        kills = []
        for check in checks:
            if self.grid[check] == clr:
                kills.append(check)
        return kills

    def gameOver(self):
        checks = 0
        for i in self.size:
            if self.isPossible(i):
                checks += 1
        if checks < 0:
            return True
        return False

    def kill(self, x, y):
        score = 0
        index = self.ydim * x + y
        clr = self.grid[index]
        kills = self.isPossible(clr, self.neighbor(index))
        if not kills:
            print("Move not possible")
            return

        self.grid[index] = ' '
        score += 1
        while kills:
            for kill in kills:
                if self.grid[kill] != ' ':
                    score += 1
                    self.grid[kill] = ' '
            newIndex = kills.pop()
            kills.extend(self.isPossible(clr, self.neighbor(newIndex)))

        print(score)
        self.collapse()
        self.shift()

    def collapse(self):
        ''' Collapse columns with empty cells down'''
        for i in range(self.size - 1, self.ydim - 1, -1):
            # if current cell empty, fill it with cell above
            if self.grid[i] == ' ':
                self.grid[i] = self.grid[i - self.ydim]
                self.grid[i - self.ydim] = ' '

    def shift(self):
        ''' Shift columns over to the left into a empty column'''
        for i in range(self.ydim - 1):
            col_clr = []
            col_indices = [k + i for k in range(self.size) if k % self.ydim == 0]
            for j in col_indices:
                if self.grid[j] == ' ':
                    col_clr.append(1)  # cell is empty
                else:
                    col_clr.append(0)
            if all(col_clr):  # all cells in the column empty
                for j in col_indices:
                    self.grid[j] = self.grid[j + 1]
                    self.grid[j + 1] = ' '
