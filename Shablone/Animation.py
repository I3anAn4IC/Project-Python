import pygame as pg

#создание экрана
pg.init()

FPS = 120
clock = pg.time.Clock()

WIDTH = 800
HEIGHT = 600

screen = pg.display.set_mode((WIDTH, HEIGHT))

canvas = pg.Surface((100, 100))

canvas_rect = canvas.get_rect()
canvas_rect.center = (800/2, 600/2)
print(canvas_rect)
canvas.fill((247, 7, 95))
pg.draw.circle(canvas, (199, 7, 247), (50, 50), 50)
screen.blit(canvas, canvas_rect)

#вывод на дисплей
pg.display.flip()

#цикл закрытия, цыкл игры
gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True
    screen.fill((0, 0, 0))
    if canvas_rect.left > WIDTH:
        canvas_rect.right = 0
    canvas_rect.x += 2
    screen.blit(canvas, canvas_rect)
    clock.tick(FPS)
    pg.display.flip()


if gameover:
    pg.quit()

