import pygame as pg


class Grid:
    """
    Create a Grid object capable of drawing a grid of width-height with
    grid sizes size.

    """

    def __init__(self, surface, width, height, size, color):
        self.surface = surface
        self.width = width
        self.height = height
        self.size = size
        self.color = pg.Color(color)
        self.row = self.height // self.size
        self.col = self.width // self.size

    def display(self):
        for row in range(self.row + 1):
            pg.draw.line(self.surface, self.color,
                         (0, row * self.size),
                         (self.width, row * self.size)
                         )

        for col in range(self.col + 1):
            pg.draw.line(self.surface, self.color,
                         (col * self.size, 0),
                         (col * self.size, self.height)
                         )
