import pygame as pg

# создание экрана
pg.init()
FPS = 120
clock = pg.time.Clock()
screen = pg.display.set_mode((800, 600))

# вывод на дисплей
pg.display.flip()

gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True

    clock.tick(FPS)
    pg.display.flip()

if gameover:
    pg.quit()

