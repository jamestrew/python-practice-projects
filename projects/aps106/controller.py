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
            fname = os.path.join("Grid", "MediumGrid.txt")
        else:
            fname = os.path.join("Grid", "LargeGrid.txt")
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

    def update_cell(self, dim=None):
        if dim is not None:
            x, y = dim
            clr = self.__grid[x, y]
            self.__grid.kill(x, y)
        else:
            # Call auto kill function in puzzle which returns x, y, clr
            x, y, clr = self.__grid.auto_kill()

        self.log_moves(x, y, clr)
        return (self.__grid.total_score, self.__grid.game_over)

    def log_moves(self, x, y, clr):
        with open("move_log.txt", "a") as f:
            print(f"{x} {y} {clr}", file=f)
            print(self.__grid, file=f)
            print(file=f)
