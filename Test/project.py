import pygame as pg
import random
# from Button import Button
import time
import threading
from pygame_project import main

# иниициализация окна
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.init()
FPS = 120
clock = pg.time.Clock()

# создание блоков
W = pg.display.Info().current_w
H = pg.display.Info().current_h


def func():
    Block.draw_button(coor[0][0], coor[0][1], '')
    Block.draw_button(coor[1][0], coor[1][1], '')
    Block.draw_button(coor[2][0], coor[2][1], '')

    Block.draw_button(coor[3][0], coor[3][1], '')
    Block.draw_button(coor[4][0], coor[4][1], '')
    Block.draw_button(coor[5][0], coor[5][1], '')

    Block.draw_button(coor[6][0], coor[6][1], '')
    Block.draw_button(coor[7][0], coor[7][1], '')
    Block.draw_button(coor[8][0], coor[8][1], '')

class Button:
    def __init__(self, width, height, screen):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactive_color = (240, 166, 148)
        self.active_color = (229, 116, 58)

    # "рисовка" кнопки на экране
    def draw_button(self, x, y, message=None, font=None, button_num=None, done=None):
        global width_text, height_text
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        # width_text, height_text = font.size(message)
        if len(message) >= 1:
            font_button = pg.font.Font(None, self.height)
            text = font_button.render(message, True, self.height)
            width_text = text.get_width()
            height_text = text.get_height()
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pg.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            # что делать после нажатия:
            # if click[0] == 1:
            #     if button_num == 1:
            #         main()
            #     if button_num == 2:
            #         funk()
            #     pg.time.delay(300)
        else:
            pg.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))
        set_text(message, x + (self.width - width_text) // 2, y + (self.height - height_text) // 2, self.screen,
                 font_size=self.height)

    #


def set_text(message, x, y, screen, font_color=(0, 0, 0), font_size=30):
    font_button = pg.font.Font(None, font_size)
    text = font_button.render(message, True, font_color)
    # print(width_text)
    screen.blit(text, (x, y))


Block = Button(150, 100, screen)
s = '123456789'
t = []

while s != '':
    h = random.choice(s)
    p = str(h)
    s = s.replace(p, '')
    t.append(h)

coor = [[random.randint(75, (W // 3) - 150), random.randint(50, (H // 3) - 100)],
        [random.randint(W//3, W-(W//3)-150), random.randint(50, (H // 3) - 100)],
        [random.randint(W-(W//3), W-150), random.randint(50, (H // 3) - 100)],
        [random.randint(75, (W // 3) - 150), random.randint((H//3), H-(H//3)-100)],
        [random.randint(W//3, W-(W//3)-150), random.randint((H//3), H-(H//3)-100)],
        [random.randint(W-(W//3), W-150), random.randint((H//3), H-(H//3)-100)],
        [random.randint(75, (W // 3) - 150), random.randint(H-(H//3), H-100)],
        [random.randint(W//3, W-(W//3)-150), random.randint(H-(H//3), H-100)],
        [random.randint(W-(W//3), W-150), random.randint(H-(H//3), H-100)]]


def funk():
    screen.fill((0, 0, 0))
    Block.draw_button(coor[0][0], coor[0][1], t[0])
    Block.draw_button(coor[1][0], coor[1][1], t[1])
    Block.draw_button(coor[2][0], coor[2][1], t[2])

    Block.draw_button(coor[3][0], coor[3][1], t[3])
    Block.draw_button(coor[4][0], coor[4][1], t[4])
    Block.draw_button(coor[5][0], coor[5][1], t[5])

    Block.draw_button(coor[6][0], coor[6][1], t[6])
    Block.draw_button(coor[7][0], coor[7][1], t[7])
    Block.draw_button(coor[8][0], coor[8][1], t[8])

    # time.sleep(10)
    timer = threading.Timer(10, func)
    timer.start()

    gameover = False
    while not gameover:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    gameover = True
        # func()

        clock.tick(FPS)
        pg.display.flip()

    if gameover:
        pg.quit()

