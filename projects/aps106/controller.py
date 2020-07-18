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
        print(self.__grid.xdim, self.__grid.ydim)
        print(self.__grid)
        return self.__grid

    def grid_dim(self):
        return (self.__grid.xdim, self.__grid.ydim)
