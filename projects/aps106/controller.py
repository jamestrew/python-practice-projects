from board import Board
from GUI import Game
import os

class Controller:

    __mode = None
    __grid = None

    def start_GUI(self):
        self.game = Game(self)
        self.game.mainloop()

    def init_mode(self, mode):
        print(f"[DEBUG]: Gamemode selected {mode}")

    def init_grid(self, grid_val):
        if grid_val == 1:
            fname = os.path.join("Grid", "SmallGrid.txt")
        elif grid_val == 2:
            fname = os.path.join("Grid", "LargeGrid.txt")  # temporary for testing
        else:
            fname = os.path.join("Grid", "test.txt")  # temporary for testing
        print(f"[DEBUG]: File selected {fname}")

        with open(fname) as f:
            rows = f.readlines()
        self.__grid_dim = tuple(rows[0].split())
        content = [letter for row in rows[1:] for letter in row.strip()]
        self.__grid = Board(self.__grid_dim, content)

        with open("move_log.txt", "w") as f:
            print(self.__grid, end='\n\n', file=f)
        return self.__grid

    def grid_dim(self):
        return (self.__grid.xdim, self.__grid.ydim)

    def update_cell(self, dim):
        x, y = dim
        self.__grid.kill(x, y)
        self.log_moves(x, y)
        return self.__grid.total_score

    def log_moves(self, x, y):
        with open("move_log.txt", "a") as f:
            print(f"{x} {y} {self.__grid[x, y]}", file=f)
            print(self.__grid, file=f)
            print(file=f)
