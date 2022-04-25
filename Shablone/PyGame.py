import pygame as pg
import random

#создание экрана
pg.init()

FPS = 300000000
clock = pg.time.Clock()

screen = pg.display.set_mode((800, 600))

#создание фигур
pg.draw.circle(screen, (242, 10, 165), (400, 300), 100, 3)

pg.draw.circle(screen, (242, 10, 165), (300, 300), 100)

pg.draw.rect(screen, (242, 10, 165), (100, 400, 100, 100))

#создание текста
myfont = pg.font.SysFont(None, 35)
text = myfont.render('It text', True, (242, 10, 79))
screen.blit(text, (450, 100))

i = 1

#вывод на дисплей
pg.display.flip()

#цикл закрытия, цыкл игры
gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            gameover = True

    pg.draw.circle(screen, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),
                   (random.randint(0, 800), random.randint(0, 600)), random.randint(0, 100), random.randint(0, 10))
    i += 5

    clock.tick(FPS)

    pg.display.flip()


if gameover:
    pg.quit()

