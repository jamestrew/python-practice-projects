import pygame
from vars import *
from objects import *

# Draw scenario
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.rect(screen, FGCOLOR, pygame.Rect((0, 0), (WIDTH, BORDER)))
pygame.draw.rect(screen, FGCOLOR, pygame.Rect((0, 0), (BORDER, HEIGHT)))
pygame.draw.rect(screen, FGCOLOR, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))


# Instantiate objects
playball = Ball(WIDTH - Ball.RADIUS, HEIGHT // 2, -VELOCITY, -VELOCITY, pygame, screen)
playball.show(FGCOLOR)

paddle = Paddle(HEIGHT // 2, pygame, screen)
paddle.show(PADDLE)

while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

    pygame.display.flip()
    playball.update_pos()
    paddle.update()

pygame.quit()
