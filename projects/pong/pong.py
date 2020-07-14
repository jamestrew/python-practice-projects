import pygame
from vars import *
from objects import *

# Draw scenario
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))


fgColor = pygame.Color("white")
pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (WIDTH, BORDER)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0, 0), (BORDER, HEIGHT)))
pygame.draw.rect(screen, fgColor, pygame.Rect((0, HEIGHT - BORDER), (WIDTH, BORDER)))


# Instantiate objects
playball = Ball(WIDTH - Ball.RADIUS, HEIGHT // 2, -VELOCITY, 0, pygame, screen)
playball.show(fgColor)

pygame.display.flip()
while True:
    e = pygame.event.poll()
    if e.type == pygame.QUIT:
        break

pygame.quit()
