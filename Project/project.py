import pygame as pg
import random
import threading
from Button import Button

# иниициализация окна
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.init()
FPS = 120
clock = pg.time.Clock()

# создание блоков
W = pg.display.Info().current_w
H = pg.display.Info().current_h


def draw_block():
    global f
    Block.draw_button(coordinates[0][0], coordinates[0][1], '', None, 3)
    Block.draw_button(coordinates[1][0], coordinates[1][1], '', None, 4)
    Block.draw_button(coordinates[2][0], coordinates[2][1], '', None, 5)

    Block.draw_button(coordinates[3][0], coordinates[3][1], '', None, 6)
    Block.draw_button(coordinates[4][0], coordinates[4][1], '', None, 7)
    Block.draw_button(coordinates[5][0], coordinates[5][1], '', None, 8)

    Block.draw_button(coordinates[6][0], coordinates[6][1], '', None, 9)
    Block.draw_button(coordinates[7][0], coordinates[7][1], '', None, 10)
    Block.draw_button(coordinates[8][0], coordinates[8][1], '', None, 11)
    f = True


Block = Button(150, 100, screen, (247, 96, 159), (255, 0, 106))
s = '123456789'
t = []
f = False

while s != '':
    h = random.choice(s)
    p = str(h)
    s = s.replace(p, '')
    t.append(h)


coordinates = [[random.randint(75, (W // 3) - 150), random.randint(50, (H // 3) - 100)],
               [random.randint(W//3, W-(W//3)-150), random.randint(50, (H // 3) - 100)],
               [random.randint(W-(W//3), W-150), random.randint(50, (H // 3) - 100)],
               [random.randint(75, (W // 3) - 150), random.randint((H//3), H-(H//3)-100)],
               [random.randint(W//3, W-(W//3)-150), random.randint((H//3), H-(H//3)-100)],
               [random.randint(W-(W//3), W-150), random.randint((H//3), H-(H//3)-100)],
               [random.randint(75, (W // 3) - 150), random.randint(H-(H//3), H-100)],
               [random.randint(W//3, W-(W//3)-150), random.randint(H-(H//3), H-100)],
               [random.randint(W-(W//3), W-150), random.randint(H-(H//3), H-100)]]


screen.fill((0, 0, 0))
Block.draw_button(coordinates[0][0], coordinates[0][1], t[0], None, 3)
Block.draw_button(coordinates[1][0], coordinates[1][1], t[1], None, 4)
Block.draw_button(coordinates[2][0], coordinates[2][1], t[2], None, 5)

Block.draw_button(coordinates[3][0], coordinates[3][1], t[3], None, 6)
Block.draw_button(coordinates[4][0], coordinates[4][1], t[4], None, 7)
Block.draw_button(coordinates[5][0], coordinates[5][1], t[5], None, 8)

Block.draw_button(coordinates[6][0], coordinates[6][1], t[6], None, 9)
Block.draw_button(coordinates[7][0], coordinates[7][1], t[7], None, 10)
Block.draw_button(coordinates[8][0], coordinates[8][1], t[8], None, 11)


sec = False
gameover = False
while not gameover:
    for event in pg.event.get():
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                gameover = True
                timer.cancel()
    while not sec:
        timer = threading.Timer(10, draw_block)
        timer.start()
        sec = True
    if f:
        draw_block()

    clock.tick(FPS)
    pg.display.flip()

if gameover:
    pg.quit()
