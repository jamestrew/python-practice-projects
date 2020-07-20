import tkinter as tk
from resource import *


class Game(tk.Frame):

    __mode = None
    __grid_val = None
    __row_size = None
    __col_size = None

    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.pack()
        self.config(width=WIDTH, height=HEIGHT)
        self.grid_propagate(False)
        self.master.title("Check Out Line")

        self.menu()

    def menu(self):
        self.title_frame = tk.Frame(self)
        self.title_frame.grid(row=0, stick='nsew')
        self.menu_frame = tk.Frame(self)
        self.menu_frame.grid(row=1, sticky='nsew')

        """ --- LABELS ---"""
        title = tk.Label(self.title_frame, text='Check Out Line', fg=BLACK,
                         font=FONTS[55]
                         )
        mode = tk.Label(self.menu_frame, text='MODE:', fg=BLACK,
                        font=FONTS[30]
                        )
        board = tk.Label(self.menu_frame, text='GRID:', fg=BLACK,
                         font=FONTS[30]
                         )

        title.grid(row=0, column=0, padx=(30, 5), pady=5, sticky='ew')
        mode.grid(row=1, column=0, padx=(30, 5), pady=5, sticky='w')
        board.grid(row=2, column=0, padx=(30, 5), pady=5, sticky='w')

        """ --- BUTTONS ---"""
        def set_mode(mode):
            ''' Configure buttons and sets gamemode '''
            self.__mode = mode
            comp_play.configure(relief='raised')
            user_play.configure(relief='raised')
            if mode == 1:
                comp_play.configure(relief='sunken')
            else:
                user_play.configure(relief='sunken')
            check_play()

        def set_grid(grid):
            ''' Configures buttons and sets difficulty '''
            small.configure(relief='raised')
            medium.configure(relief='raised')
            large.configure(relief='raised')

            self.__grid_val = grid
            if grid == 1:
                small.configure(relief='sunken')
            elif grid == 2:
                medium.configure(relief='sunken')
            else:
                large.configure(relief='sunken')
            check_play()

        def check_play():
            ''' Enable the PLAY button if gamemode and difficulty are selected'''
            if self.__mode is not None and self.__grid_val is not None:
                play_button.config(state="normal")

        def start_game():
            self.controller.init_mode(self.__mode)
            self.board = self.controller.init_grid(self.__grid_val)

            self.title_frame.destroy()
            self.menu_frame.destroy()

            self.init_game()

        # Gamemode
        comp_play = tk.Button(self.menu_frame, text='COMPUTER', fg=BLACK,
                              font=FONTS[25], command=lambda: set_mode(1)
                              )
        user_play = tk.Button(self.menu_frame, text='USER PLAY', fg=BLACK,
                              font=FONTS[25], command=lambda: set_mode(2)
                              )
        comp_play.grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        user_play.grid(row=1, column=2, padx=5, pady=5, sticky='ew')

        # Board size
        small = tk.Button(self.menu_frame, text='SMALL', fg=BLACK,
                          font=FONTS[25], command=lambda: set_grid(1)
                          )
        medium = tk.Button(self.menu_frame, text='MEDIUM', fg=BLACK,
                           font=FONTS[25], command=lambda: set_grid(2)
                           )
        large = tk.Button(self.menu_frame, text='LARGE', fg=BLACK,
                          font=FONTS[25], command=lambda: set_grid(3)
                          )  # Large temporarily set to test board
        small.grid(row=2, column=1, padx=5, pady=5, sticky='ew')
        medium.grid(row=2, column=2, padx=5, pady=5, sticky='ew')
        large.grid(row=2, column=3, padx=5, pady=5, sticky='ew')

        # Play button
        play_button = tk.Button(self.menu_frame, text='PLAY', bg=WHITE, fg=BLACK,
                                font=FONTS[25],
                                command=start_game
                                )
        play_button.config(state="disabled")
        play_button.grid(row=3, column=2, padx=5, pady=5)

    def init_game(self):
        """
        Create base frame/canvas that modular in size. Max size fits 36x36 grid.
        (Main frame: width=WIDTH, height=HEIGHT) --> 20x20 for cells
        Have space for score.

        Each color represented by cells of varying color. No border/padding.
        """

        self.game_frame = tk.Frame(self, bg=BACK, width=WIDTH, height=HEIGHT, bd=5)
        self.game_frame.grid(row=0, column=1, stick='nsew')
        self.game_frame.grid_propagate(False)
        score_frame = tk.Frame(self, bg=BACK, bd=5)
        score_frame.grid(row=0, column=0, sticky='nsew')

        score_header = tk.Label(score_frame, text="SCORE:", font=FONTS[30])
        self.score_label = tk.Label(score_frame, text=0, font=FONTS[25])
        score_header.pack()
        self.score_label.pack()

        replay = tk.Button(score_frame, text="REPLAY", font=FONTS[20], command=self.replay)
        replay.pack()

        self.xdim, self.ydim = self.controller.grid_dim()
        self.cell_dim = min(WIDTH // self.xdim, HEIGHT // self.ydim)

        self.cells = []
        for i in range(self.xdim):
            row = []
            for j in range(self.ydim):
                cell_clr = self.check_clr(i, j)
                cell_frame = tk.Frame(self.game_frame, width=self.cell_dim, height=self.cell_dim, bg=cell_clr)
                cell_frame.grid(row=i, column=j)
                cell_data = {"frame": cell_frame}
                row.append(cell_data)
            self.cells.append(row)

        self.play_game()

    def replay(self):
        self.board = self.controller.init_grid(self.__grid_val)
        # Refresh board
        for i in range(self.xdim):
            for j in range(self.ydim):
                cell_clr = self.check_clr(i, j)
                self.cells[i][j]["frame"].config(bg=cell_clr)

        self.score_label.config(text=self.__score)  # Refresh score

    def check_clr(self, i, j):
        if self.board[i, j] == 'r':
            return RED
        elif self.board[i, j] == 'g':
            return GREEN
        elif self.board[i, j] == 'b':
            return BLUE
        elif self.board[i, j] == 'y':
            return YELLOW
        else:
            return WHITE

    def play_game(self):
        self.master.bind("<Button-1>", self.kill_cell)
        self.__selection = None
        self.__score = None

    def kill_cell(self, event):
        ''' Get select widget, kill selected cell '''

        widget = str(event.widget)
        print(widget, widget[:21])
        if widget[:21] != ".!game.!frame3.!frame":
            return

        cell_index = widget[21:]
        if not cell_index:
            self.__selection = (0, 0)
        else:
            cell_index = int(cell_index) - 1
            self.__selection = (cell_index // self.ydim, cell_index % self.ydim)

        self.__score = self.controller.update_cell(self.__selection)

        # Update board
        for i in range(self.xdim):
            for j in range(self.ydim):
                cell_clr = self.check_clr(i, j)
                self.cells[i][j]["frame"].config(bg=cell_clr)

        # Update score
        self.score_label.config(text=self.__score)
