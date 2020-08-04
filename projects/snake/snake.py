import pygame as pg
from assets import Food, Snake
from constants import *
from grid import Grid

pg.init()
pg.font.init()
pg.display.set_caption("sssssssssSSNAKE")
screen = pg.display.set_mode((WIDTH, HEIGHT))


# grid = Grid(screen, WIDTH, HEIGHT, S_THICK, "white")
snake = Snake(START_X, START_Y, pg, screen)
snake.display()
food = Food(pg, screen)
food.new(snake.body)


lost_font = pg.font.SysFont("comic sans", 150)
score_font = pg.font.SysFont("comic sans", 100)
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
        snake.eat()
        food.new(snake.body)

    # grid.display()
    if snake.game_over():
        lost_label = lost_font.render("GAME OVER", 1, pg.Color("red"))
        score_label = score_font.render(f"SCORE: {len(snake.body) - snake.init_length}", 1, pg.Color("red"))
        screen.blit(lost_label, (WIDTH // 2 - lost_label.get_width() // 2, 400))
        screen.blit(score_label, (WIDTH // 2 - score_label.get_width() // 2, 500))
    clock.tick(FPS)
    pg.display.flip()

pg.quit()
