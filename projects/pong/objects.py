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

    def update_pos(self, color):
        self.x += self.vx
        self.y += self.vy
        self.show(color)


class Paddle:
    pass
