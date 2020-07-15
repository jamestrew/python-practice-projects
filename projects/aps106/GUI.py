import tkinter as tk


class Game(tk.Frame):

    def __init__(self):
        super().__init__()
        self.grid()
        self.master.title("Check Out Line")
        self.config(width=800, height=640)
