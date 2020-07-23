import pygame as pg
from board import Board
import os
from resources import *

pg.init()
pg.display.set_caption("GAY CHESS")


def load_images():
    """
    Create a dictionary of pieces and their respective png
    Access img by IMAGES['wp'] --> white pawn img
    """
    pieces = ['r', 'n', 'b', 'q', 'k', 'p']

    for piece in pieces:
        # load black pieces
        img = pg.image.load(os.path.join("images", "b" + piece + ".png"))
        IMAGES['b' + piece] = pg.transform.scale(img, (SQ_SIZE, SQ_SIZE))

        # load white pieces
        img = pg.image.load(os.path.join("images", "w" + piece + ".png"))
        IMAGES['w' + piece] = pg.transform.scale(img, (SQ_SIZE, SQ_SIZE))


def main():
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    clock = pg.time.Clock()
    screen.fill(pg.Color(BACKGROUND))

    game = Board()
    load_images()

    running = True
    while running:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            clock.tick(MAX_FPS)
            pg.display.flip()


if __name__ == '__main__':
    main()
