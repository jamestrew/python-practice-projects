import pygame as pg
import random
from assets import Food, Snake
from constants import *
from grid import Grid

pg.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))


grid = Grid(screen, WIDTH, HEIGHT, S_THICK, "white")
snake = Snake(START_X, START_Y, pg, screen)
snake.display()
food = Food(pg, screen)
food.new(snake.body)

clock = pg.time.Clock()
running = True
while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_RIGHT]:
        snake.vx = 1
        snake.vy = 0
    if keys[pg.K_LEFT]:
        snake.vx = -1
        snake.vy = 0
    if keys[pg.K_UP]:
        snake.vx = 0
        snake.vy = -1
    if keys[pg.K_DOWN]:
        snake.vx = 0
        snake.vy = 1

    snake.move_snake()
    if snake.check_eat(food.x, food.y):
        print("[DEBUG] SNAKE ATE")
        snake.eat()
        food.new(snake.body)

    grid.display()
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
