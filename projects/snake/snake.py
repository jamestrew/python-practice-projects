import pygame as pg
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
        snake.change_direction(RIGHT)
    elif keys[pg.K_LEFT]:
        snake.change_direction(LEFT)
    elif keys[pg.K_UP]:
        snake.change_direction(UP)
    elif keys[pg.K_DOWN]:
        snake.change_direction(DOWN)

    snake.move_snake()
    if snake.check_eat(food.x, food.y):
        print("[DEBUG] SNAKE ATE")
        snake.eat()
        food.new(snake.body)

    running = snake.check_game_over()
    grid.display()
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
