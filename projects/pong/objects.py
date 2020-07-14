from vars import *

class Ball:

    RADIUS = 10

    def __init__(self, x, y, vx, vy, handle, display):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.handle = handle
        self.display = display

    def show(self, color):
        self.handle.draw.circle(self.display, color, (self.x, self.y), self.RADIUS)

    def update_pos(self):
        self.show(BGCOLOR)  # hide old ball

        tempx = self.x + self.vx
        tempy = self.y + self.vy

        # Collision detection
        if (tempx - self.RADIUS) <= BORDER:
            self.vx *= -1
        if (tempy - self.RADIUS) <= BORDER:
            self.vy *= -1
        elif (tempy + self.RADIUS) >= (HEIGHT - BORDER):
            self.vy *= -1

        # Update new position with collision detection
        self.x += self.vx
        self.y += self.vy
        self.show(FGCOLOR)  # display new ball


class Paddle:
    WIDTH = 20
    HEIGHT = 100

    def __init__(self, y, handle, display):
        self.y = y
        self.handle = handle
        self.display = display

    def show(self, color):
        self.handle.draw.rect(self.display, color, self.handle.Rect((WIDTH - self.WIDTH, self.y - self.HEIGHT // 2), (self.WIDTH, self.HEIGHT)))

    def update(self):
        self.show(BGCOLOR)
        self.y = self.handle.mouse.get_pos()[1]

        if self.y < BORDER + self.HEIGHT // 2:
            self.y = BORDER + self.HEIGHT // 2
        elif self.y > (HEIGHT - BORDER - self.HEIGHT // 2):
            self.y = HEIGHT - BORDER - self.HEIGHT // 2

        self.show(PADDLE)
