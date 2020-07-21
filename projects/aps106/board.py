import random
import sys

sys.setrecursionlimit(1500)

class Board():

    __total_score = 0
    __game_over = False

    def __init__(self, dim, grid=None):
        if type(dim) is not tuple:
            raise ValueError(
                f"Expected a board dimension of 2, but found 1."
            )
        if len(dim) != 2:
            raise ValueError(
                f"Expected board dimension of 2, but found {len(dim)}."
            )
        try:
            self.xdim = int(dim[0])
            self.ydim = int(dim[1])
            self.size = self.xdim * self.ydim
        except ValueError:
            raise ValueError(f"Expected int values for grid dimension. Received {type(dim[0])} and {type(dim[0])}.")

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
        if clr == ' ':
            return None

        kills = []
        for check in checks:
            if self.grid[check] == clr:
                kills.append(check)
        return kills

    def check_game_over(self):
        moves = 0
        for i in range(self.size):
            if self.grid[i] == ' ':
                continue
            if self.isPossible(self.grid[i], self.neighbor(i)):
                moves += 1
        if moves == 0:  # no possible moves remaining
            self.__game_over = True
        else:
            self.__game_over = False

    def kill(self, x, y, kill_clr=' '):
        score = 0
        index = self.ydim * x + y
        clr = self.grid[index]
        kills = self.isPossible(clr, self.neighbor(index))
        if not kills:
            return

        self.grid[index] = kill_clr
        score += 1
        while kills:
            for kill in kills:
                if self.grid[kill] != kill_clr:
                    score += 1
                    self.grid[kill] = kill_clr
            newIndex = kills.pop()
            kills.extend(self.isPossible(clr, self.neighbor(newIndex)))

        if kill_clr != ' ':
            return score
        self.__total_score += (score**2)
        self.collapse(self.size - 1)
        self.shift()
        self.check_game_over()

    def auto_kill(self):
        """ kills cell with highest score """
        scores = {}
        for i in range(self.xdim):
            for j in range(self.ydim):
                clr = self.grid[self.ydim * i + j]
                score = self.kill(i, j, 'a')
                if score:
                    scores[(i, j)] = score
                self.kill(i, j, clr)

        highscore = max(scores.values())
        coord_list = list(scores.keys())
        scores_list = list(scores.values())
        x, y = coord_list[scores_list.index(highscore)]
        clr = self.grid[self.ydim * x + y]
        self.kill(x, y)
        return (x, y, clr)

    def collapse(self, index):
        ''' Collapse columns with empty cells down'''
        if index == 0:
            return
        if index == index % self.ydim:
            return self.collapse(index + (self.xdim - 1) * self.ydim - 1)
        if self.grid[index] != ' ':
            return self.collapse(index - self.ydim)

        for i in range(index, index % self.ydim - 1, -self.ydim):
            if self.grid[i] != ' ':
                self.grid[index] = self.grid[i]
                self.grid[i] = ' '
                break
        return self.collapse(index - self.ydim)

    def shift(self):
        ''' Shift columns over to the left into a empty column'''
        for i in range(self.ydim - 1):
            col_indices = [k + i for k in range(self.size) if k % self.ydim == 0]
            col_clr = [self.grid[j] for j in col_indices if self.grid[j] == ' ']
            if len(col_clr) == self.xdim:  # all cells in the column empty
                for j in col_indices:
                    self.grid[j] = self.grid[j + 1]
                    self.grid[j + 1] = ' '

        for i in range(self.size - self.ydim, self.size - 1, 1):
            if self.grid[i] == ' ' and self.grid[i + 1] != ' ':
                self.shift()

    @property
    def total_score(self):
        return self.__total_score

    @property
    def game_over(self):
        return self.__game_over
