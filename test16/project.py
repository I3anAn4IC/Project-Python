import pygame as pg
import random
import threading

# иниициализация окна
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.init()
FPS = 120
clock = pg.time.Clock()

# создание блоков
W = pg.display.Info().current_w
H = pg.display.Info().current_h


class Button:
    def __init__(self, width, height, screen, inactive_color=(240, 166, 148), active_color=(229, 116, 58)):
        self.screen = screen
        self.width = width
        self.height = height
        self.inactive_color = inactive_color
        self.active_color = active_color

    # "рисовка" кнопки на экране
    def draw_button(self, x, y, message=None, font=None, button_num=None, done=None):
        global width_text, height_text
        mouse = pg.mouse.get_pos()
        click = pg.mouse.get_pressed()
        if len(message) >= 1:
            font_button = pg.font.Font(None, self.height)
            text = font_button.render(message, True, self.height)
            width_text = text.get_width()
            height_text = text.get_height()

        if x < mouse[0] < x + self.width and y < mouse[1] < y + self.height:
            pg.draw.rect(self.screen, self.inactive_color, (x, y, self.width, self.height))
            if click[0] == 1:
                pg.time.delay(300)
        else:
            pg.draw.rect(self.screen, self.active_color, (x, y, self.width, self.height))

        set_text(message, x + (self.width - width_text) // 2, y + (self.height - height_text) // 2, self.screen,
                 font_size=self.height)


def set_text(message, x, y, screen, font_color=(0, 0, 0), font_size=30):
    font_button = pg.font.Font(None, font_size)
    text = font_button.render(message, True, font_color)
    screen.blit(text, (x, y))


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


def click_button(height, width, inactive_color, active_color, screen, x, y, button_num):
    global block_com
    mouse = pg.mouse.get_pos()
    click = pg.mouse.get_pressed()
    if x < mouse[0] < x + width and y < mouse[1] < y + height:
        pg.draw.rect(screen, inactive_color, (x, y, width, height))
        # что делать после нажатия:
        if click[0] == 1:
            if button_num == 3:
                block_com = 1
                block_command()
            if button_num == 4:
                block_com = 2
            if button_num == 5:
                block_com = 3
            if button_num == 6:
                block_com = 4
            if button_num == 7:
                block_com = 5
            if button_num == 8:
                block_com = 6
            if button_num == 9:
                block_com = 7
            if button_num == 10:
                block_com = 8
            if button_num == 11:
                block_com = 9
            pg.time.delay(300)
    else:
        pg.draw.rect(screen, active_color, (x, y, width, height))


block_com = 0
block_comm = False


def block_command():
    global block_com, block_comm
    if block_com == 1 and not block_comm:
        block_comm = True
        Block.draw_button(coordinates[0][0], coordinates[0][1], str(t[0]), None, 3)



Block = Button(150, 100, screen, (247, 96, 159), (255, 0, 106))
s = '123456789'
t = []
f = False

while s != '':
    h = random.choice(s)
    p = str(h)
    s = s.replace(p, '')
    t.append(h)

# for i in range(10):
#     h = random.randint(10, 100)
#     t.append(h)


coordinates = [[random.randint(75, (W // 3) - 150), random.randint(50, (H // 3) - 100)],
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
    Block.draw_button(coordinates[0][0], coordinates[0][1], str(t[0]), None, 3)
    Block.draw_button(coordinates[1][0], coordinates[1][1], str(t[1]), None, 4)
    Block.draw_button(coordinates[2][0], coordinates[2][1], str(t[2]), None, 5)

    Block.draw_button(coordinates[3][0], coordinates[3][1], str(t[3]), None, 6)
    Block.draw_button(coordinates[4][0], coordinates[4][1], str(t[4]), None, 7)
    Block.draw_button(coordinates[5][0], coordinates[5][1], str(t[5]), None, 8)

    Block.draw_button(coordinates[6][0], coordinates[6][1], str(t[6]), None, 9)
    Block.draw_button(coordinates[7][0], coordinates[7][1], str(t[7]), None, 10)
    Block.draw_button(coordinates[8][0], coordinates[8][1], str(t[8]), None, 11)

    sec = False
    gameover = False
    while not gameover:
        for event in pg.event.get():
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    screen.fill((0, 0, 0))
                    timer.cancel()
                    return
        while not sec:
            timer = threading.Timer(2, draw_block)
            timer.start()
            sec = True
        if f:
            draw_block()

        clock.tick(FPS)
        pg.display.flip()

    if gameover:
        pg.quit()


funk()

